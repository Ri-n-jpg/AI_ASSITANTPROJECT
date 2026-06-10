from .tools import get_current_time, calculator
from .llm import get_llm_response


def process_query(question):

    question_lower = question.lower()

    # Time Tool
    if "time" in question_lower:
        return get_current_time()

    # Calculator Tool
    if any(op in question for op in ["+", "-", "*", "/"]):
        return calculator(question)

    # LLM
    return get_llm_response(question)