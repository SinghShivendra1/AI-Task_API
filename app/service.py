from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent


def run_workflow(task: str):
    planner = PlannerAgent()
    executor = ExecutorAgent()

    plan = planner.create_plan(task)
    execution = executor.execute_plan(task, plan)

    return {
        "task": task,
        "plan": plan,
        "execution": execution,
        "status": "completed",
    }
