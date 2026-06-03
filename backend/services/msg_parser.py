from typing import Dict, Any
import io
try:
    import extract_msg
except ImportError:
    extract_msg = None

class MsgParser:
    def parse(self, file_content: bytes) -> Dict[str, Any]:
        if extract_msg is None:
            raise ImportError("extract_msg required. Install: pip install extract-msg")
        
        try:
            msg = extract_msg.Message(io.BytesIO(file_content))
            from_addr = msg.sender if hasattr(msg, 'sender') else None
            to_addrs = msg.to if hasattr(msg, 'to') else None
            cc_addrs = msg.cc if hasattr(msg, 'cc') else None
            bcc_addrs = msg.bcc if hasattr(msg, 'bcc') else None
            subject = msg.subject if hasattr(msg, 'subject') else None
            date = msg.date if hasattr(msg, 'date') else None
            body = msg.body if hasattr(msg, 'body') else msg.htmlBody if hasattr(msg, 'htmlBody') else ''
            
            attachments = []
            if hasattr(msg, 'attachments'):
                for attachment in msg.attachments:
                    if hasattr(attachment, 'filename'):
                        attachments.append(attachment.filename)
            
            return {
                'from': from_addr,
                'to': to_addrs,
                'cc': cc_addrs,
                'bcc': bcc_addrs,
                'subject': subject,
                'date': str(date) if date else None,
                'body': body,
                'attachments': attachments
            }
        except Exception as e:
            raise Exception(f"Error parsing MSG: {str(e)}")