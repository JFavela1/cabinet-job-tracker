from fastapi import FastAPI

app = FastAPI(title="Cabinet Job Tracker")


@app.get("/healthz")
def healthz() -> dict[str, str]:
    """Liveness probe. Container Apps will point at this."""
    return {"status": "ok"}
