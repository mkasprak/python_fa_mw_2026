"""
    imported into main. 

"""



def print_label(order_num, employee_id):
    # TODO we need to read order_num and employee_id into dictionaries
    # TODO (Week 12 - file I/O lesson): read the saved employee + order from files using IDs, then print.

    # Temp placeholder:
    employee = {}
    order = {}
    # Plan:
    # 1) Create the label text (employee + order details).
    # 2) Print the label to the screen (or to a printer later).
    # ℹ️ If `employee` is a dictionary, looping over it gives you the KEYS.
    # We use each key to print both the key and the value.
    for key in employee:
        print(f"{key}: {employee[key]}")
    for item in order:
        print(item)
    # 3) Ask if they also want a receipt.
    receipt = input("Would you like a receipt (y/n)?  ").strip().lower()
    if receipt == "y":
        # TODO (Week 12): choose a consistent receipt filename/location (ex: final_project\\receipt.txt).
        with open("final_project\\receipt", "w") as f:
            # note - write because we want a new one each time not a history
            for key in employee:
                f.write(f"{key}: {employee[key]}")
            for item in order:
                f.write(item)
    # 4) Print the receipt if requested.
