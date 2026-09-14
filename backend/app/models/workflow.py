from datetime import datetime


class Workflow:
    def __init__(
        self,
        workflow_id: str,
        employee_id: str,
        workflow_type: str,
        status: str = "PENDING"
    ):
        self.workflow_id = workflow_id
        self.employee_id = employee_id
        self.workflow_type = workflow_type
        self.status = status
        self.created_at = datetime.utcnow()
        self.completed_at = None