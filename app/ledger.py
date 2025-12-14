from datetime import datetime
from typing import Dict
from uuid import uuid4

def record_event(event_type: str, payload: Dict) -> Dict:
    return {
        "id": str(uuid4()),
        "event_type": event_type,
        "payload": payload,
        "timestamp": datetime.utcnow().isoformat()
    }
