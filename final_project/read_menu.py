"""
Reads `menu.txt` and prints menu choices.

🧠 Student style (kept on purpose):
- Keep menu values as strings (like "A, B, C") and use `.split(",")` when needed.
- Avoid helper functions like `_split_csv` so this matches what we covered in class.

✅ Small fixes (Codex):
- Fix `.len()` bug (use `len(list)`).
- Return the number of options displayed (not the number of characters in the string).
"""


def read_menu():
    menus = {}
    try:
        # 💾 Keep it simple: read the menu file from the final_project folder.
        with open("final_project\\menu.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail

        return menus
    except FileNotFoundError:
        print('Please create file or check file name. It should be "menu.txt"')
        return menus
    except IndexError:
        return menus
    except Exception as e:
        print(e)
        return menus


def split_into_variables(menu_items):
    coffee = menu_items.get("COFFEE")
    prices = menu_items.get("PRICES")
    milks = menu_items.get("MILK")
    flavors = menu_items.get("FLAVORS")
    sizes = menu_items.get("SIZES")
    return coffee, prices, milks, flavors, sizes


def print_coffee(coffee):
    # 🖨️ Display coffee choices and return how many options there are.
    print("Coffee\n")
    count = 1
    coffee_item = coffee.split(",")
    print("\nCoffee:")
    for item in coffee_item:
        print(f"{count}. \t{item.strip()}")
        count += 1
    return len(coffee_item)


def print_sizes(prices, sizes):
    # 🖨️ Display sizes + prices and return how many options there are.
    print("Sizes\n")
    count = 1
    price_item = prices.split(",")
    size_item = sizes.split(",")

    # ⚠️ Use the shorter length so it doesn't crash if menu.txt has mismatched counts.
    options = len(size_item)
    if len(price_item) < options:
        options = len(price_item)
    for i in range(0, options):
        print(
            f"{count}.  Size: {size_item[i].strip()}         Price: $ {price_item[i].strip()}"
        )
        count += 1
    return options


def print_prices(prices, sizes):
    # Backwards-compatible name if older code calls print_prices()
    return print_sizes(prices, sizes)


def print_milks(milks):
    print("Milks\n")
    count = 1
    milks_item = milks.split(",")
    for item in milks_item:
        print(f"{count}.\t{item.strip()}")
        count += 1
    return len(milks_item)


def print_flavors(flavors):
    print("Flavors\n")
    count = 1
    flavors_item = flavors.split(",")
    for item in flavors_item:
        print(f"{count}.\t{item.strip()}")
        count += 1
    return len(flavors_item)
