from typing import List, Dict


class PlannerAgent:
    """Simple deterministic planner for demo purposes."""

    def create_plan(self, task: str) -> List[Dict]:
        normalized = task.strip().lower()
        if not normalized:
            raise ValueError("Task cannot be empty.")

        if "blog" in normalized or "write" in normalized:
            return [
                {"step_id": 1, "title": "Understand task", "description": "Identify audience, intent, and deliverable."},
                {"step_id": 2, "title": "Create outline", "description": "Break the requested content into clear sections."},
                {"step_id": 3, "title": "Draft output", "description": "Generate the requested written deliverable."},
            ]

        if "analyze" in normalized or "report" in normalized:
            return [
                {"step_id": 1, "title": "Collect context", "description": "Identify the key inputs and scope."},
                {"step_id": 2, "title": "Analyze inputs", "description": "Extract relevant patterns and insights."},
                {"step_id": 3, "title": "Summarize findings", "description": "Return a concise final report."},
            ]

        return [
            {"step_id": 1, "title": "Interpret request", "description": "Understand the task objective and desired output."},
            {"step_id": 2, "title": "Plan execution", "description": "Convert the request into manageable steps."},
            {"step_id": 3, "title": "Produce result", "description": "Generate the final task output."},
        ]


class ExecutorAgent:
    """Executes each plan step with mock logic."""

    def execute(self, task: str, plan: List[Dict]) -> Dict:
        step_results = []
        for step in plan:
            step_results.append(
                {
                    "step_id": step["step_id"],
                    "title": step["title"],
                    "status": "completed",
                    "result": f'Completed "{step["title"]}" for task: {task}',
                }
            )

        final_output = (
            f"Task processed successfully. Generated {len(plan)} execution steps for: {task}"
        )

        return {"step_results": step_results, "final_output": final_output}
