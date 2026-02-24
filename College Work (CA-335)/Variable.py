# Program to demonstrate different sequence data types in Python

# 1. String (str) - sequence of characters
print("STRING:")
text = "Hello Python"
print("String:", text)
print("First character:", text[0])
print("Sliced string (0-5):", text[0:5])

# 2. List - mutable sequence
print("\nLIST:")
my_list = [10, 20, 30, 40, 50]
print("List:", my_list)
my_list.append(60)  # modifying list
print("List after append:", my_list)
print("First element:", my_list[0])

# 3. Tuple - immutable sequence
print("\nTUPLE:")
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("Second element:", my_tuple[1])

# 4. Range - sequence of numbers
print("\nRANGE:")
r = range(1, 6)
print("Range object:", r)
print("Range converted to list:", list(r))

# Common operations on sequences
print("\nCOMMON OPERATIONS:")
print("Length of string:", len(text))
print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))
print("Is 30 in list?", 30 in my_list)

# Iterating through a range sequence
print("Iterating through range:", end=" ")
for num in r:
    print(num, end=" ")
print("\n")