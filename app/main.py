from fastapi import FastAPI
from app.routes import github

app = FastAPI(
    title="DevOps Buddy",
    description="Python-based DevOps insights system",
    version="0.1.0",
)

app.include_router(github.router)


@app.get("/")
def root():
    return {"status": "DevOps Buddy is running"}
