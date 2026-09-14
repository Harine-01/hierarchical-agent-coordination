from datetime import datetime


class TaskResult:
    def __init__(
        self,
        result_id: str,
        task_id: str,
        result: str = None,
        error: str = None
    ):
        self.result_id = result_id
        self.task_id = task_id
        self.result = result
        self.error = error
        self.created_at = datetime.utcnow()