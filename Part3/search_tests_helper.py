import io
from search import display_result
import sys
from wiki import BASIC, ADVANCED, ADVANCED_TO_QUESTION 

def print_basic():
    """
    Returns string to ask user for basic search keyword
    """
    return BASIC

def print_advanced():
    """
    Returns string to ask user for advanced search option
    """
    return ADVANCED

def print_advanced_option(option):
    """
    Returns string to ask user for advanced search question
    """
    return ADVANCED_TO_QUESTION[option]

def _print_value(question, answer):
    print(question + answer)
    return answer

def get_print(input_mock, answers):
    """
    Mocks input and runs function with provided answers

    Args:
      input_mock - patched bultins.input()
      answers - desired input for builtins.input()
    """
    answers.reverse() # reverses answers so can pop off list
    input_mock.side_effect = \
        lambda question: _print_value(question, str(answers.pop())) # print input question along with given answer

    # Save printed output into variable so can return it to compare in test
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    display_result()
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return output # return printed statements in student-run code