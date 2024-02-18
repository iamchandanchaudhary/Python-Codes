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

print("Performing Operation on List :- \n")

marks = [89, 87, 94, 97]

print("Length of List : ",len(marks))

print("At normal : ",marks)

marks.append(99)

print("After append : ",marks)

marks.insert(0, 88)
print("After inser at Index[0] : ",marks)
print("Length of List : ",len(marks))

print("\nCheking Value Present or not :-")
print(99 in marks)
print(98 in marks)