"""
Final Project - Coffee Ordering System (entry point).

🧠 Original student work:
- Created `main()` and connected imports for employees/orders/printing.

✅ Completed by Codex (2026-11-11):
- 🧠 End-to-end flow: get employee → take order → confirm → save → print label → optional receipt.
- 🛡️ Removed debug prints; keep user-facing prompts clean.
"""

from __future__ import annotations

import os

import employees
import orders
import print_orders


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


def main():
    # 🧠 STEP 0: Organize the main program logic
    clear_screen()

    # 🧠 STEP 1: Employee lookup / creation
    employee_id, employee_record = employees.get_employee()

    # 🧠 STEP 2: Take an order
    order = orders.get_order(employee_id)

    # 🧠 STEP 3: Confirm/edit the order
    order = orders.confirm_order(order)

    # 💾 STEP 4: Save the order
    orders.save_order(order)

    # 🖨️ STEP 5: Print the label + optionally save a receipt
    clear_screen()
    print_orders.print_label(order, employee_id, employee_record)
    receipt_path = print_orders.maybe_print_receipt(order, employee_id, employee_record)
    if receipt_path is not None:
        print(f"Receipt saved to: {receipt_path}")


# ▶️ Start the program by calling main().
if __name__ == "__main__":
    main()

