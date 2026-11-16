"""
Employee helpers (lookup + create + confirm).

🧠 Student work:
- Prompt for employee info and save it to `final_project\\employees.txt`.

✅ Completed by Codex (student style):
- 🛡️ Input validation (so typing letters for ID doesn't crash).
- ✅ `lookup_employee()` returns the saved employee text (or None).
- 🧠 `confirm_employee()` lets the user fix mistakes before saving.
"""

import datetime
import os


def clear_screen():
    # clears screens
    _ = os.system("cls" if os.name == "nt" else "clear")


def _log_error(e):
    # 🛡️ Save errors so we can troubleshoot without crashing.
    right_now = datetime.datetime.now()
    try:
        with open("final_project\\error.txt", "a") as f:
            f.write(f"{right_now}: {e}\n")
    except Exception:
        pass


def lookup_employee(employee_id):
    # 🧠 Look for an employee_id in employees.txt
    # ✅ Return: the saved employee text (string) OR None if not found
    try:
        with open("final_project\\employees.txt", "r") as file:
            for line in file:
                line = line.strip()
                if ":" not in line:
                    continue
                id_text, record_text = line.split(":", 1)
                try:
                    saved_id = int(id_text.strip())
                except ValueError:
                    continue

                if employee_id == saved_id:
                    return record_text.strip()
        return None
    except FileNotFoundError:
        # If the file doesn't exist yet, there are no saved employees.
        return None
    except Exception as e:
        _log_error(e)
        return None


def get_employee():
    # 🧠 STEP 1: Identify the employee
    # ✅ Return: employee_id (int)
    while True:
        try:
            employee_id = int(input("Please enter your ID number:  ").strip())
            break
        except ValueError:
            input("Please enter a whole number. Press Enter to continue...")
        except Exception as e:
            _log_error(e)
            input("Something went wrong. Press Enter to continue...")

    existing = lookup_employee(employee_id)
    if existing is not None:
        print("Employee found.")
        input("Press Enter to continue...")
        return employee_id

    # 🧠 If not found, collect new employee info.
    f_name = input("Please enter your first name:  ").strip()
    l_name = input("Please enter your last name:  ").strip()
    office_nbr = input("Office to deliver to:  ").strip()
    extension = input("Please enter extension:  ").strip()
    known_allergies = input(
        "Please enter any known food allergies or sensitivities separated by commas:  "
    ).strip()

    employee_record = {
        "office": office_nbr,
        "extension": extension,
        "f_name": f_name,
        "l_name": l_name,
        "allergies": known_allergies,
    }

    employee_id, employee_record = confirm_employee(employee_id, employee_record)

    # 💾 Save the new employee at the end.
    try:
        with open("final_project\\employees.txt", "a") as f:
            f.write(f"{employee_id}:{employee_record}\n")
    except Exception as e:
        _log_error(e)

    return employee_id


def confirm_employee(employee_id, employee_record):
    # 🧠 STEP 1b: Confirm employee info (print the record, let the user fix mistakes)
    # ✅ Return: (employee_id, employee_record)
    while True:
        clear_screen()

        print(f"1.  Employee ID:  {employee_id}")
        print(f"2.  Office Number:  {employee_record['office']}")
        print(f"3.  Extension:  {employee_record['extension']}")
        print(f"4.  First Name:  {employee_record['f_name']}")
        print(f"5.  Last Name:  {employee_record['l_name']}")
        print(f"6.  Allergies: {employee_record['allergies']}")

        correct = input("Is this correct? (Y/N) ").strip().upper()
        if correct == "Y":
            return employee_id, employee_record
        if correct != "N":
            input("Please enter Y or N. Press Enter to continue...")
            continue

        try:
            change = int(input("What number would you like to change? ").strip())
        except ValueError:
            input("Please enter a number (1-6). Press Enter to continue...")
            continue
        except Exception as e:
            _log_error(e)
            input("Something went wrong. Press Enter to continue...")
            continue

        if change == 1:
            while True:
                try:
                    employee_id = int(input("New employee ID: ").strip())
                    break
                except ValueError:
                    input("Employee ID must be a whole number. Press Enter to continue...")
                except Exception as e:
                    _log_error(e)
                    input("Something went wrong. Press Enter to continue...")
        elif change == 2:
            employee_record["office"] = input("New office number: ").strip()
        elif change == 3:
            employee_record["extension"] = input("New extension: ").strip()
        elif change == 4:
            employee_record["f_name"] = input("New first name: ").strip()
        elif change == 5:
            employee_record["l_name"] = input("New last name: ").strip()
        elif change == 6:
            employee_record["allergies"] = input("New allergies: ").strip()
        else:
            input("Please choose a number 1-6. Press Enter to continue...")

