"""
   split program apart (week 12)

"""



import os

# next class add date time stamp
import datetime

import employees
import orders
import print_orders
import read_menu


def clear_screen():
  
    _ = os.system("cls" if os.name == "nt" else "clear")


def main():
    clear_screen()
    emp_id = employees.get_employee()
    order_num = orders.get_order(emp_id)
    # orders.confirm_order(order_num)


# ▶️ Start the program by calling main().
if __name__ == "__main__":
    main()
