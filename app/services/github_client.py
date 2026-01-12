import httpx
from app.core.config import GITHUB_API_BASE_URL, GITHUB_TOKEN


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

    def get_repository(self, owner: str, repo: str) -> dict:
        response = self.client.get(f"/repos/{owner}/{repo}")
        response.raise_for_status()
        return response.json()
