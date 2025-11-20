import re

# Load the 1000 common leaked passwords
with open("common-passwords.txt") as f:
    COMMON = set(line.strip() for line in f)

def validate_password(pw: str) -> bool:
    # Requirement 1: length >= 8
    if len(pw) < 8:
        return False

    # Requirement 2: contain uppercase, lowercase, digit, special char
    if not re.search(r"[A-Z]", pw):
        return False
    if not re.search(r"[a-z]", pw):
        return False
    if not re.search(r"\d", pw):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
        return False

    # Requirement 3: not in top-1000 common list
    if pw.lower() in COMMON:
        return False

    return True
