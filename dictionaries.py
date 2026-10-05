# Dictionaries
# you are allowed to use AI to fill dictionaries with data, add a comment to say you did

import random

# Created with AI assistance.
french_numbers = {
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
    10: "dix",
}

quiz = list(french_numbers.items())
random.shuffle(quiz)
quiz_questions = dict(quiz)
# ℹ️ INFO: The in operator checks a dictionary's KEYS, not its values.
# 💡 TIP: 6 is a key in french_numbers, so this prints "Found!".
# Checking for "six" this way would say "Not Found" because "six" is a value.
if 6 in french_numbers:
    print("Found! ")
else:
    print("Not Found")

# ℹ️ INFO: Square brackets look up a value using its key: dictionary[key].
# 💡 TIP: We give it the key 3 and it gives back the value "trois".
print(french_numbers[3])

# ℹ️ INFO: Assigning with dictionary[key] = value creates a new pair or updates an existing one.
# 💡 TIP: If the key already exists, its value is replaced. If not, the pair is added.
# ⚠️ WARNING: Assignment uses =, not a colon. The colon below only annotates the
# expression and does NOT add anything, so 11 is never added to the dictionary.
# The working version is: french_numbers[11] = "onze"
french_numbers[11]: "onze"

# ℹ️ INFO: pop(key) removes the pair with that key and returns its value.
# ⚠️ WARNING: pop() raises a KeyError if the key is missing. Our keys start at 1,
# so pop(0) would fail. That is why it is commented out.
# french_numbers.pop(0)

# ⚠️ WARNING: Looking up a key that does not exist raises a KeyError.
# 💡 TIP: A try/except lets the program recover instead of crashing.
try:
    print(french_numbers[14])
except KeyError:
    print("That is not in our dictionary")

# ℹ️ INFO: get(key) is a safer lookup. It returns None instead of raising a KeyError.
# 💡 TIP: get(key, "default") returns your own fallback value when the key is missing.
answer = french_numbers.get(12)
 print(answer)


# Quiz
correct = 0
incorrect = 0
for key, value in quiz_questions.items():
    answer = int(input(f"Please enter the numeric value for {value}:  "))
    if answer == key:
        print("correct")
        correct += 1
    else:
        print("incorrect")
        incorrect += 1

score = correct / 10
print(f"Score:  {score:,.1f}")
