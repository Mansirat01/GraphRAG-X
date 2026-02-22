from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from services.document_loader import load_document
from services.text_chunker import chunk_text
from services.embedding_model import EmbeddingModel
from services.vector_store import VectorStore
from services.graph_store import GraphStore
from dotenv import load_dotenv

load_dotenv()

graph_store = GraphStore()

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
print("URI:", os.getenv("NEO4J_URI"))
embedding_model = EmbeddingModel()
vector_store = None


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = load_document(file_path)

    # Chunk text
    chunks = chunk_text(text)
    # Create document node in Neo4j
    graph_store.store_document_with_chunks(file.filename, chunks)
    # Generate embeddings
    embeddings = embedding_model.encode(chunks)

    # Initialize FAISS once
    global vector_store
    if vector_store is None:
        vector_store = VectorStore(dimension=len(embeddings[0]))

    # Store embeddings
    vector_store.add_embeddings(embeddings, chunks)

    return {
        "filename": file.filename,
        "total_characters": len(text),
        "total_chunks": len(chunks),
        "status": "Indexed successfully"
    }


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
async def query_document(request: QueryRequest):
    global vector_store

    if vector_store is None:
        return {"error": "No documents uploaded yet"}

    query_embedding = embedding_model.encode([request.query])[0]
    results = vector_store.search(query_embedding)

    return {
        "query": request.query,
        "retrieved_chunks": results
    }