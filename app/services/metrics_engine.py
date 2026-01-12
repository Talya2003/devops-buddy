from app.models.github import GitHubRepository
from app.models.metrics import RepositoryMetrics


class MetricsEngine:
    @staticmethod
    def calculate(
        repo: GitHubRepository,
        commits_count: int,
        contributors_count: int,
    ) -> RepositoryMetrics:
        popularity_score = min(repo.stars / 100, 10)

        issue_health_score = max(
            0,
            10 - (repo.open_issues / 10),
        )

        commits_score = min(commits_count / 50, 10)
        contributors_score = min(contributors_count, 10)

        activity_score = round(
            (
                popularity_score
                + issue_health_score
                + commits_score
                + contributors_score
            ) / 4,
            2,
        )

        return RepositoryMetrics(
            activity_score=activity_score,
            popularity_score=round(popularity_score, 2),
            issue_health_score=round(issue_health_score, 2),
            commits_score=round(commits_score, 2),
            contributors_score=round(contributors_score, 2),
        )
