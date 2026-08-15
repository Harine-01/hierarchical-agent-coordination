from app.database.connection import SessionLocal
from app.database.crud import update_task_status, get_ready_tasks
from app.models.workflow import Workflow
from app.models.task import Task

db = SessionLocal()

workflow = db.query(Workflow).order_by(
    Workflow.created_at.desc()
).first()

hr_task = db.query(Task).filter(
    Task.workflow_id == workflow.workflow_id,
    Task.task_name == "HR Verification"
).first()

updated_task = update_task_status(
    db=db,
    task_id=hr_task.task_id,
    status="COMPLETED"
)

print("Updated task:")
print(
    updated_task.task_name,
    "->",
    updated_task.status
)

ready_tasks = get_ready_tasks(
    db=db,
    workflow_id=workflow.workflow_id
)

print("\nReady tasks after HR completion:")

for task in ready_tasks:
    print(
        task.task_name,
        "->",
        task.assigned_agent,
        "->",
        task.status
    )

db.close()