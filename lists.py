"""
lists, arrays, vectors, tuples

python - lists are muteable, tuples are immutable
other languages have arrays and vectors

"""

# ℹ️ INFO: A list stores multiple values in one variable.
# 💡 TIP: Lists use square brackets, and each item is separated by a comma.

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
# 💡 TIP: [:] creates a separate copy of the list.
vertically_challenged = dwarves[:]
for person in vertically_challenged:
    print(person)


vertically_challenged.append("Snarky")

# ℹ️ INFO: Adding Snarky to the copy does not change the original list.
for dwarf in dwarves:
    print(dwarf)


# 💡 TIP: A slice [start:stop] copies items from start up to, but not including, stop.
v_c = dwarves[2:6]

v_c.append("saracastic")

for dwarf in v_c:
    print(dwarf)

# ℹ️ INFO: sort() arranges the items in a list in alphabetical order.
v_c.sort()
print("\n\n")
for dwarf in v_c:
    print(dwarf)
