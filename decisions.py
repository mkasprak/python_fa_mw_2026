# ℹ️ Operators and decision statements

# answer = int(input("Enter a number between 1 and 100:  "))

# 💡 An if statement lets a program choose what to do based on a condition.
# ℹ️ == means "is equal to". It compares two values.
# if answer == 42:
#     print("You found the answer to life, the universe and everything")
# else:
# print("Sorry. Talk to the white mice.")

# ℹ️ input() gives us text, so float() converts the score to a number.
# ⚠️ Enter a numeric value such as 90 or 90.5, or float() will cause an error.
print("Scores must be numeric: 90   90.5")
score = float(input("Please enter your test score:  "))

# ℹ️ Python checks conditions from top to bottom.
# ⚠️ Put the highest score range first. A score of 95 is also greater than 80.
if score > 90.0:
    print("A")
# ℹ️ elif means "else if": it is checked only when the earlier condition was False.
elif score > 80.0:
    print("B")
elif score > 70.0:
    print("C")
elif score > 60.0:
    print("D")
# ℹ️ else runs when none of the conditions above are True.
else:
    print("F")

# ℹ️ match/case is another way to make a decision.
# 💀⚡ Strings are case sensitive: "May" and "may" are different text values.
# 💡 .lower() changes the user's answer to lowercase before matching it.

current_month = input("What Month is it? (spell out full):")

# ℹ️ match compares the value in parentheses to each case below.
match current_month.lower():
    # ℹ️ A case runs when its text matches the user's month.
    # 🦗 Common bug: case statements must be indented under match.
    case "january":
        # ℹ️ print displays the holiday on the screen.
        print("New Year's Day and Martin Luther King Jr. Day")
    case "february":
        print("Presidents Day")
    case "march":
        print("St. Patrick's Day")
    case "april":
        print("Earth Day")
    case "may":
        print("Memorial Day")
    case "june":
        print("Juneteenth")
    case "july":
        print("Independence Day")
    case "august":
        print("No federal holiday")
    case "september":
        print("Labor Day")
    case "october":
        print("Halloween")
    case "november":
        print("Thanksgiving")
    case "december":
        print("Christmas Day")
    # ℹ️ _ means "anything else". It is the default case.
    # 💡 Include a default case to handle an unexpected answer.
    case _:
        print("Please enter a full month name.")
