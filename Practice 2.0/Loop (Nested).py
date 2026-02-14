# Multiplication Table (1 to 5) 
print("Multiplication Table (1-5):\n")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i:>2} x {j:>2} = {i*j:>3}", end="   ")
    print()  # New line after each row

print()

# Star Pattern: Right Triangle 
print("Right Triangle Pattern:")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# Star Pattern: Pyramid 
print("Pyramid Pattern:")
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

print()

# Star Pattern: Inverted Triangle 
print("Inverted Triangle Pattern:")
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# Matrix (2D List) Traversal 
print("Matrix Traversal:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(f"{element:>3}", end=" ")
    print()
    