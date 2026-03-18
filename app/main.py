from fastapi import FastAPI, HTTPException
from app.schemas import TaskRequest, TaskResponse
from app.service import run_workflow

app = FastAPI(
    title="AI Task API",
    description="FastAPI service that exposes a simple planner-executor agent workflow.",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/task", response_model=TaskResponse)
def process_task(request: TaskRequest):
    try:
        result = run_workflow(request.task)
        return result
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc
