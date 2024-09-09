from itertools import product

import string
import time

print("Type password")
password = input().strip()
passlen = len(password)

def passwordcracker(password, passlen):
    attempts = 0

    # Prompt user for choice of character set
    print("Use a custom file with key characters or standard ASCII? Type 1 for custom file or 2 for ASCII.")
    while True:
        try:
            utchoice = int(input())
            if utchoice in [1, 2]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Please enter a valid number (1 or 2).")

    # Custom file option
    if utchoice == 1:
        text = input("Type file's name. Make sure it's in the same folder as the .py").strip()
        try:
            with open(text, "r", encoding='utf-8') as file:
                data = file.read()
        except FileNotFoundError:
            return "File not found. Please ensure it's in the same folder as the .py."

        # Prompt for splitting method
        print("Split by line (1) or custom separator (2)?")
        while True:
            try:
                marchoice = int(input())
                if marchoice in [1, 2]:
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Please enter a valid number (1 or 2).")

        if marchoice == 1:
            data = data.splitlines()  # Split by line
        else:
            print("Type the custom separator")
            separator = input().strip()
            data = data.split(separator)  # Split by custom separator

    # Standard ASCII option
    else:
        data = string.ascii_lowercase + string.digits + string.ascii_uppercase

   
    # Start timing the cracking process
    start = time.time()

    # Attempt to brute-force the password
    for attempt in product(data,repeat=passlen ):
        attempts += 1
        possibility = ''.join(attempt)

        if possibility == password:
            end = time.time()
            return "I found your password '{}' in {} attempts and in {:.2f} seconds".format(password, attempts, end - start)

    return "Password not found."

# Call the function and print the result
if __name__ == "__main__":
    print(passwordcracker(password, passlen))
