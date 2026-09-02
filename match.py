"""
Python switch/case demo.

Python uses match/case (Python 3.10+) instead of a traditional switch statement.
"""

# ℹ️ Ask the user for a month name and store the answer in a variable.
user_month = input("Enter a month name: ")

# ℹ️ match compares the value in parentheses to each case below.
# 💡 .lower() changes text to lowercase, so "January" and "january" both work.
# 🦗 Common bug: case statements must be indented under match.
match user_month.lower():
    case "january":
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
    case _:
        print("Please enter a full month name.")
