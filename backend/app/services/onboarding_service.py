from app.database.crud import (
    create_employee,
    create_workflow,
    create_onboarding_tasks
)

from app.agents.supervisor import create_onboarding_plan

def start_onboarding(
    db,
    employee_id: str,
    employee_name: str,
    department: str,
    designation: str,
    joining_date: str,
    email: str
):
    employee = create_employee(
        db=db,
        employee_id=employee_id,
        employee_name=employee_name,
        department=department,
        designation=designation,
        joining_date=joining_date,
        email=email
    )

    workflow = create_workflow(
        db=db,
        employee_id=employee["employee_id"]
    )

    tasks = create_onboarding_plan(
    workflow_id=workflow["workflow_id"]
    )

    create_onboarding_tasks(
        db=db,
        tasks=tasks
    )

    return {
        "employee": employee,
        "workflow": workflow,
        "tasks": tasks
    }