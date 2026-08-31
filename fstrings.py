"""
fstring formatting in Python-
this makes it easier to use variables, format numbers, left align, right align
etc. there is a Python F-String cheat sheet in module 0
"""

# ℹ️ fstrings for variables

name = "Meri"
age = 55

# 👤 Standard f-string: embeds variables directly into the string using curly braces {}
# 🔄 You can also perform inline math calculations inside the braces!
print(f"{name} is {age} and will be {age + 1} next year.")


# ➡️ ⬅️ Alignment
# 🔢 the number after the colon and symbol is your column width

# ⬅️ Left-aligned within a width of 30 characters
print(f"{name:<30}")
# ➡️ Right-aligned within a width of 30 characters
print(f"{name:>30}")
# ↔️ Centered within a width of 30 characters
print(f"{name:^30}")

# ℹ️ line below is creating two columns 30 wide centering name and age
# 📊 Two centered columns of 30 width side-by-side
print(f"{name:^30} {age:^30}")

score_1 = 1088
score_2 = 1073
score_3 = 1065

average = (score_1 + score_2 + score_3) / 3

print(average)

# # 🔢 Number Formatting
# ℹ️ f-string formatting options come after a colon : inside the braces

# 🎯 `,` inserts thousand separators (commas)
# 🎯 `.0f` rounds to 0 decimal places and displays as a float
print(f"{average: ,.0f}")

distance_to_monroe = 852
distance_to_phoenix = 1712

# 📍 Distance formatting using leading space, comma separator, and zero decimal rounding
print(f"Distance to Monroe, North Carolina{distance_to_monroe: ,.0f}")
print(f"Distance to Phoenix, Arizona{distance_to_phoenix: ,.0f}")


current_mort_rate = 0.0675
# # 📈 Percentage Formatting
# 🎯 `.%` multiplies the decimal by 100 and adds the percentage symbol %
# 🎯 `.2%` formats the number with exactly 2 decimal places
print(f"Mortgage rate = {current_mort_rate:.2%}")


# # ⭐️ Additional Helpful F-string Formatting Techniques ⭐️

# 🔍 Debugging Mode (=): prints both the expression/variable name and its evaluated value (Python 3.8+)
print(f"{name=}")
print(f"{age=}")

# 💵 Currency formatting: combines a currency symbol with comma separators and 2 decimal float precision
average_cost = 1075.3333
print(f"Average cost: ${average_cost:,.2f}")

# 0️⃣ Leading Zero Padding: pads numbers with zeros to a specific total width (e.g., 6 digits wide)
print(f"Padded Score: {score_1:06d}")

# 📅 Date and Time formatting (using Python's datetime module)
from datetime import datetime

now = datetime.now()
# 🕒 `%B` = Full month, `%d` = Day, `%Y` = Year, `%I:%M %p` = 12-hour clock with AM/PM
print(f"Current Date/Time: {now:%B %d, %Y - %I:%M %p}")
