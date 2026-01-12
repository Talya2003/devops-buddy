from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_ENV: str = os.getenv("APP_ENV", "development")

    GITHUB_API_BASE_URL: str = "https://api.github.com"
    GITHUB_TOKEN: str | None = os.getenv("GITHUB_TOKEN")


settings = Settings()