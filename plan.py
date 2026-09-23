"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

USER_NAMES = ("Bob", "Sue", "Tom")
passwords = ["0", "1", "2"]

#  just the change password logic/ code  choice 3


name = input("Please enter the user name:  ")
if name in USER_NAMES:
    # error checking
    # print(passwords) - error check
    location = USER_NAMES.index(name)
    password = input("Enter new password")
    passwords[location] = password
    print("Password has been changed")
    # print(passwords) - error check
