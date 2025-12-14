from fastapi import FastAPI
from app.tasks import create_task, Task

app = FastAPI(title="PrimeTime 1000x Core")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "system": "PrimeTime-1000x",
        "message": "Core engine online"
    }

@app.post("/tasks", response_model=Task)
def new_task(title: str, description: str):
    task = create_task(title=title, description=description)
    return task
