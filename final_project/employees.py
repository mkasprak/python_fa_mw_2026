"""
Called by `main.py` - handles creating, confirming, and looking up employees.

🧠 Original student work:
- Prompted for employee ID, name, office, extension, allergies, and saved to `employees.txt`.

✅ Completed by Codex (2026-11-11):
- 🛡️ Robust file parsing (loads dicts from `employees.txt` instead of returning partial strings).
- 💾 Save/update employees by ID (avoids duplicate IDs piling up forever).
- 🛡️ Input validation + error logging to `final_project/error.txt`.
- ✅ `get_employee()` now returns both `employee_id` and the `employee_record` dict for printing receipts/labels.
"""

from __future__ import annotations

import ast
import datetime
import os
from pathlib import Path
from typing import Any


_BASE_DIR = Path(__file__).resolve().parent
_EMPLOYEE_FILE = _BASE_DIR / "employees.txt"
_ERROR_FILE = _BASE_DIR / "error.txt"


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


def _log_error(e: Exception) -> None:
    # 🛡️ Safety: keep a simple local error log instead of crashing the whole program.
    right_now = datetime.datetime.now()
    try:
        with open(_ERROR_FILE, "a", encoding="utf-8") as f:
            f.write(f"{right_now}: {type(e).__name__}: {e}\n")
    except Exception:
        pass


def _parse_employee_record(text: str) -> dict[str, Any] | None:
    # 🛡️ Safety: `employees.txt` stores Python dicts like "{'office': 'g204', ...}".
    # We use `ast.literal_eval` (safe) instead of `eval`.
    try:
        value = ast.literal_eval(text.strip())
    except Exception:
        return None
    if isinstance(value, dict):
        return value
    return None


def load_employees() -> dict[int, dict[str, Any]]:
    # 💾 Load all employees into a dict keyed by employee_id.
    employees: dict[int, dict[str, Any]] = {}
    if not _EMPLOYEE_FILE.exists():
        return employees

    try:
        with open(_EMPLOYEE_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or ":" not in line:
                    continue
                employee_id_str, payload = line.split(":", 1)
                try:
                    employee_id = int(employee_id_str.strip())
                except ValueError:
                    continue

                record = _parse_employee_record(payload)
                if record is None:
                    continue
                employees[employee_id] = record
    except Exception as e:
        _log_error(e)

    return employees


def save_employees(employees: dict[int, dict[str, Any]]) -> None:
    # 💾 Save employees back to disk (one employee per line).
    try:
        with open(_EMPLOYEE_FILE, "w", encoding="utf-8") as f:
            for employee_id in sorted(employees.keys()):
                f.write(f"{employee_id}:{employees[employee_id]}\n")
    except Exception as e:
        _log_error(e)


def lookup_employee(employee_id: int) -> dict[str, Any] | None:
    employees = load_employees()
    return employees.get(employee_id)


def get_employee() -> tuple[int, dict[str, Any]]:
    # 🧠 STEP 1: Identify the employee
    # ✅ Return: (employee_id, employee_record)
    while True:
        try:
            employee_id = int(input("Please enter your ID number:  ").strip())
            break
        except ValueError:
            input("Please enter a whole number. Press Enter to continue...")
        except Exception as e:
            _log_error(e)
            input("Something went wrong. Press Enter to try again...")

    employees = load_employees()
    existing = employees.get(employee_id)
    if existing is not None:
        print("Employee found.")
        input("Press Enter to continue...")
        return employee_id, existing

    # 🧠 If not found, collect new employee info (student workflow).
    first_name = input("Please enter your first name:  ").strip()
    last_name = input("Please enter your last name:  ").strip()
    office_number = input("Office to deliver to:  ").strip()
    extension = input("Please enter extension:  ").strip()
    known_allergies = input(
        "Please enter any known food allergies or sensitivities separated by commas:  "
    ).strip()

    employee_record: dict[str, Any] = {
        "office": office_number,
        "extension": extension,
        "f_name": first_name,
        "l_name": last_name,
        "allergies": known_allergies,
    }

    employee_id, employee_record = confirm_employee(employee_id, employee_record, employees)
    employees[employee_id] = employee_record
    save_employees(employees)

    return employee_id, employee_record


def confirm_employee(
    employee_id: int,
    employee_record: dict[str, Any],
    employees: dict[int, dict[str, Any]],
) -> tuple[int, dict[str, Any]]:
    # 🧠 STEP 1b: Confirm employee info (print the record, let the user fix mistakes)
    # ✅ Return: (employee_id, employee_record)
    while True:
        clear_screen()

        print(f"1.  Employee ID:  {employee_id}")
        print(f"2.  Office Number:  {employee_record.get('office','')}")
        print(f"3.  Extension:  {employee_record.get('extension','')}")
        print(f"4.  First Name:  {employee_record.get('f_name','')}")
        print(f"5.  Last Name:  {employee_record.get('l_name','')}")
        print(f"6.  Allergies: {employee_record.get('allergies','')}")

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

        match change:
            case 1:
                while True:
                    try:
                        new_id = int(input("New employee ID: ").strip())
                        if new_id in employees and new_id != employee_id:
                            # ⚠️ Warn before overwriting another employee.
                            input(
                                "That ID already exists. Press Enter to choose a different ID..."
                            )
                            continue
                        employee_id = new_id
                        break
                    except ValueError:
                        input("Employee ID must be a whole number. Press Enter to continue...")
                    except Exception as e:
                        _log_error(e)
                        input("Something went wrong. Press Enter to continue...")
            case 2:
                employee_record["office"] = input("New office number: ").strip()
            case 3:
                employee_record["extension"] = input("New extension: ").strip()
            case 4:
                employee_record["f_name"] = input("New first name: ").strip()
            case 5:
                employee_record["l_name"] = input("New last name: ").strip()
            case 6:
                employee_record["allergies"] = input("New allergies: ").strip()
            case _:
                input("Please choose a number 1-6. Press Enter to continue...")
