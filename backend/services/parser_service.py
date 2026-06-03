from typing import Dict, List, Any
from datetime import datetime
from .msg_parser import MsgParser
from .pdf_parser import PdfParser
from .doc_parser import DocParser
from models.schemas import ParsedDocumentResponse, Table, Email

class ParserService:
    def __init__(self):
        self.msg_parser = MsgParser()
        self.pdf_parser = PdfParser()
        self.doc_parser = DocParser()

    def parse_msg(self, file_content: bytes, filename: str) -> ParsedDocumentResponse:
        try:
            msg_data = self.msg_parser.parse(file_content)
            emails = []
            if msg_data.get('from') or msg_data.get('to') or msg_data.get('subject'):
                emails.append(Email(
                    from_=msg_data.get('from'),
                    to=msg_data.get('to'),
                    cc=msg_data.get('cc'),
                    bcc=msg_data.get('bcc'),
                    subject=msg_data.get('subject'),
                    date=msg_data.get('date'),
                    body=msg_data.get('body'),
                    attachments=msg_data.get('attachments', [])
                ))
            
            tables = self._extract_tables_from_text(msg_data.get('body', ''))
            
            return ParsedDocumentResponse(
                filename=filename,
                file_type='msg',
                content=msg_data.get('body', ''),
                tables=tables,
                emails=emails,
                metadata={
                    'from': msg_data.get('from'),
                    'to': msg_data.get('to'),
                    'subject': msg_data.get('subject'),
                    'date': msg_data.get('date'),
                    'attachment_count': len(msg_data.get('attachments', []))
                },
                created_at=datetime.now()
            )
        except Exception as e:
            raise Exception(f"Error parsing MSG file: {str(e)}")

    def parse_pdf(self, file_content: bytes, filename: str) -> ParsedDocumentResponse:
        try:
            pdf_data = self.pdf_parser.parse(file_content)
            tables = pdf_data.get('tables', [])
            content = pdf_data.get('text', '')
            
            return ParsedDocumentResponse(
                filename=filename,
                file_type='pdf',
                content=content,
                tables=tables,
                emails=[],
                metadata={
                    'num_pages': pdf_data.get('num_pages', 0),
                    'author': pdf_data.get('author'),
                    'title': pdf_data.get('title'),
                    'subject': pdf_data.get('subject'),
                    'creator': pdf_data.get('creator'),
                    'creation_date': pdf_data.get('creation_date')
                },
                created_at=datetime.now()
            )
        except Exception as e:
            raise Exception(f"Error parsing PDF file: {str(e)}")

    def parse_doc(self, file_content: bytes, filename: str) -> ParsedDocumentResponse:
        try:
            doc_data = self.doc_parser.parse(file_content)
            tables = doc_data.get('tables', [])
            content = doc_data.get('text', '')
            
            return ParsedDocumentResponse(
                filename=filename,
                file_type='doc',
                content=content,
                tables=tables,
                emails=[],
                metadata={
                    'author': doc_data.get('author'),
                    'title': doc_data.get('title'),
                    'subject': doc_data.get('subject'),
                    'created': doc_data.get('created'),
                    'modified': doc_data.get('modified'),
                    'table_count': len(tables)
                },
                created_at=datetime.now()
            )
        except Exception as e:
            raise Exception(f"Error parsing DOC file: {str(e)}")

    @staticmethod
    def _extract_tables_from_text(text: str) -> List[Table]:
        return []