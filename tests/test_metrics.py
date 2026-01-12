from app.models.github import GitHubRepository
from app.services.metrics_engine import MetricsEngine


def test_metrics_calculation():
    repo = GitHubRepository(
        name="test",
        full_name="user/test",
        description="test repo",
        stars=100,
        forks=10,
        open_issues=0,
        language="Python",
        html_url="https://github.com/user/test",
    )

    metrics = MetricsEngine.calculate(
        repo,
        commits_count=100,
        contributors_count=5,
    )

    assert metrics.activity_score > 0
    assert metrics.popularity_score == 1.0
    assert metrics.issue_health_score == 10.0
    assert metrics.commits_score == 2.0
    assert metrics.contributors_score == 5.0
