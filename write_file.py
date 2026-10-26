"""
writing to files
"""

# create and write to a file
# timestamps
import datetime


def write_header(right_now):

    # old way
    # file = open("menu.txt", "w")
    # file.write("-----Coffee Menu------\n")
    # file.close()

    # new - self closing way
    with open("menu.txt", "w") as f:
        f.write(f"{right_now}\n")
        f.write("-----Specials----\n")


def append_lines():
    with open("menu.txt", "a") as f:
        sandwich_specials = {
            "Monday": "Turkey Avocado Melt",
            "Tuesday": "Spicy Chicken Bacon Ranch",
            "Wednesday": "Roast Beef & Cheddar",
            "Thursday": "Caprese Panini",
            "Friday": "BBQ Pulled Pork",
            "Saturday": "Veggie Hummus Wrap",
            "Sunday": "Ham & Swiss on Rye",
        }

        for day, sandwich in sandwich_specials.items():
            f.write(f"{day}: {sandwich}\n")


def main():
    current_time = datetime.datetime.now()
    write_header(current_time)
    append_lines()


main()
