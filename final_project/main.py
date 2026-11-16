"""
Final Project - Coffee Ordering System (entry point).

🧠 Student work:
- Connected `main()` to the other files.

✅ Completed by Codex (student style):
- 🧠 End-to-end flow: employee → order → confirm → save → print label → optional receipt.
"""

import os

import employees
import orders
import print_orders


def clear_screen():
    # clears screen
    _ = os.system("cls" if os.name == "nt" else "clear")


def main():
    # 🧠 STEP 0: Organize the main program logic
    clear_screen()

    # 🧠 STEP 1: Employee lookup / creation
    employee_id = employees.get_employee()

    # 🧠 STEP 2: Take an order
    order = orders.get_order(employee_id)

    # 🧠 STEP 3: Confirm/edit the order
    order = orders.confirm_order(order)

    # 💾 STEP 4: Save the order
    orders.save_order(order)

    # 🖨️ STEP 5: Print the label + optionally save a receipt
    clear_screen()
    print_orders.print_label(order, employee_id)
    print_orders.maybe_print_receipt(order, employee_id)


# ▶️ Start the program by calling main().
if __name__ == "__main__":
    main()

