"""
writing to files
"""

# create and write to a file
# ℹ️ We can also add a timestamp (date + time) to show when the file was generated.
import datetime


def write_header(right_now):
    # 💾 Write mode ("w") makes a brand-new file OR overwrites the old one.
    # ⚠️ If you run the program again, anything that was in menu.txt gets replaced.

    # old way
    # file = open("menu.txt", "w")
    # file.write("-----Coffee Menu------\n")
    # file.close()

    # new - self closing way
    # 💡 `with open(...) as f:` auto-closes the file for you when you're done.
    with open("menu.txt", "w") as f:
        # 🖨️ `f.write(...)` sends text into the file (not the screen).
        f.write(f"{right_now}\n")
        f.write("-----Specials----\n")


def append_lines():
    # 💾 Append mode ("a") adds new lines to the end of the file.
    with open("menu.txt", "a") as f:
        # ℹ️ A dictionary (dict) stores key → value pairs.
        # ℹ️ Here: day of week → sandwich special.
        sandwich_specials = {
            "Monday": "Turkey Avocado Melt",
            "Tuesday": "Spicy Chicken Bacon Ranch",
            "Wednesday": "Roast Beef & Cheddar",
            "Thursday": "Caprese Panini",
            "Friday": "BBQ Pulled Pork",
            "Saturday": "Veggie Hummus Wrap",
            "Sunday": "Ham & Swiss on Rye",
        }

        # 💡 `.items()` lets us loop through BOTH the key and the value each time.
        for day, sandwich in sandwich_specials.items():
            f.write(f"{day}: {sandwich}\n")


def main():
    # ▶️ main() is our program's starting function.
    # ℹ️ `datetime.datetime.now()` gives the current date + time (right now).
    current_time = datetime.datetime.now()
    write_header(current_time)
    append_lines()


# ▶️ Start the program by calling main().
main()
