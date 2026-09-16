"""
Thinking CRUD

🏗️  Create
📖  Read
🔃  Update
🗑️  Delete

💡When we get to crud, we will present users with a menu of choices. This is a standard interface module. Now that we know Match Case, it makes menu choices easy. It will get even easier when we get to functions.
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

    # 🧩 DECISION: match compares `choice` to each case and runs the matching block.
    match choice:

        case 1:
            # 🏗️ CREATE: Later, this is where we will collect and save a new contact.
            print("Create")
        case 2:
            # 📖 READ: Searching lets us look up and display an existing contact.
            print("Search")  # read
        case 3:
            # 🔃 UPDATE: Later, this is where we will change saved contact information.
            print("Update")
        case 4:
            # 🗑️ DELETE: Later, this is where we will remove a contact.
            print("Delete")
        case 5:
            # 👋 QUIT: Say goodbye. Because 5 is outside the while condition, the loop ends next.
            # 💡 TIP: This means "Good bye!" prints once instead of repeating.
            print("Good bye!")
