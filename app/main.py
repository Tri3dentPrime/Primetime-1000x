from fastapi import FastAPI

app = FastAPI(title="PrimeTime 1000x Core")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "system": "PrimeTime-1000x",
        "message": "Core engine online"
    }
