from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime

from app.database.base import Base


class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(String, primary_key=True, index=True)

    workflow_id = Column(
        String,
        ForeignKey("workflows.workflow_id"),
        nullable=False
    )

    task_name = Column(String, nullable=False)
    assigned_agent = Column(String, nullable=False)
    status = Column(String, default="PENDING")
    depends_on = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)