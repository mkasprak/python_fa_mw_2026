"""
Putting the 'Fun' into Functions!!!
"""

# ℹ️ A function is a named group of instructions that we can call when needed.
def greeting(name):
    # ℹ️ name is a parameter: the value passed into greeting().
    print(f"Hi, {name}")


# 💡 Call the function with "Meri" as the name argument.
greeting("Meri")


# ℹ️ This function sends a value back to the caller instead of printing it.
def multiply(a, b):
    return a * b


# 💡 Save the returned product so we can use it in the next line.
answer = multiply(10, 3)
print(answer)
