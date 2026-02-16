# Nested if Statement
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("You are allowed entry.")
    else:
        print("You need a valid ID to enter.")
else:
    print("You are underage. Entry denied.")
    