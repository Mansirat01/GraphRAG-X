from fastapi import FastAPI, UploadFile, File
import shutil
import os

from services.document_loader import load_document
from services.text_chunker import chunk_text

app = FastAPI()

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = load_document(file_path)

    # Chunk text
    chunks = chunk_text(text)

    return {
        "filename": file.filename,
        "total_characters": len(text),
        "total_chunks": len(chunks)
    }