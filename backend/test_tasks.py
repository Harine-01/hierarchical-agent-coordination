from app.database.connection import SessionLocal
from app.database.crud import get_ready_tasks
from app.models.workflow import Workflow

db = SessionLocal()

workflow = db.query(Workflow).order_by(
    Workflow.created_at.desc()
).first()

ready_tasks = get_ready_tasks(
    db=db,
    workflow_id=workflow.workflow_id
)

print("Workflow:", workflow.workflow_id)
print("\nReady tasks:")

for task in ready_tasks:
    print(
        task.task_name,
        "->",
        task.assigned_agent,
        "->",
        task.status
    )

db.close()