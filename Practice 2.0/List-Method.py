
fruits = ["apple", "banana", "cherry"]

# Adding Elements
fruits.append("date")              # ['apple', 'banana', 'cherry', 'date']
fruits.insert(1, "blueberry")      # Insert at index 1
fruits.extend(["fig", "grape"])    # Add multiple elements

# Removing Elements
fruits.remove("banana")     # Remove first occurrence
popped = fruits.pop()       # Remove & return last element
popped = fruits.pop(1)      # Remove & return element at index 1
fruits.clear()               # Remove all elements

# Searching
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(nums.index(4))      # 2    (index of first occurrence)
print(nums.count(1))      # 2    (count occurrences)

# Ordering
nums.sort()                # Sort in place (ascending)
nums.sort(reverse=True)    # Sort in place (descending)
nums.reverse()             # Reverse in place

# Copying
copy1 = nums.copy()        # Shallow copy
copy2 = nums[:]            # Shallow copy (slice)
copy3 = list(nums)         # Shallow copy (constructor)

# Other useful built-in functions
print(len(nums))    # Length
print(min(nums))    # Minimum
print(max(nums))    # Maximum
print(sum(nums))    # Sum
print(sorted(nums)) # Returns new sorted list (original unchanged)