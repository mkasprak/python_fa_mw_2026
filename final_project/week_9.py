"""
Final project - step 1
Copy as a new step with new comment each week
This week: Define constants, create stubs, create menu

"""

# ---------------------------------------------------------------------------
# 📝 STEP 1: Plan the program with FUNCTION STUBS
# ---------------------------------------------------------------------------
# ✅ We are NOT finishing the program yet.
# ✅ Goal: write the "skeleton" so we can see the plan for the final project.
#
# 🧠 What is a stub?
# A stub is a placeholder function you will finish later.
# - It has the correct name (so you can call it)
# - It has the correct parameters (inputs)
# - It has comments/TODOs describing what it will do later
# - It often uses `pass` so the file still runs without errors
#
# ⚠️ IMPORTANT: Right now, many of these functions do not return anything yet.
# In Python, a function with no return statement returns None.
# That is OK for Step 1 because we are only planning.
# ---------------------------------------------------------------------------

# ℹ️ Globals: variables declared outside of all functions are global.
# ℹ️ Constants (still globals): do not change while the program is running.
SIZES = ("Small", "Medium", "Large", "X-Large")
MILKS = ("Oat", "Soy", "Coconut", "Whole", "2%", "Skim")

# ⚠️ WARNING: Notice that SIZES uses "X-Large" but PRICES uses "Extra Large".
# Later, when you look up a price, the spelling must match exactly.
PRICES = {"Small": 3.50, "Medium": 5.00, "Large": 7.00, "Extra Large": 9.00}

# 💡 This is the filename where we might save menu information later.
MENU = "menu.txt"


# Program Functions


def login():
    """
    📝 LOGIN (STUB)
    Gets login information from the employee.

    Later goal:
    - Return the employee's ID (an int)
    - Look up the employee in a file/list to display their name and info
    """
    print("Please login")

    # ⚠️ input() returns TEXT, so we convert it to an integer with int(...).
    # If the user types letters, this will crash for now (we will learn try/except later).
    #
    # 💡 We use `id` as short for "employee ID". Later you might rename it to `employee_id`
    # to make the meaning extra clear.
    id = int(input("Please enter your employee ID:  "))

    # 💡 TODO (later): Have an employee text file with IDs and names.
    # - If the ID is found, display name, office, extension
    # - If the ID is not found, ask for that info and save it
    pass


def past_orders(employee):
    """
    📝 PAST ORDERS (STUB)
    Checks for past orders and offers a reorder option.

    Args:
        employee: the employee ID from login()

    Later goal:
    - Display the most recent 5 orders (if any)
    - Ask if they want to reorder
    - Return the number of the chosen order (or 6 for "new order")
    """
    # 💡 TODO (later): Read saved orders from a file and display choices.
    pass


def new_order(employee):
    """
    📝 NEW ORDER (STUB)
    Collects information for a new order.

    Args:
        employee: the employee ID for this order

    Later goal:
    - Display choices (size, milk, etc.)
    - Collect inputs
    - Build and return a LIST named `order`
    """
    # 💡 TODO (later): Decide what goes into the `order` list (the order "format").
    pass


def verify(order):
    """
    📝 VERIFY (STUB)
    Verifies an order by displaying it and asking the user what to do next.

    Args:
        order: the order list from new_order()

    Later goal:
    - Display the order nicely
    - Ask: confirm / correct / cancel
    - Return a decision
    """
    # 💡 TODO (later): Decide what this function returns (True/False? a menu number?).
    pass


def save_order(order):
    """
    📝 SAVE ORDER (STUB)
    Saves an order to a text file.

    Args:
        order: the order data to save
    """
    # 💡 TODO (later): Write order data to a .txt file so it can be loaded again.
    pass


def change_order(order):
    """
    📝 CHANGE ORDER (STUB)
    Allows the user to update parts of the order.

    Args:
        order: the order list

    Later goal:
    - Display numbered parts of the order
    - Let the user choose what to change
    - Update the order and return it
    """
    # 💡 TODO (later): Decide how to show the order so it is easy to edit.
    pass


def display_order(order):
    """
    📝 DISPLAY ORDER (STUB)
    Displays the order output (receipt/label).

    Args:
        order: the final order list
    """
    # 💡 In the real world this might print a label or receipt.
    pass


# Main traditionally is coded at the end of the page so the other functions are loaded first
def main():
    """
    🧠 MAIN (Driver Function)
    main() organizes the program flow by calling the other functions in order.
    """
    # ℹ️ main organizes all of the functions.
    id = login()
    saved = past_orders(id)

    # 💡 TODO (later): If a saved order is chosen, skip new_order() and load that order.
    # For now, we always create a new order.
    order = new_order(id)
    approved = verify(order)

    # 💡 TODO (later): If approved, save. If not, change the order and re-verify.
    save_order(order)
    change_order(order)
    display_order(order)


# ⚠️ When Python runs this file, it starts at the top and executes line-by-line.
# Calling main() here means the program runs immediately when the file runs.

main()
