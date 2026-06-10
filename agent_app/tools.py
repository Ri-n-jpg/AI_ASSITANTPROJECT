from datetime import datetime,date

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