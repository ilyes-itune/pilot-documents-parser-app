from typing import Dict, Any, List
import io
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

class PdfParser:
    def parse(self, file_content: bytes) -> Dict[str, Any]:
        if PyPDF2 is None:
            raise ImportError("PyPDF2 required. Install: pip install PyPDF2")
        
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
            metadata = pdf_reader.metadata if hasattr(pdf_reader, 'metadata') else {}
            
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
            
            tables = []
            
            return {
                'text': text,
                'num_pages': len(pdf_reader.pages),
                'author': metadata.get('/Author') if metadata else None,
                'title': metadata.get('/Title') if metadata else None,
                'subject': metadata.get('/Subject') if metadata else None,
                'creator': metadata.get('/Creator') if metadata else None,
                'creation_date': metadata.get('/CreationDate') if metadata else None,
                'tables': tables
            }
        except Exception as e:
            raise Exception(f"Error parsing PDF: {str(e)}")