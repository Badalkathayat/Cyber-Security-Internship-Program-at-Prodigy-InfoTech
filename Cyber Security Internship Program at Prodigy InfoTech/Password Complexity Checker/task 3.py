import re

def check_password_strength(password):
    # Initialize the strength score
    score = 0
    feedback = []

    # Check the length of the password
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Avoid common passwords or patterns
    common_patterns = ['password', '123456', 'qwerty', 'abc123']
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Password contains common patterns or words.")
    else:
        score += 1

    # Provide feedback based on the score
    if score == 6:
        feedback.append("Your password is strong.")
    elif score >= 4:
        feedback.append("Your password is moderate.")
    else:
        feedback.append("Your password is weak.")

    return feedback

def main():
    while True:
        print("\nPassword Complexity Checker")
        password = input("Enter a password to check its strength (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Exiting the Password Complexity Checker. Goodbye!")
            break

        feedback = check_password_strength(password)
        print("\n".join(feedback))

if __name__ == '__main__':
    main()
