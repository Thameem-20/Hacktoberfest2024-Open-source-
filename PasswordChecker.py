import re

# Function to check the password strength
def check_password_strength(password):
    # Length check
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Complexity checks
    strength_criteria = [
        bool(re.search(r'[A-Z]', password)),  # At least one uppercase letter
        bool(re.search(r'[a-z]', password)),  # At least one lowercase letter
        bool(re.search(r'[0-9]', password)),  # At least one digit
        bool(re.search(r'[@$!%*?&#]', password))  # At least one special character
    ]

    # Count how many of the criteria are met
    strength_score = sum(strength_criteria)

    # Determine password strength based on score
    if strength_score == 4:
        return "Strong: Your password is secure!"
    elif strength_score == 3:
        return "Moderate: Consider adding more complexity."
    else:
        return "Weak: Your password is too simple."

# Test the function
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(strength)
