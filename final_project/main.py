"""
check for existing

"""

import os

# next class add date time stamp
import datetime
import employees
import orders
import print_orders
import read_menu


def clear_screen():
    # clears screen

    _ = os.system("cls" if os.name == "nt" else "clear")


def main():
    # organizes logic
    clear_screen()
    emp_id = employees.get_employee()
    print(f"Main   {emp_id}")
    order_num = orders.get_order(emp_id)
    # orders.confirm_order(order_num)


# ▶️ Start the program by calling main().
if __name__ == "__main__":
    main()
