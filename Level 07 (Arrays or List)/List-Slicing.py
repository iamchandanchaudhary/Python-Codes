
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:6])      # [2, 3, 4, 5]
print(nums[:4])        # [0, 1, 2, 3]
print(nums[5:])        # [5, 6, 7, 8, 9]
print(nums[::2])       # [0, 2, 4, 6, 8]     (every 2nd)
print(nums[::-1])      # [9, 8, 7, ..., 0]    (reversed)
print(nums[1:8:3])     # [1, 4, 7]            (step of 3)

# Slice assignment
nums[2:5] = [20, 30, 40]
print(nums)  # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]
