def my_function():
    x = 10   # local variable
    print(x)

my_function()
# print(x) ❌ Error (x is not accessible outside)

x = 20  # global variable

def my_function():
    print(x)

my_function()
print(x)
