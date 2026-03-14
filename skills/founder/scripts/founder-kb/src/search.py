from .vector_store import VectorStore


def search_knowledge(query: str, k: int = 5, persist_dir: str = "./chroma_db") -> list[dict]:
    """Helper funkcija za pretragu."""
    store = VectorStore(persist_directory=persist_dir)
    results = store.search(query, k=k)

    formatted = []
    for r in results:
        formatted.append({
            "text": r["text"],
            "source": r["metadata"].get("source", "unknown"),
            "relevance_score": 1 - r["distance"]
        })

    return formatted


if __name__ == "__main__":
    results = search_knowledge("How to validate a startup idea?")
    for r in results:
        print(f"[{r['relevance_score']:.2f}] {r['text'][:100]}...")
