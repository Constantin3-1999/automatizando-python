import re

def password_strength(password):
    # Check the length of password
    if len(password) < 8:
        return False
    
    # Check if password has at least one lowercase letter, one uppercase letter, and one digit
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    
    # Check if password has special characters
    if not re.search("[!@#$%^&*]", password):
        return False

    return True

password = input("Enter a password: ")
if password_strength(password):
    print("Password is strong")
else:
    print("Password is weak")
