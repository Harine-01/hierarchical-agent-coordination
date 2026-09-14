from datetime import datetime


class Employee:
    def __init__(
        self,
        employee_id: str,
        employee_name: str,
        department: str,
        designation: str,
        joining_date: str,
        email: str
    ):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department = department
        self.designation = designation
        self.joining_date = joining_date
        self.email = email
        self.created_at = datetime.utcnow()