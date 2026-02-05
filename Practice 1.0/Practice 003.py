print("Calculator :- \n")

a = input("Enter 1st Value : ")
operator = input("Enter Operator (+,-,*,/,%) : ")
b = input("Enter 2nd Value : ")

a = int(a)
b = int(b)

print()
if operator == '+' :
    print("Their Sum : ", a + b)

elif operator == '-' :
    print("Their Substraction : ", a - b)

elif operator == '*' :
    print("Their Multiply : ", a * b)

elif operator == '/' :
    print("Their Division : ", a / b)


elif operator == '%' :
    print("Their Remainder : ", a % b)

else :
    print("Invalid Operator :(")

print("Thank you :)")