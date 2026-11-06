# Name: JAMES MICHAEL JUAREZ
# Assessment 3.2: Linear Data Structure

# ARRAY PROGRAM
# Adds every letter of a word into an array, then removes
# the letters one by one from the front until it is empty.

def show(arr):
    # turns the list into the format [A, B, C]
    return "[" + ", ".join(arr) + "]"

# Dynamic input (press Enter to use the default name)
word = input("Enter a word (example: JUAREZ): ").upper()
if word.strip() == "":
    word = "JAMES MICHAEL JUAREZ"

array = []

# ADD: put each letter into the array (spaces are skipped)
for letter in word:
    if letter != " ":
        array.append(letter)

print()
print("Add:", show(array))

# REMOVE: take out the first letter each time
while len(array) > 0:
    removed = array.pop(0)
    print(f"Remove {removed}: {show(array)}")

if len(array) == 0:
    print("Result: EMPTY")
