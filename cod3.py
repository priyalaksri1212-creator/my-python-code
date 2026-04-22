import random
import string

def generate_password(length):
    # All possible characters: letters + digits + symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("===== PASSWORD GENERATOR =====")
    
    # Ask user for password length
    length = int(input("Enter the desired password length: "))
    
    if length < 6:
        print("Password too short! Minimum length is 6.")
    else:
        password = generate_password(length)
        print(f"\n Your generated password is:\n{password}")

main()