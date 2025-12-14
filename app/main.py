from fastapi import FastAPI
from app.tasks import create_task
from app.ledger import record_event
from app.artifacts import write_artifact

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

    artifact = write_artifact(
        task_id=task.id,
        content={
            "task": task.dict(),
            "ledger": ledger_event
        }
    )

    return {
        "task": task,
        "ledger": ledger_event,
        "artifact": artifact
    }
