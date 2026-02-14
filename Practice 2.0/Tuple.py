## Creating Tuples

# Empty tuple
empty_tuple = ()

# Tuple with elements
fruits = ("apple", "banana", "cherry")

# Tuple without parentheses (tuple packing)
colors = "red", "green", "blue"

# Single element tuple (note the trailing comma!)
single = ("hello",)

# Using the tuple() constructor
numbers = tuple([1, 2, 3, 4, 5])

# Nested tuple
nested = (1, (2, 3), (4, 5, 6))

## Accessing Elements
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Indexing
print(fruits[0])      # apple
print(fruits[-1])     # elderberry

# Slicing
print(fruits[1:3])    # ('banana', 'cherry')
print(fruits[:3])     # ('apple', 'banana', 'cherry')
print(fruits[2:])     # ('cherry', 'date', 'elderberry')
