from fastapi import APIRouter, HTTPException
from app.services.github_client import GitHubClient

router = APIRouter(prefix="/github", tags=["GitHub"])

client = GitHubClient()


@router.get("/repo/{owner}/{repo}")
def get_repository(owner: str, repo: str):
    try:
        return client.get_repository(owner, repo)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
