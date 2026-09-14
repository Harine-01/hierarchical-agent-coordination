import uuid


def create_employee(
    db,
    employee_id: str,
    employee_name: str,
    department: str,
    designation: str,
    joining_date: str,
    email: str
):
    employee = {
        "employee_id": employee_id,
        "employee_name": employee_name,
        "department": department,
        "designation": designation,
        "joining_date": joining_date,
        "email": email
    }

    db.employees.insert_one(employee)

    return employee


def get_employee(db, employee_id: str):
    return db.employees.find_one(
        {"employee_id": employee_id},
        {"_id": 0}
    )


def create_workflow(
    db,
    employee_id: str,
    workflow_type: str = "EMPLOYEE_ONBOARDING"
):
    workflow = {
        "workflow_id": str(uuid.uuid4()),
        "employee_id": employee_id,
        "workflow_type": workflow_type,
        "status": "PENDING"
    }

    db.workflows.insert_one(workflow)

    return workflow


def create_onboarding_tasks(
    db,
    workflow_id: str
):
    hr_task_id = str(uuid.uuid4())

    tasks = [
        {
            "task_id": hr_task_id,
            "workflow_id": workflow_id,
            "task_name": "HR Verification",
            "assigned_agent": "HR_AGENT",
            "status": "PENDING",
            "depends_on": None
        },
        {
            "task_id": str(uuid.uuid4()),
            "workflow_id": workflow_id,
            "task_name": "IT Account Setup",
            "assigned_agent": "IT_AGENT",
            "status": "PENDING",
            "depends_on": hr_task_id
        },
        {
            "task_id": str(uuid.uuid4()),
            "workflow_id": workflow_id,
            "task_name": "Payroll Setup",
            "assigned_agent": "FINANCE_AGENT",
            "status": "PENDING",
            "depends_on": hr_task_id
        },
        {
            "task_id": str(uuid.uuid4()),
            "workflow_id": workflow_id,
            "task_name": "Asset Allocation",
            "assigned_agent": "ADMIN_AGENT",
            "status": "PENDING",
            "depends_on": hr_task_id
        }
    ]

    db.tasks.insert_many(tasks)

    return tasks


def get_ready_tasks(
    db,
    workflow_id: str
):
    pending_tasks = list(
        db.tasks.find(
            {
                "workflow_id": workflow_id,
                "status": "PENDING"
            },
            {"_id": 0}
        )
    )

    ready_tasks = []

    for task in pending_tasks:
        if task["depends_on"] is None:
            ready_tasks.append(task)
            continue

        dependency = db.tasks.find_one(
            {"task_id": task["depends_on"]},
            {"_id": 0}
        )

        if dependency and dependency["status"] == "COMPLETED":
            ready_tasks.append(task)

    return ready_tasks


def update_task_status(
    db,
    task_id: str,
    status: str
):
    result = db.tasks.update_one(
        {"task_id": task_id},
        {"$set": {"status": status}}
    )

    if result.matched_count == 0:
        return None

    return db.tasks.find_one(
        {"task_id": task_id},
        {"_id": 0}
    )


def create_task_result(
    db,
    task_id: str,
    result: str = None,
    error: str = None
):
    task_result = {
        "result_id": str(uuid.uuid4()),
        "task_id": task_id,
        "result": result,
        "error": error
    }

    db.task_results.insert_one(task_result)

    return task_result


def get_task_results(
    db,
    task_id: str
):
    return list(
        db.task_results.find(
            {"task_id": task_id},
            {"_id": 0}
        )
    )


def get_workflow_tasks(
    db,
    workflow_id: str
):
    return list(
        db.tasks.find(
            {"workflow_id": workflow_id},
            {"_id": 0}
        )
    )