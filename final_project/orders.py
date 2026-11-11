"""
Called by `main.py` - collects orders and saves them to disk.

🧠 Original student work:
- Menu-driven prompts for drink, size, milk, flavor, pumps.

✅ Completed by Codex (2026-11-11):
- 🛡️ Fixed list/index bugs and mismatched return types (now works with list-based menu data).
- 💾 Save orders to `final_project/orders.txt` (one order per line) with a real `order_id`.
- ✅ `get_order()` returns an order dict instead of `None`.
- 🧠 Implemented `confirm_order(order)` to review/edit before saving.
"""

from __future__ import annotations

import ast
import datetime
import os
from pathlib import Path
from typing import Any

import read_menu

_BASE_DIR = Path(__file__).resolve().parent
_ORDER_FILE = _BASE_DIR / "orders.txt"
_ERROR_FILE = _BASE_DIR / "error.txt"

_PUMP_COST = 0.10
_MAX_PUMPS = 10


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


def _parse_order(text: str) -> dict[str, Any] | None:
    # 🛡️ Safety: parse a saved dict safely (no `eval`).
    try:
        value = ast.literal_eval(text.strip())
    except Exception:
        return None
    if isinstance(value, dict):
        return value
    return None


def load_orders() -> list[dict[str, Any]]:
    # 💾 Load orders from disk (one dict per line).
    orders: list[dict[str, Any]] = []
    if not _ORDER_FILE.exists():
        return orders

    try:
        with open(_ORDER_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                order = _parse_order(line)
                if order is None:
                    continue
                orders.append(order)
    except Exception as e:
        _log_error(e)

    return orders


def _next_order_id(existing_orders: list[dict[str, Any]]) -> int:
    # ✅ Return: next integer order_id.
    max_id = 0
    for order in existing_orders:
        try:
            max_id = max(max_id, int(order.get("order_id", 0)))
        except Exception:
            continue
    return max_id + 1


def save_order(order: dict[str, Any]) -> None:
    # 💾 Append an order to the order file.
    try:
        with open(_ORDER_FILE, "a", encoding="utf-8") as f:
            f.write(f"{order}\n")
    except Exception as e:
        _log_error(e)


def _prompt_choice(prompt: str, option_count: int) -> int:
    # 🛡️ Safety: keep asking until the user enters a valid 1..N choice.
    while True:
        try:
            choice = int(input(prompt).strip())
        except ValueError:
            input(f"Please enter a number (1-{option_count}). Press Enter to continue...")
            continue
        except Exception as e:
            _log_error(e)
            input("Something went wrong. Press Enter to continue...")
            continue

        if 1 <= choice <= option_count:
            return choice
        input(f"Please enter a number (1-{option_count}). Press Enter to continue...")


def _prompt_pumps() -> int:
    while True:
        try:
            pumps = int(
                input(
                    f"Please enter the number of pumps you want (${_PUMP_COST:.2f} each, 0-{_MAX_PUMPS}):  "
                ).strip()
            )
        except ValueError:
            input(f"Please enter a number (0-{_MAX_PUMPS}). Press Enter to continue...")
            continue
        except Exception as e:
            _log_error(e)
            input("Something went wrong. Press Enter to continue...")
            continue

        if pumps < 0:
            input("Pumps cannot be negative. Press Enter to continue...")
            continue
        if pumps > _MAX_PUMPS:
            input(f"{_MAX_PUMPS} is the maximum number of pumps. Press Enter to continue...")
            continue
        return pumps


def _compute_prices(size_index: int, prices: list[float], pumps: int) -> tuple[float, float, float]:
    base_price = prices[size_index]
    pump_price = pumps * _PUMP_COST
    total_price = base_price + pump_price
    return base_price, pump_price, total_price


def get_order(employee_id: int) -> dict[str, Any]:
    # 🧠 STEP 2: Collect a drink order
    # ✅ Return: order dict (ready to confirm/save)
    menu_items = read_menu.read_menu()
    coffee, prices, milks, flavors, sizes = read_menu.split_into_variables(menu_items)

    clear_screen()

    drink_count = read_menu.print_coffee(coffee)
    drink_choice = _prompt_choice(
        "Please enter the number for the type of drink you want:  ",
        drink_count,
    )
    drink = coffee[drink_choice - 1]

    clear_screen()
    size_count = read_menu.print_sizes(prices, sizes)
    size_choice = _prompt_choice(
        "Please enter the number for the size of drink you want:  ",
        size_count,
    )
    size_index = size_choice - 1
    size = sizes[size_index]

    clear_screen()
    milk_count = read_menu.print_milks(milks)
    milk_choice = _prompt_choice(
        "Please enter the number for the milk you want:  ",
        milk_count,
    )
    milk = milks[milk_choice - 1]

    clear_screen()
    flavor_count = read_menu.print_flavors(flavors)
    flavor_choice = _prompt_choice(
        "Please enter the number for the flavor you want:  ",
        flavor_count,
    )
    flavor = flavors[flavor_choice - 1]

    pumps = _prompt_pumps()

    base_price, pump_price, total_price = _compute_prices(size_index, prices, pumps)

    existing_orders = load_orders()
    order_id = _next_order_id(existing_orders)
    right_now = datetime.datetime.now()

    order: dict[str, Any] = {
        "order_id": order_id,
        "employee_id": employee_id,
        "timestamp": right_now.isoformat(timespec="seconds"),
        "drink": drink,
        "size": size,
        "milk": milk,
        "flavor": flavor,
        "pumps": pumps,
        "base_price": base_price,
        "pump_price": pump_price,
        "total_price": total_price,
    }

    return order


def _print_order(order: dict[str, Any]) -> None:
    # 🖨️ Display the order neatly for confirmation.
    print("Order Summary\n")
    print(f"1.  Drink:   {order.get('drink','')}")
    print(f"2.  Size:    {order.get('size','')}  (${order.get('base_price', 0):.2f})")
    print(f"3.  Milk:    {order.get('milk','')}")
    print(f"4.  Flavor:  {order.get('flavor','')}")
    print(f"5.  Pumps:   {order.get('pumps', 0)}  (${order.get('pump_price', 0):.2f})")
    print(f"\nTotal: ${order.get('total_price', 0):.2f}")


def confirm_order(order: dict[str, Any]) -> dict[str, Any]:
    # 🧠 STEP 3: Confirm an order (show it back to the user and allow edits)
    # ✅ Return: the updated order dict
    menu_items = read_menu.read_menu()
    coffee, prices, milks, flavors, sizes = read_menu.split_into_variables(menu_items)

    while True:
        clear_screen()
        _print_order(order)

        correct = input("\nIs everything correct? (Y/N) ").strip().upper()
        if correct == "Y":
            return order
        if correct != "N":
            input("Please enter Y or N. Press Enter to continue...")
            continue

        try:
            change = int(input("Please enter the number you want to change (1-5):  ").strip())
        except ValueError:
            input("Please enter a number (1-5). Press Enter to continue...")
            continue
        except Exception as e:
            _log_error(e)
            input("Something went wrong. Press Enter to continue...")
            continue

        match change:
            case 1:
                clear_screen()
                drink_count = read_menu.print_coffee(coffee)
                drink_choice = _prompt_choice(
                    "Please enter the number for the type of drink you want:  ",
                    drink_count,
                )
                order["drink"] = coffee[drink_choice - 1]
            case 2:
                clear_screen()
                size_count = read_menu.print_sizes(prices, sizes)
                size_choice = _prompt_choice(
                    "Please enter the number for the size of drink you want:  ",
                    size_count,
                )
                size_index = size_choice - 1
                order["size"] = sizes[size_index]
                base_price, pump_price, total_price = _compute_prices(
                    size_index,
                    prices,
                    int(order.get("pumps", 0)),
                )
                order["base_price"] = base_price
                order["pump_price"] = pump_price
                order["total_price"] = total_price
            case 3:
                clear_screen()
                milk_count = read_menu.print_milks(milks)
                milk_choice = _prompt_choice(
                    "Please enter the number for the milk you want:  ",
                    milk_count,
                )
                order["milk"] = milks[milk_choice - 1]
            case 4:
                clear_screen()
                flavor_count = read_menu.print_flavors(flavors)
                flavor_choice = _prompt_choice(
                    "Please enter the number for the flavor you want:  ",
                    flavor_count,
                )
                order["flavor"] = flavors[flavor_choice - 1]
            case 5:
                pumps = _prompt_pumps()
                order["pumps"] = pumps
                try:
                    size_index = sizes.index(order.get("size"))
                except ValueError:
                    size_index = 0
                base_price, pump_price, total_price = _compute_prices(size_index, prices, pumps)
                order["base_price"] = base_price
                order["pump_price"] = pump_price
                order["total_price"] = total_price
            case _:
                input("Please choose a number 1-5. Press Enter to continue...")

