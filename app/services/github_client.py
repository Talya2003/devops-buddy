import httpx
from app.core.config import GITHUB_API_BASE_URL, GITHUB_TOKEN
from app.models.github import GitHubRepository
import httpx


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

    def get_repository(self, owner: str, repo: str):
        try:
            response = self.client.get(f"/repos/{owner}/{repo}")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                raise ValueError("Repository not found")
            if exc.response.status_code == 403:
                raise ValueError("GitHub API rate limit exceeded")
            raise ValueError("GitHub API error")

    def get_commits_count(self, owner: str, repo: str) -> int:
        response = self.client.get(
            f"/repos/{owner}/{repo}/commits",
            params={"per_page": 1},
        )
        response.raise_for_status()

        if "Link" not in response.headers:
            return len(response.json())

        link_header = response.headers["Link"]
        last_page = int(link_header.split("page=")[-1].split(">")[0])
        return last_page


    def get_contributors_count(self, owner: str, repo: str) -> int:
        response = self.client.get(
            f"/repos/{owner}/{repo}/contributors",
            params={"per_page": 1},
        )
        response.raise_for_status()

        if "Link" not in response.headers:
            return len(response.json())

        link_header = response.headers["Link"]
        last_page = int(link_header.split("page=")[-1].split(">")[0])
        return last_page
