from app.models.github import GitHubRepository
from app.models.metrics import RepositoryMetrics


class MetricsEngine:
    @staticmethod
    def calculate(repo: GitHubRepository) -> RepositoryMetrics:
        popularity_score = min(repo.stars / 100, 10)

        issue_health_score = max(
            0,
            10 - (repo.open_issues / 10),
        )

        activity_score = round(
            (popularity_score + issue_health_score) / 2,
            2,
        )

        return RepositoryMetrics(
            activity_score=activity_score,
            popularity_score=round(popularity_score, 2),
            issue_health_score=round(issue_health_score, 2),
        )
