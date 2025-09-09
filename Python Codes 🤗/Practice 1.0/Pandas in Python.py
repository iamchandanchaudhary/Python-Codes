import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)

print(df)

# Access a column
print(df['Name'])

# Filtering
print(df[df['Age'] > 23])

# Descriptive statistics
print(df.describe())
