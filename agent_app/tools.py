from datetime import datetime,date
from .models import Note, Task
from .models import Employee
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def get_current_date():
    return str(date.today())
def get_current_day():
    return datetime.now().strftime("%A")

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"
def add_note(text):
        note = Note.objects.create(content=text)
        return f"Note saved: {note.content}"
def get_notes():
        notes = Note.objects.all().order_by('-created_at')

        if not notes:
            return "No notes found"

        return "\n".join([f"{n.id}. {n.content}" for n in notes])


def add_employee(name, department, salary):
    try:
        employee = Employee.objects.create(
            name=name,
            department=department,
            salary=salary
        )

        return (
            f"Employee added successfully.\n"
            f"Name: {employee.name}\n"
            f"Department: {employee.department}\n"
            f"Salary: {employee.salary}"
        )

    except Exception as e:
        return f"Failed to add employee: {str(e)}"

def get_employees():
    employees = Employee.objects.all()

    if not employees:
        return "No employees found"

    return "\n".join([
        f"{e.id}. {e.name} - {e.department} - {e.salary}"
        for e in employees
    ])
def search_employee(name):
    employees = Employee.objects.filter(name__icontains=name)

    if not employees:
        return "Employee not found"

    return "\n".join([
        f"{e.id}. {e.name} - {e.department} - {e.salary}"
        for e in employees
    ])
def delete_employee(emp_id):
    try:
        employee = Employee.objects.get(id=emp_id)

        name = employee.name

        employee.delete()

        return f"Employee '{name}' deleted successfully."

    except Employee.DoesNotExist:
        return "Employee not found."

    except Exception as e:
        return f"Error: {str(e)}"

def add_task(title, priority="Medium"):
    try:
        task = Task.objects.create(
            title=title,
            priority=priority,
            status="Pending"
        )

        return (
            f"Task created successfully.\n"
            f"Title: {task.title}\n"
            f"Priority: {task.priority}\n"
            f"Status: {task.status}"
        )

    except Exception as e:
        return f"Failed to create task: {str(e)}"


def get_tasks():
    tasks = Task.objects.all().order_by("-created_at")

    if not tasks.exists():
        return "No tasks found."

    return "\n".join([
        f"{t.id}. {t.title} | Priority: {t.priority} | Status: {t.status}"
        for t in tasks
    ])


def get_pending_tasks():
    tasks = Task.objects.filter(status="Pending")

    if not tasks.exists():
        return "No pending tasks."

    return "\n".join([
        f"{t.id}. {t.title} | Priority: {t.priority}"
        for t in tasks
    ])


def get_completed_tasks():
    tasks = Task.objects.filter(status="Completed")

    if not tasks.exists():
        return "No completed tasks."

    return "\n".join([
        f"{t.id}. {t.title}"
        for t in tasks
    ])


def start_task(task_id):
    try:
        task = Task.objects.get(id=task_id)

        task.status = "In Progress"
        task.save()

        return f"Task '{task.title}' is now In Progress."

    except Task.DoesNotExist:
        return "Task not found."

    except Exception as e:
        return f"Error: {str(e)}"


def complete_task(task_id):
    try:
        task = Task.objects.get(id=task_id)

        task.status = "Completed"
        task.save()

        return f"Task '{task.title}' marked as completed."

    except Task.DoesNotExist:
        return "Task not found."

    except Exception as e:
        return f"Error: {str(e)}"


def delete_task(task_id):
    try:
        task = Task.objects.get(id=task_id)

        title = task.title
        task.delete()

        return f"Task '{title}' deleted successfully."

    except Task.DoesNotExist:
        return "Task not found."

    except Exception as e:
        return f"Error: {str(e)}"

def total_tasks():
    return f"Total tasks: {Task.objects.count()}"


def pending_task_count():
    count = Task.objects.filter(status="Pending").count()
    return f"Pending tasks: {count}"


def completed_task_count():
    count = Task.objects.filter(status="Completed").count()
    return f"Completed tasks: {count}"