from .tools import (
    get_current_time,
    calculator,
    get_current_date,
    get_current_day,
    add_note,
    get_notes,
    add_employee,
    get_employees,
    search_employee,
    delete_employee,
    add_task,
    get_tasks,
    complete_task,
    delete_task,
get_pending_tasks,
    get_completed_tasks,
    start_task,
    total_tasks,
    pending_task_count,
    completed_task_count,
)

from .llm import get_llm_response
from .models import ChatHistory


# -----------------------------
# MAIN AGENT FUNCTION
# -----------------------------
def process_query(question):

    question_lower = question.lower()

    # ---------------- TIME ----------------
    if "time" in question_lower:
        return get_current_time()

    # ---------------- DATE ----------------
    if "date" in question_lower:
        return get_current_date()

    # ---------------- DAY ----------------
    if "day" in question_lower:
        return get_current_day()

    # ---------------- CALCULATOR ----------------
    if any(op in question for op in ["+", "-", "*", "/"]):
        return calculator(question)

    # ---------------- NOTES TOOL ----------------
    if question_lower.startswith("remember"):
        return add_note(question)

    if "show notes" in question_lower or "my notes" in question_lower:
        return get_notes()

    # ---------------- EMPLOYEE TOOL ----------------

    if question_lower.startswith("add employee"):
        try:
            parts = question.split()

            if len(parts) != 5:
                return (
                    "Invalid format.\n"
                    "Use: add employee <name> <department> <salary>"
                )

            name = parts[2]
            department = parts[3]
            salary = int(parts[4])

            return add_employee(name, department, salary)

        except ValueError:
            return "Salary must be a number."

        except Exception as e:
            return f"Error: {str(e)}"

    if "show employees" in question_lower:
        return get_employees()

    if question_lower.startswith("search employee"):
        name = question.replace("search employee", "").strip()
        return search_employee(name)

    if question_lower.startswith("delete employee"):
        try:
            emp_id = int(question.split()[-1])
            return delete_employee(emp_id)

        except ValueError:
            return "Employee ID must be a number."

        except Exception as e:
            return f"Error: {str(e)}"

    # ---------------- TASK TOOL ----------------

    # ---------------- TASK TOOL ----------------

    if question_lower.startswith("add task"):
        try:
            title = question.replace("add task", "").strip()

            if not title:
                return "Please provide a task title."

            return add_task(title)

        except Exception as e:
            return f"Error: {str(e)}"

    if "show tasks" in question_lower:
        return get_tasks()

    if "show pending tasks" in question_lower:
        return get_pending_tasks()

    if "show completed tasks" in question_lower:
        return get_completed_tasks()

    if question_lower.startswith("start task"):
        try:
            task_id = int(question.split()[-1])
            return start_task(task_id)

        except ValueError:
            return "Task ID must be a number."

    if question_lower.startswith("complete task"):
        try:
            task_id = int(question.split()[-1])
            return complete_task(task_id)

        except ValueError:
            return "Task ID must be a number."

    if question_lower.startswith("delete task"):
        try:
            task_id = int(question.split()[-1])
            return delete_task(task_id)

        except ValueError:
            return "Task ID must be a number."

    # ---------------- TASK ANALYTICS ----------------

    if "total tasks" in question_lower:
        return total_tasks()

    if "pending task count" in question_lower:
        return pending_task_count()

    if "completed task count" in question_lower:
        return completed_task_count()

    if "how many tasks are pending" in question_lower:
        return pending_task_count()

    if "how many tasks are completed" in question_lower:
        return completed_task_count()

    # ---------------- MEMORY ----------------
    memory = get_chat_memory()

    final_prompt = f"""
Previous conversation:
{memory}

User: {question}
AI:
"""

    return get_llm_response(final_prompt)


# -----------------------------
# MEMORY FUNCTION
# -----------------------------
def get_chat_memory(limit=5):
    chats = ChatHistory.objects.all().order_by('-created_at')[:limit]

    memory = ""
    for chat in reversed(chats):
        memory += f"User: {chat.question}\nAI: {chat.answer}\n"

    return memory