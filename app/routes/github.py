from fastapi import APIRouter, HTTPException
from app.services.github_client import GitHubClient
from app.models.github import GitHubRepository
from app.services.metrics_engine import MetricsEngine
from app.models.metrics import RepositoryMetrics
from app.core.logger import logger
from app.models.summary import RepositorySummary

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

@router.get(
    "/repo/{owner}/{repo}/metrics",
    response_model=RepositoryMetrics,
    responses={
        404: {"description": "Repository not found"},
        429: {"description": "GitHub API rate limit exceeded"},
    },
)
def get_repository_metrics(owner: str, repo: str):
    logger.info(f"Metrics requested for {owner}/{repo}")
    try:
        repository = client.get_repository(owner, repo)
        commits_count = client.get_commits_count(owner, repo)
        contributors_count = client.get_contributors_count(owner, repo)

        return MetricsEngine.calculate(
            repository,
            commits_count,
            contributors_count,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.get(
    "/repo/{owner}/{repo}/summary",
    response_model=RepositorySummary,
)
def get_repository_summary(owner: str, repo: str):
    try:
        return client.get_summary(owner, repo)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.get("/repo/{owner}/{repo}/commits/activity")
def get_commit_activity(owner: str, repo: str):
    try:
        return client.get_commit_activity_last_30_days(owner, repo)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
