import chromadb
from chromadb.config import Settings
from .embeddings import EmbeddingModel
import uuid
import random


class VectorStore:
    def __init__(self, persist_directory: str = "./chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="startup_knowledge",
            metadata={"hnsw:space": "cosine"}
        )
        self.embedding_model = EmbeddingModel()

    def add_documents(
        self,
        texts: list[str],
        metadatas: list[dict] = None,
        ids: list[str] = None
    ):
        """Dodaje dokumente u bazu."""
        embeddings = self.embedding_model.embed_texts(texts)

        if ids is None:
            ids = [str(uuid.uuid4()) for _ in range(len(texts))]

        if metadatas is None:
            metadatas = [{}] * len(texts)

        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

        return len(texts)

    def search(self, query: str, k: int = 5, source_filter=None) -> list[dict]:
        """Semanticka pretraga. source_filter can be str or list[str]."""
        query_embedding = self.embedding_model.embed_text(query)
        query_kwargs = {
            "query_embeddings": [query_embedding],
            "n_results": k,
        }
        if source_filter:
            if isinstance(source_filter, list):
                query_kwargs["where"] = {"source": {"$in": source_filter}}
            else:
                query_kwargs["where"] = {"source": source_filter}

        try:
            results = self.collection.query(**query_kwargs)
        except Exception:
            # Refresh collection reference if stale
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            results = self.collection.query(**query_kwargs)

        if not results["documents"][0]:
            return []

        return [
            {
                "text": doc,
                "metadata": meta,
                "distance": dist
            }
            for doc, meta, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0]
            )
        ]

    def get_stats(self) -> dict:
        """Vraca statistiku baze."""
        try:
            count = self.collection.count()
        except Exception:
            # Refresh collection reference if stale
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            count = self.collection.count()
        return {
            "total_documents": count
        }

    def list_sources(self) -> list[dict]:
        """Vraca listu svih unikatnih source-ova sa brojem chunk-ova."""
        try:
            all_meta = self.collection.get(include=["metadatas"])
        except Exception:
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            all_meta = self.collection.get(include=["metadatas"])

        counts: dict[str, int] = {}
        for meta in all_meta["metadatas"]:
            src = meta.get("source", "unknown")
            counts[src] = counts.get(src, 0) + 1

        return [{"source": src, "chunks": cnt} for src, cnt in sorted(counts.items())]

    def get_source_chunks(self, source: str, offset: int = 0, limit: int = 10) -> dict:
        """Vraca chunk-ove za dati source sa paginacijom."""
        try:
            result = self.collection.get(
                where={"source": source},
                include=["documents", "metadatas"]
            )
        except Exception:
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            result = self.collection.get(
                where={"source": source},
                include=["documents", "metadatas"]
            )

        total = len(result["ids"])
        # Sort by chunk_index if available
        items = list(zip(result["ids"], result["documents"], result["metadatas"]))
        items.sort(key=lambda x: x[2].get("chunk_index", 0))

        page = items[offset:offset + limit]
        return {
            "total": total,
            "offset": offset,
            "limit": limit,
            "chunks": [
                {"id": id_, "text": doc, "metadata": meta}
                for id_, doc, meta in page
            ]
        }

    def get_overview(self) -> list[dict]:
        """Vraca pregled baze — za svaki source: broj chunk-ova + sample chunk-ovi."""
        try:
            all_data = self.collection.get(include=["documents", "metadatas"])
        except Exception:
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            all_data = self.collection.get(include=["documents", "metadatas"])

        # Group by source
        by_source: dict[str, list[tuple[str, dict]]] = {}
        for doc, meta in zip(all_data["documents"], all_data["metadatas"]):
            src = meta.get("source", "unknown")
            by_source.setdefault(src, []).append((doc, meta))

        overview = []
        for src in sorted(by_source):
            chunks = by_source[src]
            chunks.sort(key=lambda x: x[1].get("chunk_index", 0))
            total = len(chunks)

            # Pick representative samples: first, middle, last
            samples = []
            if total >= 1:
                samples.append({"index": 0, "preview": chunks[0][0][:200]})
            if total >= 3:
                mid = total // 2
                samples.append({"index": mid, "preview": chunks[mid][0][:200]})
            if total >= 2:
                samples.append({"index": total - 1, "preview": chunks[-1][0][:200]})

            overview.append({
                "source": src,
                "chunks": total,
                "samples": samples,
            })

        return overview

    def get_neighboring_chunks(self, source: str, chunk_index: int, context: int = 2) -> dict:
        """Vraca chunk sa N susednih chunk-ova pre i posle."""
        try:
            result = self.collection.get(
                where={"source": source},
                include=["documents", "metadatas"]
            )
        except Exception:
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            result = self.collection.get(
                where={"source": source},
                include=["documents", "metadatas"]
            )

        # Sort by chunk_index
        items = list(zip(result["ids"], result["documents"], result["metadatas"]))
        items.sort(key=lambda x: x[2].get("chunk_index", 0))

        # Find the target chunk
        target_idx = None
        for i, (_, _, meta) in enumerate(items):
            if meta.get("chunk_index") == chunk_index:
                target_idx = i
                break

        if target_idx is None:
            return {"error": f"Chunk with index {chunk_index} not found in source '{source}'"}

        # Get neighbors
        start = max(0, target_idx - context)
        end = min(len(items), target_idx + context + 1)
        neighbors = items[start:end]

        return {
            "source": source,
            "target_index": chunk_index,
            "chunks": [
                {
                    "id": id_,
                    "text": doc,
                    "index": meta.get("chunk_index", "?"),
                    "is_target": meta.get("chunk_index") == chunk_index
                }
                for id_, doc, meta in neighbors
            ]
        }

    def delete_by_source(self, source: str) -> int:
        """Brise sve chunk-ove za dati source."""
        try:
            existing = self.collection.get(
                where={"source": source},
                include=[]
            )
        except Exception:
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            existing = self.collection.get(
                where={"source": source},
                include=[]
            )

        ids = existing["ids"]
        if ids:
            self.collection.delete(ids=ids)
        return len(ids)

    def delete_all(self):
        """Brise sve dokumente."""
        self.client.delete_collection("startup_knowledge")
        self.collection = self.client.get_or_create_collection(
            name="startup_knowledge",
            metadata={"hnsw:space": "cosine"}
        )

    def keyword_search(self, keyword: str, k: int = 10, source_filter: str = None) -> list[dict]:
        """Search chunks by keyword (exact substring match)."""
        try:
            get_kwargs = {
                "where_document": {"$contains": keyword},
                "include": ["documents", "metadatas"],
            }
            if source_filter:
                get_kwargs["where"] = {"source": source_filter}
            result = self.collection.get(**get_kwargs)
        except Exception:
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            get_kwargs = {
                "where_document": {"$contains": keyword},
                "include": ["documents", "metadatas"],
            }
            if source_filter:
                get_kwargs["where"] = {"source": source_filter}
            result = self.collection.get(**get_kwargs)

        items = list(zip(result["ids"], result["documents"], result["metadatas"]))
        items.sort(key=lambda x: (x[2].get("source", ""), x[2].get("chunk_index", 0)))
        items = items[:k]

        return [
            {"id": id_, "text": doc, "metadata": meta}
            for id_, doc, meta in items
        ]

    def export_source(self, source: str) -> str:
        """Reconstruct full text for a source by joining chunks in order."""
        try:
            result = self.collection.get(
                where={"source": source},
                include=["documents", "metadatas"]
            )
        except Exception:
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            result = self.collection.get(
                where={"source": source},
                include=["documents", "metadatas"]
            )

        if not result["ids"]:
            return ""

        items = list(zip(result["documents"], result["metadatas"]))
        items.sort(key=lambda x: x[1].get("chunk_index", 0))
        return "\n\n".join(doc for doc, _ in items)

    def get_random_chunks(self, n: int = 1, source: str = None) -> list[dict]:
        """Return n random chunks, optionally filtered by source."""
        try:
            get_kwargs = {"include": ["documents", "metadatas"]}
            if source:
                get_kwargs["where"] = {"source": source}
            result = self.collection.get(**get_kwargs)
        except Exception:
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            get_kwargs = {"include": ["documents", "metadatas"]}
            if source:
                get_kwargs["where"] = {"source": source}
            result = self.collection.get(**get_kwargs)

        if not result["ids"]:
            return []

        items = list(zip(result["ids"], result["documents"], result["metadatas"]))
        n = min(n, len(items))
        sampled = random.sample(items, n)

        return [
            {"id": id_, "text": doc, "metadata": meta}
            for id_, doc, meta in sampled
        ]

    def get_quality_report(self, source: str = None) -> dict:
        """Analyze chunk quality: lengths, whitespace, flagged chunks."""
        try:
            get_kwargs = {"include": ["documents", "metadatas"]}
            if source:
                get_kwargs["where"] = {"source": source}
            result = self.collection.get(**get_kwargs)
        except Exception:
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            get_kwargs = {"include": ["documents", "metadatas"]}
            if source:
                get_kwargs["where"] = {"source": source}
            result = self.collection.get(**get_kwargs)

        if not result["ids"]:
            return {"total_chunks": 0, "error": "No chunks found."}

        docs = result["documents"]
        metas = result["metadatas"]
        lengths = [len(d) for d in docs]

        short_chunks = []
        long_chunks = []
        whitespace_heavy = []
        for i, (doc, meta) in enumerate(zip(docs, metas)):
            info = {"source": meta.get("source", "?"), "chunk_index": meta.get("chunk_index", i), "length": len(doc)}
            if len(doc) < 50:
                short_chunks.append(info)
            if len(doc) > 2000:
                long_chunks.append(info)
            if len(doc) > 0 and sum(1 for c in doc if c.isspace()) / len(doc) > 0.5:
                whitespace_heavy.append(info)

        return {
            "total_chunks": len(docs),
            "avg_length": sum(lengths) / len(lengths),
            "min_length": min(lengths),
            "max_length": max(lengths),
            "short_chunks_count": len(short_chunks),
            "short_chunks": short_chunks[:10],
            "long_chunks_count": len(long_chunks),
            "long_chunks": long_chunks[:10],
            "whitespace_heavy_count": len(whitespace_heavy),
            "whitespace_heavy": whitespace_heavy[:10],
        }

    def get_semantic_clusters(self, n_clusters: int = 5, source: str = None) -> dict:
        """Cluster chunks by embedding similarity using KMeans."""
        try:
            from sklearn.cluster import KMeans
            import numpy as np
        except ImportError:
            return {"error": "scikit-learn and numpy are required for clustering. Install with: pip install scikit-learn numpy"}

        try:
            get_kwargs = {"include": ["documents", "metadatas", "embeddings"]}
            if source:
                get_kwargs["where"] = {"source": source}
            result = self.collection.get(**get_kwargs)
        except Exception:
            self.collection = self.client.get_or_create_collection(
                name="startup_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            get_kwargs = {"include": ["documents", "metadatas", "embeddings"]}
            if source:
                get_kwargs["where"] = {"source": source}
            result = self.collection.get(**get_kwargs)

        if not result["ids"] or len(result["ids"]) < n_clusters:
            return {"error": f"Need at least {n_clusters} chunks for clustering, found {len(result['ids'])}."}

        embeddings = np.array(result["embeddings"])
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = kmeans.fit_predict(embeddings)

        clusters = {}
        for i in range(n_clusters):
            mask = labels == i
            indices = np.where(mask)[0]

            # Find chunk closest to centroid (representative)
            cluster_embeddings = embeddings[mask]
            centroid = kmeans.cluster_centers_[i]
            distances = np.linalg.norm(cluster_embeddings - centroid, axis=1)
            rep_idx = indices[np.argmin(distances)]

            member_samples = []
            for idx in indices[:5]:
                member_samples.append({
                    "source": result["metadatas"][idx].get("source", "?"),
                    "chunk_index": result["metadatas"][idx].get("chunk_index", "?"),
                    "preview": result["documents"][idx][:150],
                })

            clusters[f"cluster_{i}"] = {
                "size": int(mask.sum()),
                "representative": {
                    "source": result["metadatas"][rep_idx].get("source", "?"),
                    "chunk_index": result["metadatas"][rep_idx].get("chunk_index", "?"),
                    "text": result["documents"][rep_idx][:300],
                },
                "members": member_samples,
            }

        return {"n_clusters": n_clusters, "total_chunks": len(result["ids"]), "clusters": clusters}
