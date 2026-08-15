from pydantic import BaseModel
from datetime import date


class EmployeeOnboardingRequest(BaseModel):
    employee_name: str
    employee_id: str
    department: str
    designation: str
    joining_date: date
    email: str