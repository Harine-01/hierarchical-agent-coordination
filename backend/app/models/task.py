from datetime import datetime


class Task:
    def __init__(
        self,
        task_id: str,
        workflow_id: str,
        task_name: str,
        assigned_agent: str,
        status: str = "PENDING",
        depends_on: str = None
    ):
        self.task_id = task_id
        self.workflow_id = workflow_id
        self.task_name = task_name
        self.assigned_agent = assigned_agent
        self.status = status
        self.depends_on = depends_on
        self.created_at = datetime.utcnow()
        self.started_at = None
        self.completed_at = None