"""

using functions to create a menu
"""

# ℹ️ This global list stores the names entered through the menu.
NAMES = []  # an empty list


def display_menu():
    # ℹ️ Show the available actions before asking the user to choose one.
    print("1.  Create")
    print("2.  Read")
    print("3.  Update")
    print("4.  Delete")

    # ℹ️ int() converts the typed text into a whole number for match/case.
    try:
        selection = int(input("Please enter the number of your selection:  "))
    except Exception as e:
        # ⚠️ Non-numeric input cannot be converted to an integer.
        print("Sorry. That was not a valid choice.")
        display_menu()

    # ℹ️ return sends the selected number back to the code that called this function.
    return selection


def run_menu(choice):
    # 💡 match/case chooses an action based on the menu number.
    match choice:
        case 1:
            create()
        case 2:
            read()
            print(NAMES)
        case 3:
            update()
        case 4:
            delete()
        case _:
            # ⚠️ Handle a number that is not one of the listed menu choices.
            print("Sorry, that is not a valid choice")
            value = display_menu()
            run_menu(value)


def create():
    # ℹ️ Ask for a name and append it to the shared NAMES list.
    name = input("Please enter your first name:  ")
    NAMES.append(name)


def read():
    # 💡 TODO: Add the code that reads or displays a saved record.
    pass


def update():
    # 💡 TODO: Add the code that updates a saved record.
    pass


def delete():
    # 💡 TODO: Add the code that deletes a saved record.
    pass


def main():
    # ℹ️ First get the user's choice, then pass it to the menu dispatcher.
    value = display_menu()
    run_menu(value)
    # ℹ️ Print the current list to show the names stored so far.
    print(NAMES)


main()
