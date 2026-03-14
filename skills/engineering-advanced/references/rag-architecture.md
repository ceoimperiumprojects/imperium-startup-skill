# RAG Architecture

## Pipeline Overview
```
Documents → Ingestion → Chunking → Embedding → Vector Store
                                                     ↓
User Query → Query Processing → Retrieval → Re-ranking → Generation → Response
```

## Chunking Strategies

| Strategy | Chunk Size | Best For |
|----------|-----------|----------|
| Fixed-size | 256-512 tokens | Simple docs, uniform content |
| Semantic | Variable | Mixed content, complex documents |
| Recursive | Parent + child | Hierarchical content (docs, codebases) |
| Sentence-level | 1-3 sentences | FAQ, Q&A, short answers |
| Document-level | Full document | Short docs, complete context needed |

### Overlap
- 10-20% overlap between chunks prevents information loss at boundaries
- Too much overlap = redundant storage and retrieval

## Retrieval Optimization

### Hybrid Search
Combine vector similarity + keyword search (BM25):
- Vector: Good at semantic similarity ("dog" matches "puppy")
- Keyword: Good at exact matches (names, codes, specific terms)
- Reciprocal Rank Fusion to merge results

### Re-ranking
After initial retrieval (top 20-50), re-rank to top 5-10:
- Cross-encoder models (slower but more accurate)
- Cohere Reranker, BGE Reranker, or ColBERT

### Query Enhancement
- Query expansion: Generate 3-5 query variations
- HyDE: Generate hypothetical answer, use as search query
- Step-back prompting: Ask broader question first, then specific

## Vector Database Selection

| Database | Hosted | Self-hosted | Best For |
|----------|--------|------------|----------|
| pgvector | Supabase, Neon | Yes | Already using PostgreSQL |
| Pinecone | Yes | No | Managed serverless, easy setup |
| Weaviate | Yes | Yes | Hybrid search, multi-modal |
| Qdrant | Yes | Yes | High performance, rich filtering |
| ChromaDB | No | Yes | Prototyping, local development |

## Quality Metrics

| Metric | What It Measures | How to Measure |
|--------|-----------------|----------------|
| Retrieval Precision | % retrieved chunks that are relevant | Human evaluation |
| Retrieval Recall | % relevant chunks that are retrieved | Known-answer tests |
| Faithfulness | Answer matches retrieved context | LLM-as-judge |
| Answer Relevancy | Answer addresses the question | LLM-as-judge |
| Context Utilization | How well context is used | Compare with/without RAG |

## Common Issues & Fixes

| Issue | Symptom | Fix |
|-------|---------|-----|
| Chunks too small | Answers lack context | Increase chunk size, add parent retrieval |
| Chunks too large | Irrelevant content retrieved | Decrease chunk size, improve chunking strategy |
| Poor embedding | Wrong documents retrieved | Try different embedding model, fine-tune |
| Missing context | Answer is incomplete | Increase top-k, add metadata filtering |
| Hallucination | Answer contradicts sources | Add citation requirements, verify step |
