text = "  Hello, Chandan!  "

# Case Methods
print(text.upper())        # "  HELLO, Chandan!  "
print(text.lower())        # "  hello, Chandan!  "
print(text.title())        # "  Hello, Chandan!  "
print(text.capitalize())   # "  hello, Chandan!  "
print(text.swapcase())     # "  hELLO, Chandan!  "

# Search Methods
print(text.find("Chandan"))       # 9
print(text.index("Chandan"))      # 9
print(text.count("l"))          # 3
print(text.startswith("  He"))  # True
print(text.endswith("!  "))     # True


# Modification Methods
print(text.strip())        # "Hello, Chandan!"
print(text.lstrip())       # "Hello, Chandan!  "
print(text.rstrip())       # "  Hello, Chandan!"
print(text.replace("Chandan", "Python"))  # "  Hello, Python!  "

# Split & Join
print("a,b,c".split(","))       # ['a', 'b', 'c']
print("-".join(["a", "b", "c"]))  # "a-b-c"

# Validation Methods
print("hello".isalpha())    # True
print("123".isdigit())      # True
print("hello123".isalnum()) # True
print("   ".isspace())      # True