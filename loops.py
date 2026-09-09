# while loop demo
# calculating average test score
# ℹ️ INFO: This program asks for test scores until the user types -1.
# It then calculates the average of all valid scores.

# 💡 TIP: A variable can act like a flag to control when a loop should stop.
score = 0  # flag
# ℹ️ INFO: These variables store the running total and number of valid scores.
total = 0
count = 0

# 💡 TIP: A while loop keeps repeating while the condition is True.
# ⚠️ WARNING: If the condition never becomes False, the loop can run forever.
while score >= 0:
    print("Enter each test score, enter -1 when done.")
    score = float(input("Enter the test score:  "))

    # ℹ️ INFO: We only count positive scores in the average.
    if score > 0:
        total += score  # shortcut for total = total + score
        count += 1
    elif score == -1:
        print("Entry completed")
    else:
        # ⚠️ WARNING: A negative number other than -1 is ignored to keep the program simple.
        print("Invalid score. Please enter a positive number or -1 to finish.")

# 💡 TIP: Average = total divided by how many scores were counted.
# ⚠️ WARNING: Never divide by zero. This check prevents that problem.
if count == 0:
    print("No valid scores were entered.")
else:
    average = total / count
    print(f"The average test score was: {average:,.1f}")

# 🔁 FOR LOOP PRACTICE
# ℹ️ INFO: range(1, 11) starts at 1 and stops before 11.
for x in range(1, 11):
    print(x)

# 💡 TIP: range(10, 0, -1) counts backward by 1 each time.
for y in range(10, 0, -1):
    print(y)

# ℹ️ INFO: A for loop is useful when we know how many times we want to repeat.
for day in (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
):
    print(day)

eat = False

# 💡 TIP: .lower() converts the user's input to lowercase.
# That means "YES", "Yes", and "yes" all become "yes".
# This helps us compare user input in a simple, consistent way.
# ℹ️ INFO: It is a string method, so it works on text input from input().
while not eat:
    feed = input("Can we eat now???  (yes/no)   ").lower()
    if feed == "yes":
        eat = True
