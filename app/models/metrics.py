from pydantic import BaseModel


class RepositoryMetrics(BaseModel):
    activity_score: float
    popularity_score: float
    issue_health_score: float
    commits_score: float
    contributors_score: float