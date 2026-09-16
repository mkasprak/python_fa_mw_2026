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

# 🚩 STATE FLAG: We create a variable to track if the program should keep running.
is_running = True

while is_running:
    # 🧭 MENU: Display the available choices at the start of each iteration
    print("\n--- CONTACT MANAGER ---")
    print("1. Create a new contact")
    print("2. Search contacts")
    print("3. Update contact")
    print("4. Delete a contact")
    print("5. Quit")

    # 🛡️ INPUT VALIDATION: Guard numeric conversion against text crashes
    try:
        choice = int(input("Please enter the number of your selection: "))
    except ValueError:
        print("Error: That is not a valid number. Please enter digits only.")
        # ⏭️ CONTINUE: Immediately skip the rest of this pass and return to the menu prompt.
        continue
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        continue

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
