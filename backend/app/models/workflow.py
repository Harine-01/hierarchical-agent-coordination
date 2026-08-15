from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime

from app.database.base import Base


class Workflow(Base):
    __tablename__ = "workflows"

    workflow_id = Column(String, primary_key=True, index=True)
    employee_id = Column(
        String,
        ForeignKey("employees.employee_id"),
        nullable=False
    )
    workflow_type = Column(String, nullable=False)
    status = Column(String, default="PENDING")
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)