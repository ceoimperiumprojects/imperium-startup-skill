from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    _instance = None
    _model = None

    def __new__(cls, model_name: str = "all-MiniLM-L6-v2"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._model = SentenceTransformer(model_name)
        return cls._instance

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        pass

    def embed_text(self, text: str) -> list[float]:
        """Embed-uje jedan tekst."""
        return self._model.encode(text).tolist()

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        """Embed-uje listu tekstova."""
        return self._model.encode(texts).tolist()


if __name__ == "__main__":
    model = EmbeddingModel()
    embedding = model.embed_text("Test startup knowledge")
    print(f"Embedding dimension: {len(embedding)}")
