from fastapi import APIRouter, HTTPException
from app.services.github_client import GitHubClient
from app.models.github import GitHubRepository
from app.services.metrics_engine import MetricsEngine
from app.models.metrics import RepositoryMetrics

router = APIRouter(prefix="/github", tags=["GitHub"])

client = GitHubClient()


@router.get(
    "/repo/{owner}/{repo}",
    response_model=GitHubRepository,
)
def get_repository(owner: str, repo: str):
    try:
        return client.get_repository(owner, repo)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get(
    "/repo/{owner}/{repo}/metrics",
    response_model=RepositoryMetrics,
)
def get_repository_metrics(owner: str, repo: str):
    try:
        repository = client.get_repository(owner, repo)

        commits_count = client.get_commits_count(owner, repo)
        contributors_count = client.get_contributors_count(owner, repo)

        return MetricsEngine.calculate(
            repository,
            commits_count,
            contributors_count,
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
