"""
Python switch/case demo.

Python uses match/case (Python 3.10+) instead of a traditional switch statement.
"""


# ℹ️ A function groups code so we can use it again.
# ℹ️ "month" is a parameter: it receives a value when the function is called.
def holiday_for_month(month):
    """Return a representative U.S. holiday or observance for a month."""
    # ℹ️ match works like a switch statement in other programming languages.
    # 💡 .lower() changes text to lowercase, so "January" and "january" both work.
    # ⚠️ month must be a string because .lower() only works with text.
    match month.lower():
        # ℹ️ Each case checks whether the month matches this text.
        # 🦗 Common bug: case statements must be indented under match.
        case "january":
            # ℹ️ return sends a value back to where the function was called.
            return "New Year's Day and Martin Luther King Jr. Day"
        case "february":
            return "Presidents Day"
        case "march":
            return "St. Patrick's Day"
        case "april":
            return "Earth Day"
        case "may":
            return "Memorial Day"
        case "june":
            return "Juneteenth"
        case "july":
            return "Independence Day"
        case "august":
            return "No federal holiday"
        case "september":
            return "Labor Day"
        case "october":
            return "Halloween"
        case "november":
            return "Thanksgiving"
        case "december":
            return "Christmas Day"
        # ℹ️ _ means "anything else". It is the default case.
        case _:
            return "Please enter a full month name."

    # ℹ️ A list stores several values in one variable.
    # 💡 Try changing or adding month names to see different cases run.


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# ℹ️ This loop runs once for every item in the months list.
# ℹ️ During each loop, month holds one month name from the list.
for month in months:
    # ℹ️ An f-string lets us put variable values inside a string using {}.
    print(f"{month}: {holiday_for_month(month)}")
