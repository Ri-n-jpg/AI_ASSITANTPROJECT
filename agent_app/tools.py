from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"