#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      chand
#
# Created:     09-01-2024
# Copyright:   (c) chand 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Controle Statement :- \n")

numbers = [89, 108, 65, 87, 12, 108]

print("Numbers are : ",numbers)

# continue Statement skip the Specific Condition
for numbers in numbers :
    if numbers == 108 :
        continue;
    print(numbers)