import re

def validateEmail (email=None):

    pattern = re.compile("\w+@\w")

    if pattern.match(email): return True # Success

    return False # Unsuccess
