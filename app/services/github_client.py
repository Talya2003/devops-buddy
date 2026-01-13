import httpx
from app.core.config import settings
from app.models.github import GitHubRepository
import httpx
from app.core.logger import logger
from datetime import datetime, timedelta
from collections import Counter


class GitHubClient:
    def __init__(self):
        headers = {}
        if settings.GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {settings.GITHUB_TOKEN}"

        self.client = httpx.Client(
            base_url=settings.GITHUB_API_BASE_URL,
            headers=headers,
            timeout=10.0,
        )

    def get_repository(self, owner: str, repo: str) -> GitHubRepository:
        try:
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


    def get_summary(self, owner: str, repo: str) -> dict:
        repository = self.get_repository(owner, repo)
        contributors = self.get_contributors_count(owner, repo)

        return {
            "full_name": repository.full_name,
            "description": repository.description,
            "stars": repository.stars,
            "forks": repository.forks,
            "open_issues": repository.open_issues,
            "contributors": contributors,
            "language": repository.language,
            "html_url": repository.html_url,
        }
    
    def get_commits_last_30_days(self, owner: str, repo: str) -> int:
        since = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"

        response = self.client.get(
            f"/repos/{owner}/{repo}/commits",
            params={"since": since, "per_page": 100},
        )
        response.raise_for_status()

        return len(response.json())


    def get_commit_activity_last_30_days(self, owner: str, repo: str) -> dict:
        since = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"

        response = self.client.get(
            f"/repos/{owner}/{repo}/commits",
            params={"since": since, "per_page": 100},
        )
        response.raise_for_status()

        commits = response.json()

        counter = Counter()
        for commit in commits:
            date = commit["commit"]["author"]["date"][:10]
            counter[date] += 1

        return dict(counter)