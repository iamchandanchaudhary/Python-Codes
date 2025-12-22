#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chand
#
# Created:     09-01-2024
# Copyright:   (c) chand 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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