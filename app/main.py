from fastapi import FastAPI
from app.tasks import create_task, Task
from app.ledger import record_event

app = FastAPI(title="PrimeTime 1000x Core")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "system": "PrimeTime-1000x",
        "message": "Core engine online"
    }

@app.post("/tasks")
def new_task(title: str, description: str):
    task = create_task(title=title, description=description)
    ledger_event = record_event(
        event_type="task_created",
        payload=task.dict()
    )
    return {
        "task": task,
        "ledger": ledger_event
    }
