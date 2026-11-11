"""
Menu file reader + helpers for printing selection menus.

Fixes/notes (2026-11-11):
- Parse comma-separated menu values into Python lists so callers can safely use `len()` and indexing.
- Fix `.len()` bug and string-price formatting bug by converting prices to `float`.
- Make return values consistent: the `print_*` helpers return the number of options displayed.
- Add `print_sizes()` because `orders.get_order()` calls it.
- Read `menu.txt` from the `final_project/` folder by default so running from the repo root works.
"""

from __future__ import annotations

from pathlib import Path


def _menu_path() -> Path:
    # ✅ FIX: Use a path relative to this file so `py final_project/main.py` works from the repo root.
    local = Path(__file__).resolve().parent / "menu.txt"
    if local.exists():
        return local
    return Path("menu.txt")


def read_menu():
    menus = {}
    try:
        with open(_menu_path(), "r", encoding="utf-8") as file:
            for line in file:
                # FIX: avoid IndexError and accidental early-return when a line is blank or missing ":".
                line = line.strip()
                if not line or ":" not in line:
                    continue
                category, detail = line.split(":", 1)
                menus[category.strip()] = detail.strip()

        return menus
    except FileNotFoundError:
        print('Please create file or check file name. It should be "menu.txt"')
        # FIX: return an empty menu dict so downstream code doesn't crash on `None`.
        return {}
    except IndexError:
        return menus
    except Exception as e:
        print(e)


def _split_csv(value):
    """Split a comma-separated string into a clean list of non-empty items."""
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def split_into_variables(menu_items):
    # FIX: return lists (not raw strings) so callers can index and count options correctly.
    coffee = _split_csv(menu_items.get("COFFEE"))
    milks = _split_csv(menu_items.get("MILK"))
    flavors = _split_csv(menu_items.get("FLAVORS"))
    sizes = _split_csv(menu_items.get("SIZES"))

    # FIX: convert prices to floats so printing with `:.2f` works.
    prices_raw = _split_csv(menu_items.get("PRICES"))
    prices = []
    for p in prices_raw:
        try:
            prices.append(float(p))
        except ValueError:
            raise ValueError(f'Invalid price "{p}" in menu.txt under PRICES') from None

    return coffee, prices, milks, flavors, sizes


def print_coffee(coffee):
    print("Coffee\n")
    print("\nCoffee:")
    for idx, item in enumerate(coffee, start=1):
        print(f"{idx}. \t{item}")
    # FIX: return number of options displayed (not character count).
    return len(coffee)


def print_sizes(prices, sizes):
    """Print numbered size choices with their prices; returns number of choices shown."""
    print("Sizes\n")
    if not sizes:
        print("(No sizes found in menu.)")
        return 0
    if not prices:
        print("(No prices found in menu.)")
        return 0

    # FIX: avoid index errors if the menu file has mismatched counts.
    count = min(len(sizes), len(prices))
    for i in range(count):
        print(f"{i+1}.  Size: {sizes[i]}         Price: $  {prices[i]:.2f}")
    return count


def print_prices(prices, sizes):
    # Backwards-compatible alias: older code may still call print_prices().
    return print_sizes(prices, sizes)


def print_milks(milks):
    print("Milks\n")
    for idx, item in enumerate(milks, start=1):
        print(f"{idx}.\t{item}")
    # FIX: return number of options displayed (not character count).
    return len(milks)


def print_flavors(flavors):
    print("Flavors\n")
    for idx, item in enumerate(flavors, start=1):
        print(f"{idx}.\t{item}")
    # FIX: return number of options displayed (not character count).
    return len(flavors)
