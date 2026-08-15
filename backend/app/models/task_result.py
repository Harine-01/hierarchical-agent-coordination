from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime

from app.database.base import Base


class TaskResult(Base):
    __tablename__ = "task_results"

    result_id = Column(String, primary_key=True, index=True)

    task_id = Column(
        String,
        ForeignKey("tasks.task_id"),
        nullable=False
    )

    result = Column(String, nullable=True)
    error = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)