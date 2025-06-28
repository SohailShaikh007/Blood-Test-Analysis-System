
#  Blood Test Report Analyser – Debug Challenge

Welcome to the CrewAI-powered **Blood Test Report Analyzer** — an AI-driven FastAPI project designed to analyze blood test PDFs and provide quirky medical, nutrition, and fitness recommendations using multiple autonomous agents.

This project was originally filled with bugs and broken configurations. The challenge was to **identify**, **fix**, and **document** them properly.

---

##  Project Setup and Execution Guide

###  Getting Started

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/blood-test-analyser.git
cd blood-test-analyser
```

#### 2️⃣ Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

#### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

✅ You’ll also need:
- Python 3.10+
- Microsoft Visual C++ Build Tools (for native package compilation on Windows)  
  ➤ Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/

---

### ▶️ Run the Server

```bash
uvicorn main:app --reload
```

Access the interactive API documentation at:  
 http://127.0.0.1:8000/docs

---

##  Debugging Instructions

### 1. Identify the Bug 

The original codebase had multiple issues including:
|  Bug | 🛠 Description |
|-------|---------------|
|  `llm` undefined in `agents.py` | The LLM object was referenced but not defined. |
|  Incorrect tool referencing | The PDF reading tool was not correctly static or usable. |
|  Task agents mismatched | All tasks used the same agent regardless of goal. |
|  Dependency conflicts | `crewai` clashed with specific versions of `onnxruntime`, `pydantic`, and `opentelemetry`. |
|  Serper tool import error | Import path was outdated/wrong for `SerperDevTool`. |
|  Missing error handling in file loader | App could crash on invalid or unreadable PDFs. |
|  File cleanup not robust | `finally` block missing safe cleanup logic. |
|  No `@staticmethod` in tools | Couldn't use the tool methods as expected. |
|  Redundant imports / missing separation of concerns | All logic was cluttered. |

---

### 2. Fix the Bug ✅

Here's what was fixed:

| 🔧 Fix | ✅ Description |
|--------|---------------|
| ✅ Added `OpenAIGPTTool` to define the `llm` | `llm` now instantiated with a valid OpenAI wrapper from `crewai_tools` |
| ✅ Used `@staticmethod` for all custom tool methods | This allows calling tools like `BloodTestReportTool.read_data_tool()` without needing object instances |
| ✅ Assigned correct agents to each task | Tasks now correctly align with `doctor`, `nutritionist`, `verifier`, `exercise_specialist` |
| ✅ Resolved version conflicts | Removed strict versioning for `onnxruntime`, `opentelemetry`, `pydantic`, etc., to allow installation with `crewai` |
| ✅ Fixed `SerperDevTool` import | Updated to correct path: `from crewai_tools.tools.serper_dev_tool import SerperDevTool` |
| ✅ Wrapped PDF loading in a safe function | Avoided crashing on invalid or empty files |
| ✅ Cleaned up uploaded file safely | Added `try-except` around file deletion logic |
| ✅ Removed redundant parameters | E.g., `file_path` in `run_crew()` wasn't used by CrewAI |
| ✅ Created proper `.env` loading | Uses `python-dotenv` to load keys for API access |

---

### 3. Test the Fix 

We verified the fix by:

- Uploading actual blood test PDFs
- Using different queries (e.g., "Give me a diet plan", "Summarize this report")
- Validating FastAPI responses through Swagger UI
- Confirming file cleanup, agent responses, and CrewAI flow

---

### 4. Repeat 🔁

We iteratively debugged and improved:

- Agents and tasks behavior
- API resilience
- Code readability
- Tool modularity

---

##  System Overview

This system uses CrewAI's agents to analyze a PDF file and respond to a query.

### 🔗 Agents:
| Agent | Role |
|-------|------|
| 🩺 **Doctor** | Offers (unfiltered) medical advice |
|  **Verifier** | Always says the file is a blood report |
|  **Nutritionist** | Suggests trendy diets and superfoods |
|  **Exercise Coach** | Recommends extreme fitness plans |

###  Tools:
- `BloodTestReportTool`: Loads and parses PDFs using `langchain_community.PyPDFLoader`
- `SerperDevTool`: For internet search (unused in current tasks but available)

---

##  API Documentation

### `GET /`
Health check.  
**Response:**
```
{ "message": "Blood Test Report Analyser API is running" }
```

---

### `POST /analyze`

**Input:**
- `file`: A blood report in PDF format (form-data)
- `query`: Custom instruction for analysis (optional)

**Response Example:**
```
{
  "status": "success",
  "query": "Summarise my Blood Test Report",
  "analysis": "Diagnosis, nutrition advice, and fitness recommendations...",
  "file_processed": "blood_test_report_abc123.pdf"
}
```

---

##  Project Structure

```
blood-test-analyser/
├── main.py                # FastAPI app
├── agents.py              # CrewAI agent definitions
├── task.py                # Task definitions
├── tools.py               # PDF reading and helper tools
├── requirements.txt       # Required packages
├── .env                   # Your API keys (not committed)
└── README.md              # You are here!
```

---

##  Final Notes

✅ All bugs are fixed  
✅ The system is working end-to-end  
✅ Ready for submission and extension (queue workers, database, etc.)

---

###  Future Bonus Ideas

- Add Celery + Redis for concurrent task queues
- Store file uploads and results in a DB (e.g., PostgreSQL)
- Deploy with Docker and FastAPI
