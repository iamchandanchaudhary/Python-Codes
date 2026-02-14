name = "Chandu"
age = 30
money = 49.99

# 1. f-strings (Python 3.6+) Recommended
print(f"Name: {name}, Age: {age}")
print(f"money: {money:.2f}")           # money: 49.99
print(f"{'Center':^20}")               # "       Center       "
print(f"{name!r}")                     # 'Chandu' (repr)

# 2. .format() method
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# 3. % operator (old style)
print("Name: %s, Age: %d" % (name, age))
print("money: %.2f" % money)

# 4. Template strings
from string import Template
t = Template("Hello, $name!")
print(t.substitute(name="Chandu"))  # Hello, Chandu!