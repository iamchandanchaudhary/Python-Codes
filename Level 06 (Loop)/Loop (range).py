## Syantax
range(stop)             # 0 to stop-1
range(start, stop)      # start to stop-1
range(start, stop, step) # start to stop-1, incrementing by step

# range(stop) → starts from 0 by default
print(list(range(5)))          # [0, 1, 2, 3, 4]

# range(start, stop)
print(list(range(2, 7)))       # [2, 3, 4, 5, 6]

# range(start, stop, step)
print(list(range(0, 10, 2)))   # [0, 2, 4, 6, 8]

# Negative step (counting backwards)
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]