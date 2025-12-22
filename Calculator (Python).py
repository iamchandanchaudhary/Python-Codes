#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chand
#
# Created:     08-01-2024
# Copyright:   (c) chand 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Calculator : \n")

first = input("Enter 1st Number : ")
operator = input("Enter Operator (+,-,*,/,%) : ")
second = input("Enter Second Number : ")

first = int(first)
second = int(second)

print()

if operator == "+" :
    print("Their Sum : ", first + second)

elif operator == "-" :
    print("Their Subtraction : ", first - second)

elif operator == "*" :
    print("Their Multipication : ", first * second)

elif operator == "/" :
    print("Their Division : ", first / second)

elif operator == "%" :
    print("Their Remainder : ", first % second)

else :
    print("Invalid Operator :( ")

print("Thank You :)")