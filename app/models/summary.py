from pydantic import BaseModel
from typing import Optional


class RepositorySummary(BaseModel):
    full_name: str
    description: Optional[str]
    stars: int
    forks: int
    open_issues: int
    contributors: int
    language: Optional[str]
    html_url: str
