# AI Task API

## Overview
This project exposes a simple **agentic AI workflow** through a FastAPI service.

It accepts a task through an API endpoint, passes that task to a **Planner Agent** for task decomposition, executes the generated steps with an **Executor Agent**, and returns a structured JSON response.

This repository is designed to demonstrate:
- FastAPI backend development
- API design for AI workflows
- modular Python architecture
- agent orchestration concepts
- testable service structure

## Why This Project Matters
Modern AI systems are often deployed as services, not just scripts. This project shows how to package an agent-based workflow behind a clean API so it can be integrated into applications, dashboards, and automation systems.

## Architecture
```text
Client Request -> FastAPI Endpoint -> Planner Agent -> Executor Agent -> JSON Response
```

## Features
- `/health` endpoint for service monitoring
- `/task` endpoint for task processing
- Planner agent for task decomposition
- Executor agent for mock execution
- structured JSON output
- clean modular design
- unit tests using pytest

## Example Request
```json
{
  "task": "Write a short blog outline on how agentic AI can improve customer support workflows."
}
```

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test the API
```bash
pytest
```

## Example cURL Request
```bash
curl -X POST "http://127.0.0.1:8000/task" \
  -H "Content-Type: application/json" \
  -d '{"task": "Write a short blog on AI in healthcare"}'
```

## Example Response
```json
{
  "task": "Write a short blog on AI in healthcare",
  "plan": [
    {
      "step_id": 1,
      "title": "Understand task",
      "description": "Identify audience, intent, and deliverable."
    }
  ],
  "execution": {
    "step_results": [],
    "final_output": "..."
  },
  "status": "completed"
}
```

## Future Improvements
- integrate OpenAI or another LLM API
- add authentication and rate limiting
- persist workflow results to a database
- add a reviewer agent
- deploy using Docker

# Auther:
Shivendra Singh
