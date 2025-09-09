rows = int(input("enter the number of rows to print: "))
num = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1  
    print()  
