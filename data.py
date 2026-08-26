# ℹ️ In Python, text is represented as a "string" and can be written using either double quotes ("") or single quotes ('').
# 💡 Tip: It is generally best to be consistent and use one style throughout your program, unless you have a specific reason to switch.
print("Double quotes")
print("single quotes")

# ℹ️ If you want to print double quotes inside your text, you can wrap the entire string in single quotes.
print('Print "double quotes"')

# ℹ️ Similarly, to print single quotes inside your text, wrap the entire string in double quotes.
print("Print 'single quotes'")

# ℹ️ You can also use a backslash (\) right before a quote to "escape" it. This tells Python to treat it as a normal character rather than the end of the string.
# ⚠️ Warning: Forgetting the backslash when using the same quotes inside and outside will cause a syntax error!
print("Or use escape \" or ' to print quotes")


# ℹ️ Data Types: Numbers vs. Strings.
# Python treats integers (whole numbers) and strings (text in quotes) very differently.
integer = 1
my_int = "1"

# ⚠️ Warning: Adding an integer and a string together directly is NOT ALLOWED in Python! It will cause a TypeError.
# print("Adding a number to a string: ")
# print(integer + my_int)                    💀⚡💀⚡ NOT ALLOWED


# ℹ️ String Concatenation: When you use "+" with two strings, Python joins (glues) them end-to-end.
print("Adding strings: ")
print(my_int + my_int)
# 💡 Tip: Since "my_int" is a string, "1" + "1" results in "11" (not 2).

# ℹ️ Math Addition: When you use "+" with two integers, Python performs standard math.
print("Adding numbers:")
print(integer + integer)
# 💡 Tip: Since "integer" is a number, 1 + 1 results in 2.


# ℹ️ Booleans: Boolean variables store logical values of either True or False. Notice the capital T and F!
# 👻 Fun fact: Named after mathematician George Boole, they are used to handle true/false states.
tired = True
awake = True
coffee = False

print(coffee)

# ℹ️ Basic Decision Making: An "if" statement executes the indented code block below it only if the condition is True.
if tired:
    print("I need coffee")
