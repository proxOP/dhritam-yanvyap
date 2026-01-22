# Dritam - AI Financial Intelligence System

**Phase 1 Implemented**

Dritam is an autonomous AI system designed to analyze financial markets, supply chains, and economic events using a graph of specialized agents.

## 🏗 Architecture

The system follows a micro-agent architecture orchestrated by a reasoning graph.

- **Backend**: Python 3.11 + FastAPI
- **Orchestration**: LangGraph (Stateful DAG execution)
- **Agents**: LangChain (Specialized roles: Market, Supply Chain, Governance, etc.)
- **Frontend**: React + Vite
- **Storage**: In-memory Event/Pattern stores (Phase 1)

## 🚀 Getting Started

### Prerequisites

- Python 3.11.9
- Node.js & npm (for frontend)

### 1. Backend Setup

The project uses a local virtual environment.

```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the Intelligence API
uvicorn dritam.api:app --reload
```
*API will run at http://localhost:8000*

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start Development Server
npm run dev
```
*UI will run at http://localhost:5173*

## 🧠 Reasoning Graph

The system processes queries through the following pipeline:

1. **Observer**: Detects events/queries.
2. **Interpreter**: Structures the raw input.
3. **Domain Specialist**: Identifies relevant sectors.
4. **Market Agent**: Analyzes financial impact.
5. **Supply Chain Agent**: Maps dependencies.
6. **Governance**: Checks compliance and safety.
7. **Confidence**: Scores the analysis reliability.
8. **Composer**: Synthesizes the final intelligence report.

## 🧪 Testing

You can verify the backend logic without the frontend using the provided test script:

```bash
python test_api.py
```

## 📁 Repository Structure

- `dritam/`: Core backend and agent logic.
  - `agents/`: Agent definitions.
  - `graph/`: LangGraph orchestration workflow.
  - `api/`: FastAPI routes and lifecycle.
- `frontend/`: React application source.

## 📜 License

Proprietary/Commercial - Dhritam Project.
