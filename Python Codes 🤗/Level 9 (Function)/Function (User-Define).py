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

print("Function(User-Define) :- \n")

def print_sum(first, second) :
    print("Their Sum : ",first + second)

print_sum(4, 11)

def print_multiply(first, second = 5) :
    print("Their Multiply : ", first * second)

print_multiply(12)