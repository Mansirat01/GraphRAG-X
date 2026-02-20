
GraphRAG-X: Hybrid Knowledge Graph Enhanced Retrieval-Augmented Generation System

GraphRAG-X is a full-stack AI system that enhances traditional Retrieval-Augmented Generation (RAG) by integrating Knowledge Graph reasoning with Vector-based semantic search to enable explainable, multi-hop, and context-aware question answering over unstructured documents.

Conventional RAG systems rely primarily on semantic similarity search over vector embeddings. While effective for surface-level retrieval, this approach often struggles with:
Multi-hop reasoning
Relationship understanding between entities
Response explainability
Hallucination control
GraphRAG-X addresses these limitations by combining structured graph traversal with vector retrieval to create a hybrid reasoning pipeline.

Core Features:
Document upload (PDF / TXT)
Entity and relationship extraction
Knowledge Graph construction using Neo4j
Vector embedding and semantic retrieval using FAISS
Hybrid retrieval (Graph + Vector)
Multi-hop query handling
Evaluation metrics for retrieval quality
REST API backend
Interactive frontend interface

System Architecture:
User (React Frontend)
→ FastAPI Backend
→ Hybrid Retrieval Engine
  • Vector Search (FAISS)
  • Graph Traversal (Neo4j)
→ LLM
→ Grounded Response with Reasoning Context

Technology Stack:

Frontend:
React (Vite)
JavaScript (ES6+)
Axios
D3.js (Graph Visualization)

Backend:
Python 3.11+
FastAPI
Pydantic
Uvicorn

AI & Retrieval Layer:
LangChain
LLMGraphTransformer
FAISS (Vector Store)
OpenAI / HuggingFace Embeddings

Database:
Neo4j (Graph Database)
Cypher Query Language

DevOps:
Docker
Docker Compose

Workflow:

Step 1: Document Ingestion
Upload document (PDF / TXT)
Perform text extraction
Split content into manageable chunks

Step 2: Knowledge Graph Extraction
LLM extracts entities and relationships from text
Convert extracted information into triples
Store triples as nodes and edges in Neo4j
Example relationship:
(LangChain) — INTEGRATES_WITH — (Neo4j)

Step 3: Vector Indexing
Convert text chunks into embeddings
Store embeddings in FAISS
Enable semantic similarity search

Step 4: Hybrid Query Processing
When a user submits a query:
Retrieve top-k relevant chunks using vector search
Extract key entities from retrieved context
Perform graph traversal (1–2 hops) in Neo4j
Merge structured graph context with semantic context
Generate grounded response using LLM



