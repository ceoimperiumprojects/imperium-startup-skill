from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings


# Cache embeddings model for semantic chunking
_semantic_embeddings = None


def get_semantic_embeddings():
    """Lazy load and cache embeddings model."""
    global _semantic_embeddings
    if _semantic_embeddings is None:
        _semantic_embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    return _semantic_embeddings


def create_chunks_semantic(text: str) -> list[str]:
    """Dijeli tekst semanticki - koristi embeddings za prirodne granice."""
    embeddings = get_semantic_embeddings()
    splitter = SemanticChunker(
        embeddings=embeddings,
        breakpoint_threshold_type="percentile"
    )
    return splitter.split_text(text)


def create_chunks(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> list[str]:
    """Dijeli tekst na chunk-ove."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
    )
    chunks = splitter.split_text(text)
    return chunks


def create_chunks_with_metadata(
    text: str,
    source: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
    use_semantic: bool = False
) -> list[dict]:
    """Kreira chunk-ove sa metadata.

    Args:
        text: Tekst za chunking
        source: Naziv izvora (npr. ime fajla)
        chunk_size: Velicina chunk-a (ignorise se ako use_semantic=True)
        chunk_overlap: Overlap chunk-ova (ignorise se ako use_semantic=True)
        use_semantic: Koristi semantic chunking umjesto character-based
    """
    if use_semantic:
        chunks = create_chunks_semantic(text)
    else:
        chunks = create_chunks(text, chunk_size, chunk_overlap)

    return [
        {
            "text": chunk,
            "metadata": {
                "source": source,
                "chunk_index": i,
                "chunking_method": "semantic" if use_semantic else "character"
            }
        }
        for i, chunk in enumerate(chunks)
    ]


if __name__ == "__main__":
    sample_text = "Ovo je test tekst. " * 100
    chunks = create_chunks(sample_text)
    print(f"Created {len(chunks)} chunks (character-based)")

    # Test semantic chunking
    print("Testing semantic chunking...")
    semantic_chunks = create_chunks_semantic(sample_text)
    print(f"Created {len(semantic_chunks)} chunks (semantic)")
