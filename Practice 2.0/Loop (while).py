
# Basic Counting 
print("Counting 1 to 5:")
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
# Output: 1 2 3 4 5

print()

# Sum until threshold 
print("\nAdding numbers until sum >= 50:")
total = 0
number = 1
while total < 50:
    total += number
    number += 1
print(f"Sum = {total}, Last number added = {number - 1}")
# Output: Sum = 55, Last number added = 10

# User Input Simulation 
print("\nPassword checker:")
password = ""
attempts = 0
correct_password = "python123"

# Simulating attempts
passwords_tried = ["hello", "admin", "python123"]
while attempts < len(passwords_tried):
    password = passwords_tried[attempts]
    attempts += 1
    if password == correct_password:
        print(f"  ✅ Access granted on attempt {attempts}!")
        break
    else:
        print(f"  ❌ Attempt {attempts}: Wrong password '{password}'")
