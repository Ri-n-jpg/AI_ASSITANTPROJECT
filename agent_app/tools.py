from datetime import datetime,date
from .models import Note
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