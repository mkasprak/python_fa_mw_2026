
import os
import datetime
import read_menu
def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")



def get_order(emp_id):
    menu_items = read_menu.read_menu()
    coffee, prices, milks, flavors, shots = read_menu.split_into_variables(menu_items)
    #read_menu.print_menu(coffee, prices, milks, flavors, shots)
    clear_screen()
    while True:
        list_length = read_menu.print_coffee(coffee)
        try:
           
            type = int(
                input(
                    "Please enter the number for the type of drink you want:  "
                ).strip()
            )
        except ValueError:
            
            input(
                f"Please enter a number (1-{list_length}). Press Enter to continue..."
            )
        except Exception as e:
            right_now = datetime.datetime.now()
            with open("final_project\\error.txt", "a") as f:
                f.write(f"{right_now}:  {e}\n")
            continue
        if type < 1 or type > list_length:
            input(
                f"Please enter a number (1-{list_length}). Press Enter to continue..."
            )
            continue
        # ℹ️ info: We subtract 1 because users choose 1..N, but Python indexes are 0..N-1.
        drink = list_length[type - 1]
        break

    clear_screen()
    # while True:
    #     # 🖨️ Display the size menu
    #     count = 1
    #     for size in SIZES:
    #         print(f"{count}.   {size}")
    #         count += 1
    #     try:
    #         my_size = int(
    #             input(
    #                 "Please enter the number for the size of drink you want:  "
    #             ).strip()
    #         )
    #     except ValueError:
    #         # ⚠️ Common bug: use len(SIZES), not SIZES.len()
    #         input(f"Please enter a number (1-{len(SIZES)}). Press Enter to continue...")
    #         continue
    #     except Exception as e:
    #         right_now = datetime.datetime.now()
    #         with open("final_project\\error.txt", "a") as f:
    #             f.write(f"{right_now}:  {e}\n")
    #         continue
    #     if my_size < 1 or my_size > len(SIZES):
    #         input(f"Please enter a number (1-{len(SIZES)}). Press Enter to continue...")
    #         continue
    #     size = SIZES[my_size - 1]
    #     break

    # clear_screen()
    # while True:
    #     # 🖨️ Display the milk menu
    #     count = 1
    #     for milk in MILKS:
    #         print(f"{count}.   {milk}")
    #         count += 1
    #     try:
    #         my_milk = int(
    #             input("Please enter the number for the milk you want:  ").strip()
    #         )
    #     except ValueError:
    #         # ⚠️ Common bug: use len(MILKS), not MILKS.len()
    #         input(f"Please enter a number (1-{len(MILKS)}). Press Enter to continue...")
    #         continue
    #     except Exception as e:
    #         right_now = datetime.datetime.now()
    #         with open("final_project\\error.txt", "a") as f:
    #             f.write(f"{right_now}:  {e}\n")
    #         continue
    #     if my_milk < 1 or my_milk > len(MILKS):
    #         input(f"Please enter a number (1-{len(MILKS)}). Press Enter to continue...")
    #         continue
    #     milk = MILKS[my_milk - 1]
    #     break

    # clear_screen()
    # while True:
    #     # 🖨️ Display the flavor menu
    #     count = 1
    #     for flavor in FLAVORS:
    #         print(f"{count}.   {flavor}")
    #         count += 1
    #     try:
    #         my_flavor = int(
    #             input("Please enter the number for the flavor you want:  ").strip()
    #         )
    #     except ValueError:
    #         # ⚠️ Common bug: use len(FLAVORS), not FLAVORS.len()
    #         input(
    #             f"Please enter a number (1-{len(FLAVORS)}). Press Enter to continue..."
    #         )
    #         continue
    #     except Exception as e:
    #         right_now = datetime.datetime.now()
    #         with open("final_project\\error.txt", "a") as f:
    #             f.write(f"{right_now}:  {e}\n")
    #         continue
    #     if my_flavor < 1 or my_flavor > len(FLAVORS):
    #         input(
    #             f"Please enter a number (1-{len(FLAVORS)}). Press Enter to continue..."
    #         )
    #         continue
    #     flavor = FLAVORS[my_flavor - 1]
    #     break

    # while True:
    #     try:
    #         # 🧠 Ask for the number of flavor pumps (extra flavor shots)
    #         pumps = int(
    #             input(
    #                 "Please enter the number of pumps you want (ten cents each):  "
    #             ).strip()
    #         )
    #         if pumps < 0:
    #             print("Pumps cannot be negative. ")
    #             continue
    #         if pumps > 10:
    #             print("Ten is the maximum number of pumps. ")
    #             continue
    #     except ValueError:
    #         # 🛡️ If they type something that is not a number, don't crash—ask again.
    #         input(f"Please enter a number (0-10). Press Enter to continue...")
    #         continue
    #     except Exception as e:
    #         right_now = datetime.datetime.now()
    #         with open("final_project\\error.txt", "a") as f:
    #             f.write(f"{right_now}:  {e}\n")
    #         continue
    #     break

    # # ℹ️ info: This order is stored as a Dictionary.
    # order = {
    #     emp_id: {
    #         "drink": drink,
    #         "size": size,
    #         "milk": milk,
    #         "flavor": flavor,
    #         "pumps": pumps,
    #     }
    # }
    # # TODO (Week 12 - file I/O lesson):
    # # - Save orders to a consistent file location (probably under final_project\\).
    # # - Use a format that's easy to read back (ex: CSV or JSON) instead of Python dict strings.
    # # - Return the order (or an order_id) so the next step can confirm/print it without re-reading yet.
    # with open("all_orders.txt", "a") as f:
    #     f.write(f"{order}\n")

    # return


def confirm_order(order_num):
    # 🧠 STEP 3: Confirm an order (show it back to the user and allow edits)
    # ✅ Return: the updated order list
    order = []  # Week 12: we will read in the order from a file

    while True:
        clear_screen()
        count = 1
        # 🖨️ Display the order with numbers starting at 1 (easier for people to choose a line to edit)
        for item in order:
            print(f"{count}.  {item}")
            count += 1
        try:
            correct = input("Is everything correct (Y/N)").strip().upper()
            if correct == "Y":
                return order
            if correct != "N":
                input("Please enter Y or N. Press Enter to continue...")
                continue

            change = int(input("Please enter the number you want to change:  ").strip())
        except ValueError:
            # ⚠️ Common bug: lists don't have .length(); the Python way is len(order)
            input(f"Please enter a number (1-{len(order)}). Press Enter to continue...")
            continue
        except Exception as e:
            right_now = datetime.datetime.now()
            with open("final_project\\error.txt", "a") as f:
                f.write(f"{right_now}:  {e}\n")
            continue

        try:
            if change < 1 or change > len(order):
                input(
                    f"Please enter a number (1-{len(order)}). Press Enter to continue..."
                )
                continue
            # ℹ️ info: change is 1-based for the user, so we use change-1 for the list index.
            new_value = input(f"Please enter the new value for {order[change-1]}")
            order[change - 1] = new_value
            # 💡 tip: We use `continue` (loop again) instead of calling confirm_order(order) again.
            # That keeps the logic in one loop and avoids recursion.
            continue
        except Exception as e:
            print(f"{e}\n\nThat was not a valid entry. Try again")
            input("Press Enter to continue...")
            continue
        except Exception as e:
            right_now = datetime.datetime.now()
            with open("final_project\\error.txt", "a") as f:
                f.write(f"{right_now}:  {e}\n")
            continue

