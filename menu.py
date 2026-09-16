"""
Thinking CRUD

🏗️ Create
📖 Read
🔃 Update
🗑️ Delete

💡 A CRUD program presents users with a menu of choices.
This version uses a state flag (is_running) to control the loop, safely validates inputs,
and uses continue to restart the menu if bad data is entered.
"""

# 🧭 MENU: A CRUD program usually starts by showing the user available actions.
# ℹ️ INFO: Each numbered option represents one task the program will eventually perform.
print(f" 1.  Create a new contact")
print(f" 2.  Search contacts")
print(f" 3.  Update contact")
print(f" 4.  Delete a contact")
print(f" 5.  Quit")

# 💡 TIP: `choice` needs a starting value before Python can test the `while` condition.
# Starting at 1 lets the loop begin and ask the user for their real selection.
choice = 1

# 🔁 LOOP: Keep offering actions while the choice is 1, 2, 3, or 4.
# ℹ️ INFO: Choice 4 keeps the loop going, so Delete can be selected again.
while choice > 0 and choice < 5:
    # 💀⚡💀 WARNING: The value used in a while condition must change inside the loop.
    # Without this new input, a choice of 2 stays 2 forever and prints "Search" forever.
    # ⌨️ INPUT: input() gives us text, so int() changes a number such as "2" into the integer 2.
    choice = int(input("Please enter the number of your selection:  "))

    # 🧩 DECISION: match compares choice to each valid case
    match choice:
        case 1:
            # 🏗️ CREATE: Later, collect and save a new record
            print("Action: Create contact selected.")

        case 2:
            # 📖 READ: Look up and display an existing record
            print("Action: Search contacts selected.")

        case 3:
            # 🔃 UPDATE: Modify saved information
            print("Action: Update contact selected.")

        case 4:
            # 🗑️ DELETE: Remove a record
            print("Action: Delete contact selected.")

        case 5:
            # 👋 QUIT: Change the state flag to False to end the loop gracefully
            print("Good bye!")
            is_running = False

        case _:
            # 🛑 CATCH-ALL: Matches any integer outside the 1 to 5 range
            print("Invalid selection. Please choose an option from 1 to 5.")
