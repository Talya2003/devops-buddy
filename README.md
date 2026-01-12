# devops-buddy
DevOps Buddy – a Python-based system that analyzes GitHub repositories and provides actionable DevOps insights via a clean API and dashboard.

DevOps Buddy is a fully Python-based system that analyzes GitHub repositories and provides clear, actionable DevOps insights through a clean API and dashboard.

The project is designed as a real-world, production-style MVP — focusing on clarity, maintainability, and developer experience.

---

## ✨ Features (MVP)
- Analyze GitHub repositories using the GitHub API
- Expose insights through a FastAPI-based backend
- Clean and extensible project architecture
- Interactive API documentation (Swagger UI)

---

## 🧱 Tech Stack
- **Python 3.10+**
- **FastAPI** – API framework
- **Uvicorn** – ASGI server
- **SQLite** (planned)
- **SQLAlchemy** (planned)

---

## 📦 Project Structure
devops-buddy/
├── app/
│ ├── init.py
│ └── main.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

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

## 🧭 Roadmap

 - GitHub API integration
 - Repository metrics engine
 - Persistent storage layer
 - Dashboard UI
 - Notifications & automation

## 📄 License
MIT License
