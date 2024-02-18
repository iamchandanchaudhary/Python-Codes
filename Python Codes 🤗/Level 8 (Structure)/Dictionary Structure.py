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

print("Dictionary :- \n")

marks = {"maths" : 97, "english" :  95, "physics" : 98}

print(marks)

# you can print single index
print("Physics marks : ",marks["physics"])

# You can Add new Index
marks["GK"] = 98
print(marks)

# you can change the index value
marks["GK"] = 99
print(marks)

marks["maths"] = 99
print(marks)