
import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if not (use_upper or use_lower or use_digits or use_special):
        return "Error: At least one character type must be selected."

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated Password:")
    print(generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True))
