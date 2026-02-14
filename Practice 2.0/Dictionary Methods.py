# Creating a dictionary
person = {"name": "Chandu", "age": 30, "city": "NYC"}

# Accessing 
person.get("name")              # "Chandu" (returns None if key missing)
person.get("phone", "N/A")     # "N/A" (default if key missing)
person.keys()                   # dict_keys(["name", "age", "city"])
person.values()                 # dict_values(["Chandu", 30, "NYC"])
person.items()                  # dict_items([("name","Chandu"), ("age",30), ...])

# Adding / Updating 
person["email"] = "a@b.com"    # Add or overwrite a key
person.update({"age": 31, "phone": "123"})  # Merge another dict
person.setdefault("country", "US")  # Set only if key doesn't exist

# Removing 
person.pop("city")              # Remove key, return value (KeyError if missing)
person.pop("zip", None)        # Remove key, return default if missing
person.popitem()                # Remove and return last inserted (key, value)
person.clear()                  # Remove all items
del person["name"]              # Delete a specific key

# Copy 
p2 = person.copy()              # Shallow copy

# Creating from keys 
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)     # {"a": 0, "b": 0, "c": 0}

# Merging (Python 3.9+) 
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2                # {"a": 1, "b": 3, "c": 4}
d1 |= d2                       # In-place merge