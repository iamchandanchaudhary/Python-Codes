if 5 > 2:
    print("Five is greater than two!")  # This runs only if the condition is true
print("This runs no matter what.")      # This is OUTSIDE the block

if 5 > 2:
print("Five is greater than two!") 
# ERROR: IndentationError: expected an indented block

def check_numbers(numbers):
    # Level 1 Indentation (Inside function)
    for num in numbers:
        # Level 2 Indentation (Inside loop)
        if num > 0:
            # Level 3 Indentation (Inside if)
            print("Positive number")
        else:
            # Level 3 Indentation (Inside else)
            print("Negative number")
    # Back to Level 1
    print("Done checking.")