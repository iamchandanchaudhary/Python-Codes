#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chand
#
# Created:     07-01-2024
# Copyright:   (c) chand 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Chandan Chaudhary Presents :- \n")

name = "Kailash"

print(name)

# Making Upper & Lower case
print(name.upper())
print(name.lower())

# findind String position
print(name.find('l'))
print(name.find("lash"))

# String Replacing (it  can Character / Full String)
print(name.replace("Kailash", "Bholenath"))

print(name)
print(name.replace('a','e'))

# String present or Not
# Present ==> True
# Absent ==> False
print('a' in name)
print("ash" in name)
print("kailash" in name)
print('A' in name)

print("\nThank you :)")