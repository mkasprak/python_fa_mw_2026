def read_menu():
    menus = {}
    try:
        with open("menu.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail

        return menus
    except FileNotFoundError:
        print('Please create file or check file name. It should be "menu.txt"')
    except IndexError:
        return menus
    except Exception as e:
        print(e)


def split_into_variables(menu_items):
    coffee = menu_items.get("COFFEE")
    prices = menu_items.get("PRICES")
    milks = menu_items.get("MILK")
    flavors = menu_items.get("FLAVORS")
    shots = menu_items.get("SHOTS")
    return coffee, prices, milks, flavors, shots


def print_coffee(coffee):
    print("Coffee\n")
    count = 1
    coffee_item = coffee.split(",")
    print("\nCoffee:")
    for item in coffee_item:
        print(f"{count}. \t{item.strip()}")
        count += 1
    return len(coffee)

def print_prices(prices, sizes):
    print("Prices\n")
    count = 1
    price_item = prices.split(",")
    size_item = sizes.split(",")
    for i in range(0, price_item.len()):
        print(f"{count}.  Size: {size_item[i]}         Price: $  {price_item[i]:.2f}")
        count += 1
    return len(prices)
    

def print_milks(milks):
    print("Milks\n")
    count = 1
    milks_item = milks.split(",")
    for item in milks_item:
        print(f"{count}.\t{item.strip()}")
        count += 1
    return len(milks)


def print_flavors(flavors):
    print("Flavors\n")
    count = 1
    flavors_item = flavors.split(",")
    for item in flavors_item:
        print(f"{count}.\t{item.strip()}")
        count += 1  
    return len(flavors)      

   


