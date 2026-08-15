from app.database.connection import engine
from app.database.base import Base

from app.models.employee import Employee
from app.models.workflow import Workflow
from app.models.task import Task
from app.models.task_result import TaskResult

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")
