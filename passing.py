"""
passing values with functions

"""

# 🧠 GOAL: Practice SCOPE (where a variable can be "seen") and how to PASS VALUES into functions.
# 💡 Vocabulary:
# - parameter = the variable name inside the function definition (def ...)
# - argument  = the actual value you send in when you call the function
# - local scope  = variables created inside a function (only usable in that function)
# - global scope = variables created at the top level of the file (usable anywhere in this file)

# 🌍 Global variables live at the top level of the file.
# 💡 Tip: Use globals sparingly in real programs, but they are helpful for learning scope.
SCOPE_DEMO = "Visible!!!"


def passed(variable):
    # ✅ variable is a PARAMETER (local to this function).
    # 💡 Tip: The PARAMETER NAME does not have to match the caller's variable name.
    # If main() passes in local, we can still name the parameter variable (or x, or value, etc.).
    print(variable)


def not_passed():
    # ⚠️ These would crash because local variables from OTHER functions are not in scope here:
    # print(local)     # local exists only inside main()
    # print(variable)  # variable exists only inside passed()

    # ✅ But globals ARE in scope inside functions.
    print(SCOPE_DEMO)


def count(one, two, three=3):
    # 🧠 Default parameter:
    # If the caller does NOT provide three, it uses the default value (3).
    print("\n\ncount")
    print(one)
    print(two)
    print(three)


def control(one, two, three):
    # 🧠 Keyword arguments:
    # The caller can name the parameters, so the order in the call does not matter.
    print("\n\nControl")
    print(one)
    print(two)
    print(three)


def order_pizza(toppings):
    # 🧠 Passing a LIST (mutable object):
    # toppings and my_toppings can refer to the SAME list in memory.
    # 💡 If we changed the list here (append/pop/etc.), the change could be seen back in main().
    for topping in toppings:
        print(topping)


def main():
    # ✅ main() is the "driver" function: it starts the program's work.
    print(SCOPE_DEMO)

    # 🏠 local is a LOCAL variable (it only exists inside main).
    local = "Can you see me?"
    print(local)

    # 📦 Passing a value into a function (argument -> parameter).
    # argument: local
    # parameter: variable (inside passed())
    passed(local)

    # 🔍 This function was NOT given local, so it cannot see it.
    not_passed()

    # ✅ Positional arguments: values match parameters by position.
    count(4, 32)

    # ✅ Keyword arguments: values match parameters by name (order does not matter).
    control(three=3, one=1, two=2)

    # ✅ Passing a list into a function.
    my_toppings = ["Pepperoni", "Mushroom", "Green Peppers", "Onions"]
    order_pizza(my_toppings)


# 💡 For now we call `main()` directly at the bottom of the file.
# Later (when we start using multiple files), you'll learn another common pattern for starting a program.
main()
