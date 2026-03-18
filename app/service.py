from app.agents import PlannerAgent, ExecutorAgent


def run_workflow(task: str) -> dict:
    planner = PlannerAgent()
    executor = ExecutorAgent()

    plan = planner.create_plan(task)
    execution = executor.execute(task, plan)

    return {
        "task": task,
        "plan": plan,
        "execution": execution,
        "status": "completed",
    }
