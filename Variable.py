# Multiple assignment (same value)
a = b = c = 100

# Multiple assignment (different values)
x, y, z = 10, 20.5, "Hello"

# Swapping variables (Pythonic way!)
a, b = 1, 2
a, b = b, a   # Now a=2, b=1

# Dynamic typing — variable type can change
value = 10        # int
value = "Python"  # now it's a str

Data Types
├── Numeric
│   ├── int        → Whole numbers
│   ├── float      → Decimal numbers
│   └── complex    → Complex numbers
├── Boolean
│   └── bool       → True / False
├── Text
│   └── str        → Strings
├── Sequence
│   ├── list       → Ordered, mutable
│   ├── tuple      → Ordered, immutable
│   └── range      → Sequence of numbers
├── Set
│   ├── set        → Unordered, unique, mutable
│   └── frozenset  → Unordered, unique, immutable
├── Mapping
│   └── dict       → Key-value pairs
├── Binary
│   ├── bytes      → Immutable byte sequence
│   ├── bytearray  → Mutable byte sequence
│   └── memoryview → Memory view object
└── None
    └── NoneType   → Represents absence of value

import keyword
print(keyword.kwlist)
