"""
constants vs tuples
"""

# A tuple stores values in a fixed order. The comma makes this a one-item tuple.
SCHOOL_NAME = ("McHenry County College",)

print(SCHOOL_NAME)


# Tuples are immutable, so this creates a new tuple and reassigns the name.
# It does not modify the original tuple, just as replacing a string does not
# modify the original string.
SCHOOL_NAME = ("Elgin Community College",)

print(SCHOOL_NAME)

# This is not allowed because tuples cannot be changed after they are created.
# SCHOOL_NAME.pop()

# len tells us how many items are in the tuple.
print(len(SCHOOL_NAME))
