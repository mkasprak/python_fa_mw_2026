"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# 🧺 GLOBAL CONSTANTS (The Pantry)
# ℹ️ Tuples keep these menu choices together; the values are not changed by this program.
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

# 💡 TODO: Define get_price(size) to match the requested size with its price.
def get_price(size):
    # ℹ️ match checks the size against each case from top to bottom.
    match size:
        case "small":
            return 3.0
        case "medium":
            return 4.0
        case "large":
            return 5.0
        # ℹ️ _ is the default case when none of the sizes above match.
        case _:
            print("invalid entry")
            return 0

# 💡 TODO: Define blend(size, base, fruit, scoops) to display the smoothie order.

# 💡 TODO: Define main() to collect input and call the smoothie functions.
def main():
    # ℹ️ input() gives us text; this value is used to look up the price.
    try:
        size = input("What size smoothie do you want (small, medium, large): ")
        price = get_price(size)

main()