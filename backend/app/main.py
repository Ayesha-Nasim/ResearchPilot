from fastapi import FastAPI

app = FastAPI(title="ResearchPilot Backend")


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
