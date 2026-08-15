from app.database.connection import SessionLocal
from app.models.employee import Employee
from app.models.workflow import Workflow
from app.models.task import Task

db = SessionLocal()

employee = db.query(Employee).filter(
    Employee.employee_id == "EMP003"
).first()

workflow = db.query(Workflow).filter(
    Workflow.employee_id == "EMP003"
).order_by(
    Workflow.created_at.desc()
).first()

tasks = db.query(Task).filter(
    Task.workflow_id == workflow.workflow_id
).all()

print("EMPLOYEE")
print("ID:", employee.employee_id)
print("Name:", employee.employee_name)
print("Department:", employee.department)

print("\nWORKFLOW")
print("ID:", workflow.workflow_id)
print("Type:", workflow.workflow_type)
print("Status:", workflow.status)

print("\nTASKS")

for task in tasks:
    print(
        task.task_name,
        "|",
        task.assigned_agent,
        "|",
        task.status,
        "| Depends on:",
        task.depends_on
    )

db.close()