# devops-buddy
DevOps Buddy is a fully Python-based system that analyzes GitHub repositories and provides clear, actionable DevOps insights through a clean API and an interactive dashboard.

The project is designed as a real-world, production-style MVP — focusing on clarity, maintainability, developer experience, and visual impact.


## ✨ Features (MVP)
- Analyze GitHub repositories using the GitHub API
- Calculate meaningful DevOps metrics (activity, popularity, issues, commits, contributors)
- Expose insights through a FastAPI-based backend
- Interactive API documentation (Swagger UI)
- Clean, extensible, production-style architecture
- Logging, configuration management, and automated tests


## 🧱 Tech Stack
- **Python 3.10+**
- **FastAPI** – API framework
- **Uvicorn** – ASGI server
- **Pydantic** – Data validation
- **Streamlit** – Interactive dashboard
- **pytest** – Testing framework
- **SQLite** (planned)
- **SQLAlchemy** (planned)


## 📦 Project Structure
```
devops-buddy/
├── app/
│ ├── core/ # config & logging
│ ├── models/ # Pydantic models
│ ├── routes/ # API routes
│ ├── services/ # GitHub client & metrics engine
│ └── main.py
│
├── dashboard/
│ └── app.py # Streamlit dashboard
│
├── tests/
│ ├── test_health.py
│ └── test_metrics.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## ▶️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Talya2003/devops-buddy.git
cd devops-buddy
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
uvicorn app.main:app --reload
```

Visit:

 * API: `http://127.0.0.1:8000`
 * Docs: `http://127.0.0.1:8000/docs`


## 📊 Run the Dashboard
In a separate terminal (while the API is running):

`streamlit run dashboard/app.py`

Dashboard will open at: 
`http://localhost:8501`


Enter a GitHub owner and repository name to instantly view DevOps insights.

## 🧪 Run Tests
`pytest`

Optional coverage:
`pytest --cov=app
`

## 🧭 Roadmap
 - Historical metrics with persistent storage
 - Advanced DevOps scoring algorithms
 - Charts & trends in the dashboard
 - GitHub Actions (CI)
 - Dockerized deployment
 - Notifications & automation

## 📄 License
MIT License
