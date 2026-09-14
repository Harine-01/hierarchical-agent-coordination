from app.database.crud import (
    create_employee,
    create_workflow,
    create_onboarding_tasks
)


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

    tasks = create_onboarding_tasks(
        db=db,
        workflow_id=workflow["workflow_id"]
    )

    return {
        "employee": employee,
        "workflow": workflow,
        "tasks": tasks
    }