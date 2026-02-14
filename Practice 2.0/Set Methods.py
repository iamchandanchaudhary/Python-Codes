
# Creating a set
fruits = {"apple", "banana", "cherry"}

# --- Adding / Removing ---
fruits.add("orange")           # Add a single element
fruits.update(["mango", "grape"])  # Add multiple elements
fruits.remove("banana")        # Remove element (raises KeyError if missing)
fruits.discard("kiwi")         # Remove element (no error if missing)
fruits.pop()                   # Remove and return an arbitrary element
fruits.clear()                 # Remove all elements

# Set Operations 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.union(b)                     # {1, 2, 3, 4, 5, 6}       — a | b
a.intersection(b)              # {3, 4}                    — a & b
a.difference(b)                # {1, 2}                    — a - b
a.symmetric_difference(b)      # {1, 2, 5, 6}              — a ^ b

# Comparison 
a.issubset(b)                  # False — is a ⊆ b?
a.issuperset(b)                # False — is a ⊇ b?
a.isdisjoint(b)                # False — no common elements?

# In-place Operations 
a.intersection_update(b)       # a = a & b
a.difference_update(b)         # a = a - b
a.symmetric_difference_update(b)  # a = a ^ b

# Copy 
c = a.copy()                   # Shallow copy of the set