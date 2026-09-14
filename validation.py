"""
Error checking data entry with while statements
"""

# ℹ️ INFO: This program checks user input before accepting it.
# It uses while loops to keep asking when an entry is invalid.

# 📝 NAME CHECK

# ℹ️ Rules for the first name:
# - It cannot be empty.
# - It should be less than 30 characters.
# - Its first letter should be capitalized. (We will handle this later.)

try:
    # 💡 TIP: An empty string is False in a condition.
    # Starting with an empty string makes the while loop run at least once.
    fname = ""

    # ℹ️ INFO: Keep asking while fname is empty.
    while not fname:
        fname = input("Please enter your first name:  ")

        # 💡 TIP: strip() removes spaces from the beginning and end.
        # This makes an entry containing only spaces count as empty.
        fname = fname.strip()

    # 📝 AGE CHECK
    # 💡 TIP: -1 is used as a starting value because it is not a valid age.
    age = -1

    # ℹ️ INFO: Keep asking while the age is negative.
    while age < 0:
        # ⚠️ WARNING: int() can only convert whole-number text.
        age = int(input("please enter your child's age: (whole years, round down)"))

# ⚠️ WARNING: ValueError happens when input cannot be converted to the needed type.
except ValueError:
    print("I'm sorry, that is not a valid value")

# ℹ️ INFO: This catches other unexpected errors and displays their message.
except Exception as e:
    print(f"Error: {e}")
