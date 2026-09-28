"""
All about strings! 🧵🪕🎸

Strings are sequences of text. This lesson explores joining, inspecting,
cleaning, splitting, and looping through strings.
"""

# ℹ️ A string is text surrounded by quotation marks.
names = "Meri"

new_name = "Louise"

# 💡 The + operator concatenates (joins) strings and stores the result.
names = names + new_name

print(names)

# 💡 Multiplying a string repeats its contents.
print("*" * 50)

# ℹ️ len() counts the characters in a string; indexes start at 0.
print(len(names))

# ℹ️ Use square brackets and an index to get one character.
print(names[5])
# 💡 \n makes a new line and \t adds a tab.
print(f"\n\n - 2 blank lines \n \ttab")

# ℹ️ strip() removes surrounding whitespace; title() capitalizes each word.
my_name = "    meri    kasprak    "
print(my_name.strip().title())

# ℹ️ split() breaks a string into a list of smaller strings.
greeting = "Hello World"

words = greeting.split(" ")
print(words)
# 💡 A for loop can visit each word in the resulting list.
for word in words:
    print(word)

# ℹ️ isdigit() checks whether every character is a digit.
print("Is Digit?")
print("123".isdigit())
print("123.4".isdigit())

# ℹ️ isalpha() checks whether every character is a letter (no spaces or punctuation).
print("Is Alpha")
print("Python".isalpha())
print("Python!".isalpha())

# 🐕 Strings are iterable, so this loop runs once for each character in "BINGO".
name_string = "BINGO"
dog_letters = list(name_string)
count = 0

for char in name_string:
    current_name = " ".join(dog_letters)

    print("There was a farmer who had a dog and Bingo was his Name-o")
    # 💡 Repeating this formatted string prints the chorus three times.
    print(f"({current_name}) \n" * 3)
    print("and Bingo was his Nam-o\n")
    # 💡 Replace the next letter with a dog emoji as the loop progresses.
    dog_letters[count] = "🐕 "
    count += 1
# ℹ️ Join the updated character list into the final string.
final_name = " ".join(dog_letters)
print(f"({final_name}) \n" * 3)
print("and Bingo was his name-o!")
