
# break: Stop at first even number 
print("break example:")
for num in [1, 3, 7, 4, 9, 2]:
    if num % 2 == 0:
        print(f"  First even number found: {num}")
        break
# Output: First even number found: 4

# continue: Skip odd numbers 
print("\ncontinue example (even numbers only):")
for num in range(1, 11):
    if num % 2 != 0:
        continue
    print(f"  {num}", end=" ")
# Output: 2 4 6 8 10

print()

# pass: Placeholder 
print("\npass example:")
for i in range(5):
    if i == 3:
        pass  # TODO: handle this case later
    else:
        print(f"  {i}", end=" ")
# Output: 0 1 2 4

print()

# for-else: Loop completed without break 
print("\nfor-else example (searching for 'Grape'):")
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    if fruit == "Grape":
        print(f"  Found {fruit}!")
        break
else:
    print("  Grape not found in the list.")
# Output: Grape not found in the list.