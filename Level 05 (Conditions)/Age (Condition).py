print("Conditional Statement :- \n")

age = input("Enter your age : ")

age = int(age)

if age >= 18 and age <= 100:
    print("He is Adult")

elif age < 18 and age >= 13:
    print("He is Teeganer")

elif age < 13  and age >= 0:
    print("He is Child")

else:
    print("Invalid Age :(")

print("\nThank You :)")