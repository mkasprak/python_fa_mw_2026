"""
lists, arrays, vectors, tuples

python - lists are mutable, tuples are immutable
other languages have arrays and vectors

"""

# ℹ️ INFO: A list stores multiple values in one variable.
# 💡 TIP: Lists use square brackets, and each item is separated by a comma.
# ℹ️ INFO: During the lecture, comment out each example after demonstrating it before moving on.
# At the end, uncomment the examples so students can see the complete program.

dwarves = ["Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"]

# ℹ️ INFO: A for loop visits each item in the list one at a time.
for dwarf in dwarves:
    print(dwarf)

# 💡 TIP: List indexes start at 0, so index 2 refers to the third item.
# print(dwarves[2])
college_classes = [
    "Introduction to Psychology",
    "Calculus I",
    "World History",
    "General Chemistry",
    "English Composition",
    "Microeconomics",
    "Introduction to Programming",
    "Spanish II",
    "Organic Chemistry",
    "Statistics",
]


# ℹ️ INFO: append() adds one new item to the end of a list.
college_classes.append("Web Design")

# ℹ️ INFO: This loop prints every class in the list.
for item in college_classes:
    print(item)


# ℹ️ INFO: pop(index) removes the item at the given index.
# 💡 TIP: Without an index, pop() removes the last item.
# ℹ️ INFO: pop(3) removes the fourth item because list indexes start at 0.

college_classes.pop(3)
print("\n\n")
for item in college_classes:
    print(item)


# ℹ️ INFO: remove(value) removes the first matching value from a list.
# ⚠️ WARNING: remove() raises a ValueError if the value is not in the list.
try:
    college_classes.remove("Calculus I")
    for item in college_classes:
        print(item)
except ValueError:
    print("Sorry, that is not in my list ")


# 💡 TIP: len() tells us how many items are currently in the list.
print(len(college_classes))


# ℹ️ INFO: The in operator checks whether a value is in a list.
if "Sleepy" in dwarves:
    print("Yes, Sleepy is a dwarf")

# ⚠️ WARNING: Assigning one list to another variable does not make a copy.
# 💡 TIP: Both variable names will point to the same list.
# The guest_list name represents the Thanksgiving guest list.
# Try this first during the lecture:
# guest_list = dwarves
# guest_list.append("Snarky")
# print(dwarves)  # The original list also has Snarky.

# 💡 TIP: [:] creates a separate copy of the list.
# Add Snarky to the copy and then print dwarves to show that the original is unchanged.
guest_list = dwarves[:]
for person in guest_list:
    print(person)


guest_list.append("Snarky")

# ℹ️ INFO: Adding Snarky to the copy does not change the original list.
for dwarf in dwarves:
    print(dwarf)


# 💡 TIP: A slice [start:stop] copies items from start up to, but not including, stop.
# This slice creates a new list containing dwarves at indexes 2, 3, 4, and 5.
# Adding sarcastic to guests will not add it to dwarves because guests is a separate list.
guests = dwarves[2:6]

guests.append("sarcastic")

for dwarf in guests:
    print(dwarf)

# ℹ️ INFO: sort() arranges the items in a list in alphabetical order.
guests.sort()
print("\n\n")
for dwarf in guests:
    print(dwarf)
