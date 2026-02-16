
# Iterating with range()
print("Numbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
# Output: 1 2 3 4 5

print()

# Iterating over a List
fruits = ["Apple", "Banana", "Cherry", "Mango"]
print("\nFruits:")
for fruit in fruits:
    print(f"{fruit}")


# Iterating over a String
print("\nLetters in 'Python':")
for char in "Python":
    print(char, end=" ")
# Output: P y t h o n

print()

# Using enumerate() for index + value
colors = ["Red", "Green", "Blue"]
print("\nColors with index:")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")
