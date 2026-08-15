from app.database.connection import SessionLocal
from app.database.crud import create_workflow, create_onboarding_tasks

db = SessionLocal()

workflow = create_workflow(
    db=db,
    employee_id="EMP002"
)

tasks = create_onboarding_tasks(
    db=db,
    workflow_id=workflow.workflow_id
)

print("Workflow created:")
print("Workflow ID:", workflow.workflow_id)
print("Employee ID:", workflow.employee_id)
print("Status:", workflow.status)

print("\nTasks and dependencies:")

for task in tasks:
    print(
        task.task_name,
        "| Agent:", task.assigned_agent,
        "| Status:", task.status,
        "| Depends on:", task.depends_on
    )

db.close()