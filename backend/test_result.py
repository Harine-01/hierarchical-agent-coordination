from app.database.connection import SessionLocal
from app.database.crud import get_task_results
from app.models.workflow import Workflow
from app.models.task import Task

db = SessionLocal()

workflow = db.query(Workflow).order_by(
    Workflow.created_at.desc()
).first()

task = db.query(Task).filter(
    Task.workflow_id == workflow.workflow_id,
    Task.task_name == "HR Verification"
).first()

results = get_task_results(
    db=db,
    task_id=task.task_id
)

print("Task results:")

for result in results:
    print(
        "Result ID:", result.result_id,
        "| Result:", result.result,
        "| Error:", result.error
    )

db.close()