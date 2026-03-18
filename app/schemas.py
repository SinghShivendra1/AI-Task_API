from pydantic import BaseModel, Field
from typing import List, Dict, Any


class TaskRequest(BaseModel):
    task: str = Field(..., min_length=1, description="High-level task to process")


class PlanStep(BaseModel):
    step_id: int
    title: str
    description: str


class ExecutionResult(BaseModel):
    step_results: List[Dict[str, Any]]
    final_output: str


class TaskResponse(BaseModel):
    task: str
    plan: List[PlanStep]
    execution: ExecutionResult
    status: str
