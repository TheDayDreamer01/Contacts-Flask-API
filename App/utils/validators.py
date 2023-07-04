import re


def isValidEmail(email : str) -> bool:
    PATTERN : str = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(PATTERN, email)