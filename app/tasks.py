from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4

class Task(BaseModel):
    id: str
    title: str
    description: str
    status: str
    created_at: datetime

def create_task(title: str, description: str) -> Task:
    return Task(
        id=str(uuid4()),
        title=title,
        description=description,
        status="created",
        created_at=datetime.utcnow()
    )
