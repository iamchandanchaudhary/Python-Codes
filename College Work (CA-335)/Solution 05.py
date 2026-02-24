# Program to print unique words from a text file in alphabetical order

# ask user for file name
filename = input("Enter file name: ")

# open and read file
with open(filename, "r") as file:
    text = file.read()

# convert text to lowercase and split into words
words = text.lower().split()

# remove punctuation (basic cleaning)
clean_words = []
for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    clean_words.append(word)

# get unique words using set
unique_words = set(clean_words)

# sort words alphabetically
sorted_words = sorted(unique_words)

# print result
print("\nUnique words in alphabetical order:")
for w in sorted_words:
    if w:   # avoid empty strings
        print(w)