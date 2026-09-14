import uuid

from app.database.crud import (
    get_ready_tasks,
    update_task_status,
    create_task_result
)

from app.agents.hr_agent import execute_hr_task
from app.agents.it_agent import execute_it_task


def create_onboarding_plan(workflow_id: str):

    hr_task_id = str(uuid.uuid4())

    return [
        {
            "task_id": hr_task_id,
            "workflow_id": workflow_id,
            "task_name": "HR Verification",
            "assigned_agent": "HR_AGENT",
            "status": "PENDING",
            "depends_on": None
        },
        {
            "task_id": str(uuid.uuid4()),
            "workflow_id": workflow_id,
            "task_name": "IT Account Setup",
            "assigned_agent": "IT_AGENT",
            "status": "PENDING",
            "depends_on": hr_task_id
        },
        {
            "task_id": str(uuid.uuid4()),
            "workflow_id": workflow_id,
            "task_name": "Payroll Setup",
            "assigned_agent": "FINANCE_AGENT",
            "status": "PENDING",
            "depends_on": hr_task_id
        },
        {
            "task_id": str(uuid.uuid4()),
            "workflow_id": workflow_id,
            "task_name": "Asset Allocation",
            "assigned_agent": "ADMIN_AGENT",
            "status": "PENDING",
            "depends_on": hr_task_id
        }
    ]

def get_next_tasks(db, workflow_id: str):
    return get_ready_tasks(
        db=db,
        workflow_id=workflow_id
    )

def execute_task(db, task):

    update_task_status(
        db=db,
        task_id=task["task_id"],
        status="IN_PROGRESS"
    )

    if task["assigned_agent"] == "HR_AGENT":
        response = execute_hr_task(task)

    elif task["assigned_agent"] == "IT_AGENT":
        response = execute_it_task(task)

    else:
        response = {
            "status": "FAILED",
            "result": None,
            "error": "Agent not implemented"
        }

    update_task_status(
        db=db,
        task_id=task["task_id"],
        status=response["status"]
    )

    create_task_result(
        db=db,
        task_id=task["task_id"],
        result=response.get("result"),
        error=response.get("error")
    )

    return response