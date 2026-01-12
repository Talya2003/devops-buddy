import httpx
from app.core.config import GITHUB_API_BASE_URL, GITHUB_TOKEN
from app.models.github import GitHubRepository


class GitHubClient:
    def __init__(self):
        headers = {}
        if GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

        self.client = httpx.Client(
            base_url=GITHUB_API_BASE_URL,
            headers=headers,
            timeout=10.0,
        )

    def get_repository(self, owner: str, repo: str) -> GitHubRepository:
        response = self.client.get(f"/repos/{owner}/{repo}")
        response.raise_for_status()
        data = response.json()

        return GitHubRepository(
            name=data["name"],
            full_name=data["full_name"],
            description=data["description"],
            stars=data["stargazers_count"],
            forks=data["forks_count"],
            open_issues=data["open_issues_count"],
            language=data["language"],
            html_url=data["html_url"],
        )
