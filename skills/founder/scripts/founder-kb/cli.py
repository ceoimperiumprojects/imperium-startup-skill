#!/usr/bin/env python3
"""Founder KB — AI-powered knowledge base CLI for founders."""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="founder-kb",
    help="AI-powered knowledge base for founders. Semantic search over startup literature.",
    no_args_is_help=True,
)

console = Console()
err_console = Console(stderr=True)

# ── Global state ──────────────────────────────────────────────────────────────

_db_path: str = "./chroma_db"
_json_output: bool = False
_vector_store = None

META_FILE: Path = Path("knowledge_meta.json")


def _out(data, human_text: str):
    """Print JSON or human-readable text depending on --json flag."""
    if _json_output:
        typer.echo(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        console.print(human_text)


def _get_vs():
    global _vector_store
    if _vector_store is None:
        err_console.print("[dim]Loading embedding model...[/dim]")
        from src.vector_store import VectorStore
        _vector_store = VectorStore(persist_directory=_db_path)
    return _vector_store


def _load_meta() -> dict:
    if META_FILE.exists():
        return json.loads(META_FILE.read_text(encoding="utf-8"))
    return {"tags": {}, "annotations": {}}


def _save_meta(data: dict):
    META_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def _ingest_text(text: str, source: str, use_semantic: bool = True) -> int:
    """Chunk text and add to vector store. Returns number of chunks added."""
    from src.chunker import create_chunks_with_metadata
    chunks = create_chunks_with_metadata(text=text, source=source, use_semantic=use_semantic)
    texts = [c["text"] for c in chunks]
    metadatas = [c["metadata"] for c in chunks]
    ids = [f"{source}_{c['metadata']['chunk_index']}" for c in chunks]
    vs = _get_vs()
    vs.add_documents(texts=texts, metadatas=metadatas, ids=ids)
    return len(chunks)


def _extract_text_from_file(file_path: Path) -> str:
    """Extract text from PDF, EPUB, or TXT file."""
    ext = file_path.suffix.lower()
    if ext == ".pdf":
        from src.pdf_processor import extract_text_from_pdf
        return extract_text_from_pdf(str(file_path))
    elif ext == ".epub":
        from src.epub_processor import extract_text_from_epub
        return extract_text_from_epub(str(file_path))
    elif ext == ".txt":
        return file_path.read_text(encoding="utf-8")
    else:
        raise typer.BadParameter(f"Unsupported file type: {ext}. Supported: .pdf, .epub, .txt")


def _fetch_url_text(url: str) -> str:
    """Fetch a URL and extract text content."""
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url, timeout=30, headers={
        "User-Agent": "Mozilla/5.0 (compatible; FounderKB/1.0)"
    })
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    if not text.strip():
        raise typer.BadParameter("No text content could be extracted from the URL.")
    return text


# ── App callback (global options) ─────────────────────────────────────────────

@app.callback()
def main(
    db_path: str = typer.Option("./chroma_db", "--db-path", help="Path to ChromaDB directory."),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON for machine parsing."),
):
    """Founder KB — AI-powered knowledge base for founders."""
    global _db_path, _json_output, META_FILE
    _db_path = db_path
    _json_output = json_output
    # Meta file lives next to the DB
    META_FILE = Path(db_path).parent / "knowledge_meta.json"


# ══════════════════════════════════════════════════════════════════════════════
# SEARCH & DISCOVERY
# ══════════════════════════════════════════════════════════════════════════════

@app.command()
def search(
    query: str = typer.Argument(..., help="Semantic search query."),
    top_k: int = typer.Option(5, "--top-k", "-k", help="Number of results."),
    source: Optional[str] = typer.Option(None, "--source", "-s", help="Filter by source."),
):
    """Semantic search through the knowledge base."""
    vs = _get_vs()
    results = vs.search(query, k=top_k, source_filter=source)

    if not results:
        _out([], "No results found.")
        return

    data = []
    parts = []
    for i, r in enumerate(results, 1):
        relevance = 1 - r["distance"]
        src = r["metadata"].get("source", "unknown")
        data.append({"relevance": round(relevance, 3), "source": src, "text": r["text"]})
        parts.append(f"[bold]Result {i}[/bold] (Relevance: {relevance:.0%}, Source: {src})\n{r['text']}")

    _out(data, "\n\n---\n\n".join(parts))


@app.command()
def keyword(
    term: str = typer.Argument(..., help="Keyword or phrase to search (exact substring)."),
    top_k: int = typer.Option(10, "--top-k", "-k", help="Max results."),
    source: Optional[str] = typer.Option(None, "--source", "-s", help="Filter by source."),
):
    """Search by exact keyword/substring match."""
    vs = _get_vs()
    results = vs.keyword_search(term, k=top_k, source_filter=source)

    if not results:
        _out([], f"No chunks contain '{term}'.")
        return

    data = []
    parts = []
    for i, r in enumerate(results, 1):
        src = r["metadata"].get("source", "?")
        idx = r["metadata"].get("chunk_index", "?")
        data.append({"source": src, "chunk_index": idx, "text": r["text"]})
        parts.append(f"[bold]Match {i}[/bold] (Source: {src}, Chunk {idx})\n{r['text']}")

    _out(data, f"Found {len(results)} chunk(s) containing '{term}':\n\n" + "\n\n---\n\n".join(parts))


@app.command("multi-search")
def multi_search(
    queries: list[str] = typer.Argument(..., help="Search queries."),
    top_k: int = typer.Option(10, "--top-k", "-k", help="Max results after dedup."),
    source: Optional[str] = typer.Option(None, "--source", "-s", help="Filter by source."),
):
    """Execute multiple search queries with deduplicated results."""
    vs = _get_vs()

    all_results = {}
    for q in queries:
        results = vs.search(q, k=top_k * 2, source_filter=source)
        for r in results:
            doc_id = r["metadata"].get("source", "?") + "_" + str(r["metadata"].get("chunk_index", "?"))
            if doc_id not in all_results:
                all_results[doc_id] = r

    sorted_results = sorted(all_results.values(), key=lambda x: x["distance"])[:top_k]

    if not sorted_results:
        _out([], "No results found.")
        return

    data = []
    parts = []
    for i, r in enumerate(sorted_results, 1):
        relevance = 1 - r["distance"]
        src = r["metadata"].get("source", "unknown")
        data.append({"relevance": round(relevance, 3), "source": src, "text": r["text"]})
        parts.append(f"[bold]Result {i}[/bold] (Relevance: {relevance:.0%}, Source: {src})\n{r['text']}")

    header = f"Searched {len(queries)} queries, found {len(sorted_results)} unique results:\n\n"
    _out(data, header + "\n\n---\n\n".join(parts))


@app.command("search-tag")
def search_tag(
    query: str = typer.Argument(..., help="Semantic search query."),
    tag: list[str] = typer.Option(..., "--tag", "-t", help="Tags to filter by (ALL must match)."),
    top_k: int = typer.Option(5, "--top-k", "-k", help="Max results."),
):
    """Semantic search filtered by source tags."""
    meta = _load_meta()
    tag_data = meta.get("tags", {})

    matching_sources = [src for src, src_tags in tag_data.items() if all(t in src_tags for t in tag)]

    if not matching_sources:
        _out([], f"No sources found with tags {tag}.")
        return

    vs = _get_vs()
    results = vs.search(query, k=top_k, source_filter=matching_sources)

    if not results:
        _out([], f"No results found in sources with tags {tag}.")
        return

    data = []
    parts = []
    for i, r in enumerate(results, 1):
        relevance = 1 - r["distance"]
        src = r["metadata"].get("source", "?")
        data.append({"relevance": round(relevance, 3), "source": src, "text": r["text"]})
        parts.append(f"[bold]Result {i}[/bold] (Relevance: {relevance:.0%}, Source: {src})\n{r['text']}")

    _out(data, f"Searched {len(matching_sources)} source(s) with tags {tag}:\n\n" + "\n\n---\n\n".join(parts))


@app.command()
def compare(
    topic: str = typer.Argument(..., help="Topic to compare across sources."),
    source1: str = typer.Option(..., "--source1", help="First source."),
    source2: str = typer.Option(..., "--source2", help="Second source."),
    top_k: int = typer.Option(3, "--top-k", "-k", help="Results per source."),
):
    """Compare what two sources say about a topic."""
    vs = _get_vs()
    results_a = vs.search(topic, k=top_k, source_filter=source1)
    results_b = vs.search(topic, k=top_k, source_filter=source2)

    data = {"topic": topic, "source_a": {"name": source1, "results": []}, "source_b": {"name": source2, "results": []}}
    parts = [f"[bold]Comparing:[/bold] \"{topic}\"\n"]

    parts.append(f"\n[bold underline]Source A: {source1}[/bold underline]")
    for i, r in enumerate(results_a, 1):
        rel = 1 - r["distance"]
        data["source_a"]["results"].append({"relevance": round(rel, 3), "text": r["text"]})
        parts.append(f"[bold]{i}.[/bold] (Relevance: {rel:.0%})\n{r['text']}")
    if not results_a:
        parts.append("[dim]No results found.[/dim]")

    parts.append(f"\n[bold underline]Source B: {source2}[/bold underline]")
    for i, r in enumerate(results_b, 1):
        rel = 1 - r["distance"]
        data["source_b"]["results"].append({"relevance": round(rel, 3), "text": r["text"]})
        parts.append(f"[bold]{i}.[/bold] (Relevance: {rel:.0%})\n{r['text']}")
    if not results_b:
        parts.append("[dim]No results found.[/dim]")

    _out(data, "\n\n".join(parts))


@app.command()
def duplicates(
    text: str = typer.Argument(..., help="Text to check for duplicates."),
    threshold: float = typer.Option(0.85, "--threshold", "-t", help="Similarity threshold (0-1)."),
    top_k: int = typer.Option(5, "--top-k", "-k", help="Max similar chunks."),
):
    """Check if similar content already exists in the knowledge base."""
    vs = _get_vs()
    results = vs.search(text, k=top_k)

    dupes = []
    for r in results:
        similarity = 1 - r["distance"]
        if similarity >= threshold:
            dupes.append({
                "similarity": round(similarity, 3),
                "source": r["metadata"].get("source", "unknown"),
                "chunk_index": r["metadata"].get("chunk_index", "?"),
                "preview": r["text"][:300],
            })

    if not dupes:
        _out([], f"No duplicates found above {threshold:.0%} similarity threshold.")
        return

    parts = []
    for d in dupes:
        parts.append(
            f"[bold]{d['similarity']:.0%} match[/bold] (Source: {d['source']}, Chunk {d['chunk_index']})\n  {d['preview']}..."
        )

    _out(dupes, f"Found {len(dupes)} similar chunk(s):\n\n" + "\n\n".join(parts))


@app.command()
def random(
    count: int = typer.Option(1, "--count", "-n", help="Number of random chunks."),
    source: Optional[str] = typer.Option(None, "--source", "-s", help="Filter by source."),
):
    """Get random chunks for discovery or quality spot-checking."""
    vs = _get_vs()
    chunks = vs.get_random_chunks(n=count, source=source)

    if not chunks:
        _out([], "No chunks found.")
        return

    data = []
    parts = []
    for i, c in enumerate(chunks, 1):
        src = c["metadata"].get("source", "?")
        idx = c["metadata"].get("chunk_index", "?")
        data.append({"source": src, "chunk_index": idx, "text": c["text"]})
        parts.append(f"[bold]Random {i}[/bold] (Source: {src}, Chunk {idx})\n{c['text']}")

    _out(data, "\n\n---\n\n".join(parts))


# ══════════════════════════════════════════════════════════════════════════════
# INGESTION
# ══════════════════════════════════════════════════════════════════════════════

@app.command()
def add(
    text: str = typer.Argument(..., help="Text content to add."),
    source: str = typer.Option(..., "--source", "-s", help="Source label."),
    semantic: bool = typer.Option(True, "--semantic/--no-semantic", help="Use semantic chunking."),
):
    """Add raw text to the knowledge base."""
    n = _ingest_text(text, source, use_semantic=semantic)
    stats = _get_vs().get_stats()

    data = {"source": source, "chunks_added": n, "total_chunks": stats["total_documents"]}
    _out(data, f"Added {n} chunks from source '{source}'. Total: {stats['total_documents']} chunks.")


@app.command()
def ingest(
    file_path: Path = typer.Argument(..., exists=True, help="Path to PDF, EPUB, or TXT file."),
    source: Optional[str] = typer.Option(None, "--source", "-s", help="Source label (default: filename)."),
    semantic: bool = typer.Option(True, "--semantic/--no-semantic", help="Use semantic chunking."),
):
    """Ingest a file (PDF, EPUB, TXT) into the knowledge base."""
    source_name = source or file_path.stem
    text = _extract_text_from_file(file_path)
    n = _ingest_text(text, source_name, use_semantic=semantic)
    stats = _get_vs().get_stats()

    data = {"file": str(file_path), "source": source_name, "chunks_added": n, "total_chunks": stats["total_documents"]}
    _out(data, f"Ingested '{file_path.name}' as '{source_name}'. Added {n} chunks. Total: {stats['total_documents']}.")


@app.command("ingest-url")
def ingest_url(
    url: str = typer.Argument(..., help="URL to fetch and ingest."),
    source: Optional[str] = typer.Option(None, "--source", "-s", help="Source label (default: domain/path)."),
    semantic: bool = typer.Option(True, "--semantic/--no-semantic", help="Use semantic chunking."),
):
    """Fetch a web page and ingest its text content."""
    text = _fetch_url_text(url)
    parsed = urlparse(url)
    source_name = source or f"{parsed.netloc}{parsed.path}".rstrip("/")
    n = _ingest_text(text, source_name, use_semantic=semantic)
    stats = _get_vs().get_stats()

    data = {"url": url, "source": source_name, "chars_extracted": len(text), "chunks_added": n, "total_chunks": stats["total_documents"]}
    _out(data, f"Ingested URL as '{source_name}'. Extracted ~{len(text)} chars, added {n} chunks. Total: {stats['total_documents']}.")


@app.command("ingest-dir")
def ingest_dir(
    directory: Path = typer.Argument(..., exists=True, file_okay=False, help="Directory to scan."),
    semantic: bool = typer.Option(True, "--semantic/--no-semantic", help="Use semantic chunking."),
    pattern: str = typer.Option("*", "--pattern", "-p", help="Glob pattern (e.g. '*.pdf')."),
):
    """Batch ingest all supported files from a directory."""
    supported_exts = {".pdf", ".epub", ".txt"}
    if pattern == "*":
        files = [f for f in directory.iterdir() if f.is_file() and f.suffix.lower() in supported_exts]
    else:
        files = [f for f in directory.glob(pattern) if f.is_file() and f.suffix.lower() in supported_exts]

    if not files:
        _out({"success": [], "errors": []}, f"No supported files found in {directory}")
        return

    results = {"success": [], "errors": []}
    for fp in sorted(files):
        try:
            text = _extract_text_from_file(fp)
            n = _ingest_text(text, fp.stem, use_semantic=semantic)
            results["success"].append({"file": fp.name, "chunks": n})
            console.print(f"  [green]✓[/green] {fp.name} ({n} chunks)") if not _json_output else None
        except Exception as e:
            results["errors"].append({"file": fp.name, "error": str(e)})
            console.print(f"  [red]✗[/red] {fp.name}: {e}") if not _json_output else None

    stats = _get_vs().get_stats()
    results["total_chunks"] = stats["total_documents"]

    if not _json_output:
        console.print(f"\nProcessed {len(files)} files: {len(results['success'])} ok, {len(results['errors'])} errors.")
        console.print(f"Total: {stats['total_documents']} chunks.")
    else:
        typer.echo(json.dumps(results, ensure_ascii=False, indent=2))


@app.command()
def replace(
    source: str = typer.Argument(..., help="Source name to replace."),
    content: str = typer.Argument(..., help="File path, URL, or raw text."),
    content_type: str = typer.Option("file", "--type", "-t", help="Content type: file, url, or text."),
    semantic: bool = typer.Option(True, "--semantic/--no-semantic", help="Use semantic chunking."),
):
    """Atomically replace a source (delete old + ingest new)."""
    vs = _get_vs()
    deleted = vs.delete_by_source(source)

    if content_type == "file":
        fp = Path(content)
        if not fp.exists():
            raise typer.BadParameter(f"File not found: {content}")
        text = _extract_text_from_file(fp)
    elif content_type == "url":
        text = _fetch_url_text(content)
    elif content_type == "text":
        text = content
    else:
        raise typer.BadParameter(f"Unknown content type: {content_type}. Use: file, url, text.")

    if not text.strip():
        raise typer.BadParameter("No content to ingest.")

    n = _ingest_text(text, source, use_semantic=semantic)
    stats = vs.get_stats()

    data = {"source": source, "deleted": deleted, "added": n, "total_chunks": stats["total_documents"]}
    _out(data, f"Replaced '{source}': deleted {deleted} old, added {n} new chunks. Total: {stats['total_documents']}.")


# ══════════════════════════════════════════════════════════════════════════════
# BROWSE & EXPORT
# ══════════════════════════════════════════════════════════════════════════════

@app.command()
def chunks(
    source: str = typer.Argument(..., help="Source name to browse."),
    page: int = typer.Option(1, "--page", "-p", help="Page number (1-based)."),
    page_size: int = typer.Option(10, "--page-size", "-n", help="Chunks per page."),
):
    """Browse stored chunks for a source with pagination."""
    vs = _get_vs()
    offset = (page - 1) * page_size
    result = vs.get_source_chunks(source, offset=offset, limit=page_size)

    if not result["chunks"]:
        _out(result, f"No chunks found for source '{source}'.")
        return

    data = result
    parts = []
    for c in result["chunks"]:
        idx = c["metadata"].get("chunk_index", "?")
        parts.append(f"[bold]Chunk {idx}[/bold]\n{c['text']}")

    total_pages = (result["total"] + page_size - 1) // page_size
    footer = f"\n[dim]Page {page}/{total_pages} — showing {len(result['chunks'])} of {result['total']} chunks[/dim]"
    _out(data, "\n\n---\n\n".join(parts) + footer)


@app.command()
def neighbors(
    source: str = typer.Argument(..., help="Source name."),
    chunk_index: int = typer.Argument(..., help="Target chunk index."),
    context: int = typer.Option(2, "--context", "-c", help="Neighboring chunks before/after."),
):
    """Get a chunk with its surrounding context."""
    vs = _get_vs()
    result = vs.get_neighboring_chunks(source, chunk_index, context=context)

    if "error" in result:
        _out(result, f"[red]{result['error']}[/red]")
        raise typer.Exit(1)

    parts = []
    for c in result["chunks"]:
        marker = " [bold yellow]← TARGET[/bold yellow]" if c["is_target"] else ""
        parts.append(f"[bold]Chunk {c['index']}{marker}[/bold]\n{c['text']}")

    _out(result, "\n\n".join(parts))


@app.command()
def export(
    source: str = typer.Argument(..., help="Source name to export."),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Write to file instead of stdout."),
):
    """Export the full reconstructed text of a source."""
    vs = _get_vs()
    text = vs.export_source(source)

    if not text:
        _out({"source": source, "text": ""}, f"No content found for source '{source}'.")
        return

    if output:
        output.write_text(text, encoding="utf-8")
        _out({"source": source, "chars": len(text), "output": str(output)}, f"Exported '{source}' ({len(text)} chars) → {output}")
    else:
        data = {"source": source, "chars": len(text), "text": text}
        _out(data, text)


@app.command()
def overview():
    """High-level overview of the entire knowledge base."""
    vs = _get_vs()
    ov = vs.get_overview()

    if not ov:
        _out([], "Knowledge base is empty.")
        return

    total_chunks = sum(s["chunks"] for s in ov)

    if _json_output:
        typer.echo(json.dumps(ov, ensure_ascii=False, indent=2))
        return

    console.print(f"[bold]Knowledge Base: {len(ov)} sources, {total_chunks} chunks[/bold]\n")
    for src in ov:
        console.print(f"[bold underline]{src['source']}[/bold underline] ({src['chunks']} chunks)")
        for s in src["samples"]:
            preview = s["preview"][:120].replace("\n", " ")
            console.print(f"  Chunk {s['index']}: [dim]{preview}...[/dim]")
        console.print()


# ══════════════════════════════════════════════════════════════════════════════
# ORGANIZATION
# ══════════════════════════════════════════════════════════════════════════════

@app.command()
def tag(
    source: str = typer.Argument(..., help="Source name to tag."),
    add: Optional[list[str]] = typer.Option(None, "--add", "-a", help="Tags to add."),
    remove: Optional[list[str]] = typer.Option(None, "--remove", "-r", help="Tags to remove."),
    set_tags: Optional[list[str]] = typer.Option(None, "--set", help="Replace all tags."),
):
    """Manage tags on a source."""
    meta = _load_meta()
    current_tags = meta.get("tags", {}).get(source, [])

    if set_tags is not None:
        new_tags = list(set(set_tags))
    elif add or remove:
        new_tags = list(set(current_tags + (add or [])))
        if remove:
            new_tags = [t for t in new_tags if t not in remove]
    else:
        # View mode
        _out({"source": source, "tags": current_tags}, f"Tags for '{source}': {current_tags}")
        return

    meta.setdefault("tags", {})[source] = new_tags
    _save_meta(meta)

    _out({"source": source, "tags": new_tags}, f"Tags for '{source}': {new_tags}")


@app.command()
def annotate(
    source: str = typer.Argument(..., help="Source name."),
    chunk_index: int = typer.Argument(..., help="Chunk index to annotate."),
    note: Optional[str] = typer.Argument(None, help="Annotation text. Omit to view existing."),
):
    """Add a note to a specific chunk, or view existing annotations."""
    meta = _load_meta()
    key = f"{source}_{chunk_index}"
    annotations = meta.get("annotations", {})

    if note is None:
        existing = annotations.get(key, [])
        if not existing:
            _out([], f"No annotations for {source} chunk {chunk_index}.")
        else:
            parts = [f"[bold]Annotations for {source} chunk {chunk_index}:[/bold]"]
            for a in existing:
                parts.append(f"  [{a.get('created', '?')}] {a.get('note', '')}")
            _out(existing, "\n".join(parts))
    else:
        annotations.setdefault(key, []).append({
            "note": note,
            "created": datetime.now(timezone.utc).isoformat(),
        })
        meta["annotations"] = annotations
        _save_meta(meta)
        _out(
            {"source": source, "chunk_index": chunk_index, "total_annotations": len(annotations[key])},
            f"Annotation added to {source} chunk {chunk_index}. Total: {len(annotations[key])}",
        )


@app.command()
def sources():
    """List all sources in the knowledge base."""
    vs = _get_vs()
    src_list = vs.list_sources()

    if not src_list:
        _out([], "Knowledge base is empty — no sources found.")
        return

    if _json_output:
        typer.echo(json.dumps(src_list, ensure_ascii=False, indent=2))
        return

    table = Table(title="Sources")
    table.add_column("Source", style="bold")
    table.add_column("Chunks", justify="right")
    total = 0
    for s in src_list:
        table.add_row(s["source"], str(s["chunks"]))
        total += s["chunks"]
    table.add_row("[bold]TOTAL[/bold]", f"[bold]{total}[/bold]")
    console.print(table)


@app.command()
def delete(
    source: str = typer.Argument(..., help="Source name to delete."),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt."),
):
    """Delete all chunks for a source."""
    if not confirm:
        typer.confirm(f"Delete all chunks for source '{source}'?", abort=True)

    vs = _get_vs()
    deleted = vs.delete_by_source(source)
    stats = vs.get_stats()

    data = {"source": source, "deleted": deleted, "total_chunks": stats["total_documents"]}
    _out(data, f"Deleted {deleted} chunks from '{source}'. Total remaining: {stats['total_documents']}.")


# ══════════════════════════════════════════════════════════════════════════════
# ANALYTICS
# ══════════════════════════════════════════════════════════════════════════════

@app.command()
def stats():
    """Show knowledge base statistics."""
    vs = _get_vs()
    s = vs.get_stats()
    src_list = vs.list_sources()

    data = {"total_chunks": s["total_documents"], "total_sources": len(src_list), "sources": src_list}

    if _json_output:
        typer.echo(json.dumps(data, ensure_ascii=False, indent=2))
        return

    console.print(f"[bold]Knowledge Base Statistics[/bold]")
    console.print(f"  Total chunks:  {s['total_documents']}")
    console.print(f"  Total sources: {len(src_list)}")
    if src_list:
        console.print()
        for src in src_list:
            console.print(f"  {src['source']}: {src['chunks']} chunks")


@app.command()
def quality(
    source: Optional[str] = typer.Option(None, "--source", "-s", help="Analyze specific source. Omit for whole DB."),
):
    """Chunk quality report — find broken or garbled chunks."""
    vs = _get_vs()
    report = vs.get_quality_report(source=source)

    if "error" in report:
        _out(report, report["error"])
        return

    if _json_output:
        typer.echo(json.dumps(report, ensure_ascii=False, indent=2))
        return

    scope = f"source '{source}'" if source else "entire knowledge base"
    console.print(f"[bold]Chunk Quality Report ({scope})[/bold]\n")
    console.print(f"  Total chunks:           {report['total_chunks']}")
    console.print(f"  Avg length:             {report['avg_length']:.0f} chars")
    console.print(f"  Min length:             {report['min_length']} chars")
    console.print(f"  Max length:             {report['max_length']} chars")
    console.print(f"  Short chunks (<50):     {report['short_chunks_count']}")
    console.print(f"  Long chunks (>2000):    {report['long_chunks_count']}")
    console.print(f"  Whitespace-heavy (>50%): {report['whitespace_heavy_count']}")

    if report["short_chunks"]:
        console.print("\n[yellow]Flagged short chunks:[/yellow]")
        for c in report["short_chunks"]:
            console.print(f"  {c['source']} chunk {c['chunk_index']}: {c['length']} chars")
    if report["long_chunks"]:
        console.print("\n[yellow]Flagged long chunks:[/yellow]")
        for c in report["long_chunks"]:
            console.print(f"  {c['source']} chunk {c['chunk_index']}: {c['length']} chars")
    if report["whitespace_heavy"]:
        console.print("\n[yellow]Flagged whitespace-heavy chunks:[/yellow]")
        for c in report["whitespace_heavy"]:
            console.print(f"  {c['source']} chunk {c['chunk_index']}: {c['length']} chars")


@app.command()
def reindex(
    source: str = typer.Argument(..., help="Source to re-chunk."),
    semantic: bool = typer.Option(True, "--semantic/--no-semantic", help="Use semantic chunking."),
    chunk_size: int = typer.Option(1000, "--chunk-size", help="Chunk size for character-based."),
    chunk_overlap: int = typer.Option(200, "--chunk-overlap", help="Overlap between chunks."),
):
    """Re-chunk a source with different settings."""
    vs = _get_vs()
    text = vs.export_source(source)
    if not text:
        _out({"error": f"No content for '{source}'"}, f"[red]No content found for source '{source}'.[/red]")
        raise typer.Exit(1)

    deleted = vs.delete_by_source(source)

    from src.chunker import create_chunks_with_metadata
    chunks = create_chunks_with_metadata(
        text=text, source=source, use_semantic=semantic,
        chunk_size=chunk_size, chunk_overlap=chunk_overlap,
    )
    texts = [c["text"] for c in chunks]
    metadatas = [c["metadata"] for c in chunks]
    ids = [f"{source}_{c['metadata']['chunk_index']}" for c in chunks]
    vs.add_documents(texts=texts, metadatas=metadatas, ids=ids)

    data = {"source": source, "deleted": deleted, "created": len(chunks), "semantic": semantic, "chunk_size": chunk_size, "chunk_overlap": chunk_overlap}
    _out(data, f"Reindexed '{source}': {deleted} old → {len(chunks)} new chunks. (semantic={semantic}, size={chunk_size}, overlap={chunk_overlap})")


@app.command()
def clusters(
    n_clusters: int = typer.Option(5, "--n-clusters", "-n", help="Number of clusters."),
    source: Optional[str] = typer.Option(None, "--source", "-s", help="Cluster only this source."),
):
    """Semantic clustering of chunks using KMeans."""
    vs = _get_vs()
    result = vs.get_semantic_clusters(n_clusters=n_clusters, source=source)

    if "error" in result:
        _out(result, f"[red]{result['error']}[/red]")
        raise typer.Exit(1)

    if _json_output:
        typer.echo(json.dumps(result, ensure_ascii=False, indent=2))
        return

    console.print(f"[bold]Semantic Clusters ({result['total_chunks']} chunks → {result['n_clusters']} clusters)[/bold]\n")
    for name, cluster in result["clusters"].items():
        rep = cluster["representative"]
        console.print(f"[bold underline]{name}[/bold underline] ({cluster['size']} chunks)")
        console.print(f"  Representative: {rep['source']} chunk {rep['chunk_index']}")
        console.print(f"  [dim]{rep['text'][:200]}...[/dim]")
        if cluster["members"]:
            console.print("  Members:")
            for m in cluster["members"]:
                console.print(f"    - {m['source']} chunk {m['chunk_index']}: [dim]{m['preview'][:100]}...[/dim]")
        console.print()


if __name__ == "__main__":
    app()
