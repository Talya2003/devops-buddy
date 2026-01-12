from pydantic import BaseModel
from typing import Optional


class GitHubRepository(BaseModel):
    name: str
    full_name: str
    description: Optional[str]
    stars: int
    forks: int
    open_issues: int
    language: Optional[str]
    html_url: str
