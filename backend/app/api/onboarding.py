from fastapi import APIRouter, HTTPException

from app.schemas.onboarding import EmployeeOnboardingRequest
from app.database.crud import get_employee, get_workflow_tasks
from app.services.onboarding_service import start_onboarding
from app.database.connection import get_database
from app.agents.supervisor import get_next_tasks, execute_task

router = APIRouter(
    prefix="/onboarding",
    tags=["Employee Onboarding"]
)


@router.post("/")
def create_onboarding(
    request: EmployeeOnboardingRequest
):
    db = get_database()

    existing_employee = get_employee(
        db,
        request.employee_id
    )

    if existing_employee:
        raise HTTPException(
            status_code=409,
            detail="Employee ID already exists"
        )

    onboarding = start_onboarding(
        db=db,
        employee_id=request.employee_id,
        employee_name=request.employee_name,
        department=request.department,
        designation=request.designation,
        joining_date=request.joining_date,
        email=request.email
    )

    return {
        "message": "Employee onboarding created",
        "employee_id": onboarding["employee"]["employee_id"],
        "workflow_id": onboarding["workflow"]["workflow_id"],
        "tasks_created": len(onboarding["tasks"]),
        "status": onboarding["workflow"]["status"]
    }


@router.get("/{workflow_id}")
def get_onboarding_status(
    workflow_id: str
):
    db = get_database()

    workflow = db.workflows.find_one(
        {"workflow_id": workflow_id},
        {"_id": 0}
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found"
        )

    tasks = get_workflow_tasks(
        db=db,
        workflow_id=workflow_id
    )

    return {
        "workflow_id": workflow["workflow_id"],
        "employee_id": workflow["employee_id"],
        "workflow_type": workflow["workflow_type"],
        "status": workflow["status"],
        "tasks": [
            {
                "task_id": task["task_id"],
                "task_name": task["task_name"],
                "assigned_agent": task["assigned_agent"],
                "status": task["status"],
                "depends_on": task["depends_on"]
            }
            for task in tasks
        ]
    }

@router.get("/{workflow_id}/ready-tasks")
def get_ready_onboarding_tasks(
    workflow_id: str
):
    db = get_database()

    workflow = db.workflows.find_one(
        {"workflow_id": workflow_id},
        {"_id": 0}
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found"
        )

    tasks = get_next_tasks(
        db=db,
        workflow_id=workflow_id
    )

    return {
        "workflow_id": workflow_id,
        "ready_tasks": tasks
    }

@router.post("/{workflow_id}/execute-next")
def execute_next_task(
    workflow_id: str
):
    db = get_database()

    workflow = db.workflows.find_one(
        {"workflow_id": workflow_id},
        {"_id": 0}
    )

    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found"
        )

    ready_tasks = get_next_tasks(
        db=db,
        workflow_id=workflow_id
    )

    if not ready_tasks:
        return {
            "message": "No tasks are ready for execution",
            "workflow_id": workflow_id
        }

    task = ready_tasks[0]

    result = execute_task(
        db=db,
        task=task
    )

    return {
        "workflow_id": workflow_id,
        "task_id": task["task_id"],
        "task_name": task["task_name"],
        "assigned_agent": task["assigned_agent"],
        "result": result
    }