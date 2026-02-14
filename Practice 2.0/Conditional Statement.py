# if Statement
age = 18

if age >= 18:
    print("You are eligible to vote.")

# if-else Statement
age = 15

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")
    
# if-elif-else Statement (if-elseif-else)
marks = 75

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

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
    