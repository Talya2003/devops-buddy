from fastapi import FastAPI

app = FastAPI(
    title="DevOps Buddy",
    description="Python-based DevOps insights system",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"status": "DevOps Buddy is running"}
