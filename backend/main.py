from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from datetime import datetime
from services.parser_service import ParserService
from models.schemas import ParsedDocumentResponse

load_dotenv()

app = FastAPI(
    title="Pilot Documents Parser API",
    description="API for parsing .msg, .pdf, and .doc files",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads/")
os.makedirs(UPLOAD_DIR, exist_ok=True)

parser_service = ParserService()

@app.get("/")
async def root():
    return {
        "message": "Pilot Documents Parser API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.post("/api/parse/msg", response_model=ParsedDocumentResponse)
async def parse_msg(file: UploadFile = File(...)):
    if not file.filename.endswith('.msg'):
        raise HTTPException(status_code=400, detail="File must be a .msg file")
    try:
        contents = await file.read()
        result = parser_service.parse_msg(contents, file.filename)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing MSG file: {str(e)}")

@app.post("/api/parse/pdf", response_model=ParsedDocumentResponse)
async def parse_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be a .pdf file")
    try:
        contents = await file.read()
        result = parser_service.parse_pdf(contents, file.filename)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing PDF file: {str(e)}")

@app.post("/api/parse/doc", response_model=ParsedDocumentResponse)
async def parse_doc(file: UploadFile = File(...)):
    if not (file.filename.endswith('.doc') or file.filename.endswith('.docx')):
        raise HTTPException(status_code=400, detail="File must be a .doc or .docx file")
    try:
        contents = await file.read()
        result = parser_service.parse_doc(contents, file.filename)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing DOC file: {str(e)}")

@app.get("/api/documents")
async def get_documents():
    return []

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)