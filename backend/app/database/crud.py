from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.models.workflow import Workflow
import uuid
from app.models.task import Task
from app.models.task_result import TaskResult


def create_employee(
    db: Session,
    employee_id: str,
    employee_name: str,
    department: str,
    designation: str,
    joining_date: str,
    email: str
):
    employee = Employee(
        employee_id=employee_id,
        employee_name=employee_name,
        department=department,
        designation=designation,
        joining_date=joining_date,
        email=email
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


def get_employee(db: Session, employee_id: str):
    return db.query(Employee).filter(
        Employee.employee_id == employee_id
    ).first()

def create_workflow(
    db: Session,
    employee_id: str,
    workflow_type: str = "EMPLOYEE_ONBOARDING"
):
    workflow = Workflow(
        workflow_id=str(uuid.uuid4()),
        employee_id=employee_id,
        workflow_type=workflow_type,
        status="PENDING"
    )

    db.add(workflow)
    db.commit()
    db.refresh(workflow)

    return workflow

def create_onboarding_tasks(
    db: Session,
    workflow_id: str
):
    hr_task_id = str(uuid.uuid4())

    tasks = [
        Task(
            task_id=hr_task_id,
            workflow_id=workflow_id,
            task_name="HR Verification",
            assigned_agent="HR_AGENT",
            status="PENDING",
            depends_on=None
        ),
        Task(
            task_id=str(uuid.uuid4()),
            workflow_id=workflow_id,
            task_name="IT Account Setup",
            assigned_agent="IT_AGENT",
            status="PENDING",
            depends_on=hr_task_id
        ),
        Task(
            task_id=str(uuid.uuid4()),
            workflow_id=workflow_id,
            task_name="Payroll Setup",
            assigned_agent="FINANCE_AGENT",
            status="PENDING",
            depends_on=hr_task_id
        ),
        Task(
            task_id=str(uuid.uuid4()),
            workflow_id=workflow_id,
            task_name="Asset Allocation",
            assigned_agent="ADMIN_AGENT",
            status="PENDING",
            depends_on=hr_task_id
        )
    ]

    db.add_all(tasks)
    db.commit()

    for task in tasks:
        db.refresh(task)

    return tasks

def get_ready_tasks(
    db: Session,
    workflow_id: str
):
    pending_tasks = db.query(Task).filter(
        Task.workflow_id == workflow_id,
        Task.status == "PENDING"
    ).all()

    ready_tasks = []

    for task in pending_tasks:
        if task.depends_on is None:
            ready_tasks.append(task)
            continue

        dependency = db.query(Task).filter(
            Task.task_id == task.depends_on
        ).first()

        if dependency and dependency.status == "COMPLETED":
            ready_tasks.append(task)

    return ready_tasks

def update_task_status(
    db: Session,
    task_id: str,
    status: str
):
    task = db.query(Task).filter(
        Task.task_id == task_id
    ).first()

    if not task:
        return None

    task.status = status

    db.commit()
    db.refresh(task)

    return task

def create_task_result(
    db: Session,
    task_id: str,
    result: str = None,
    error: str = None
):
    task_result = TaskResult(
        result_id=str(uuid.uuid4()),
        task_id=task_id,
        result=result,
        error=error
    )

    db.add(task_result)
    db.commit()
    db.refresh(task_result)

    return task_result

def get_task_results(
    db: Session,
    task_id: str
):
    return db.query(TaskResult).filter(
        TaskResult.task_id == task_id
    ).all()

def get_workflow_tasks(
    db: Session,
    workflow_id: str
):
    return db.query(Task).filter(
        Task.workflow_id == workflow_id
    ).all()