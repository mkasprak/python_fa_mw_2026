"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Copy and paste THIS comment from opening to closing quotes).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# ℹ️ This program is a Mad Libs game that takes user input to customize a famous nursery rhyme.
# 🆘 Need help? Reach out to your instructor or check the assignment guidelines!


# ℹ️ Declare variables
# 💡 Tip: Initializing variables first is optional in Python but highly recommended.
# name = ""
# animal = ""
# color = ""


# ℹ️ Request user inputs and store them in descriptive variables.
name = input("Please enter a person's name: ")
animal = input("Please enter a type of animal: ")
color = input("Please enter a color: ")


# ℹ️ Output the final story.
# 💡 Tip: We use f-strings (formatted string literals prefixed with 'f') to embed variables easily.
# ⚠️ Warning: Forgetting the 'f' before the opening quote will print variable names as raw text instead of their values!
print("Mad Lib for Mary Had a Little Lamb\n\n")
print(f"{name} had a little {animal}")
print(f"Whose fleece was {color} as snow")
print(f"And everywhere that {name} went")
print(f"The {animal} was sure to go")
