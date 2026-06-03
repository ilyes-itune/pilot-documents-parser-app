from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class Table(BaseModel):
    headers: List[str]
    rows: List[List[Any]]

class Email(BaseModel):
    from_: str = None
    to: str = None
    cc: Optional[str] = None
    bcc: Optional[str] = None
    subject: str = None
    date: Optional[str] = None
    body: str = None
    attachments: List[str] = []

    class Config:
        populate_by_name = True

class ParsedDocumentResponse(BaseModel):
    id: Optional[str] = None
    filename: str
    file_type: str
    content: str
    tables: List[Table] = []
    emails: List[Email] = []
    metadata: Dict[str, Any] = {}
    created_at: Optional[datetime] = None