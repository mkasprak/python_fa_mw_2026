"""
    called by main - handles creating confirming and looking up employees
"""
import os
import datetime

def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")




def get_employee():
    
    id = int(input("Please enter your ID number:  "))
    # TODO lookup employee
    f_name = input("Please enter your first name:  ")
    l_name = input("Please enter your last name:  ")
    office_nbr = input("Office to deliver to:  ")
    extension = input("Please enter extension:  ")
    known_allergies = input(
        "Please enter any known food allergies or sensitivities separated by commas:  "
    )
    
    employee_record = {
        "office": office_nbr,
        "extension": extension,
        "f_name": f_name,
        "l_name": l_name,
        "allergies": known_allergies,
    }

    
    with open("final_project\\employees.txt", "a") as f:
        f.write(f"{id}:{employee_record}\n")

    return id




def confirm_employee(employee_id, employee_record):
    
    while True:
        clear_screen()
        
        print(f"1.  Employee ID:  {employee_id}")
        print(f"2.  Office Number:  {employee_record['office']}")
        print(f"3.  Extension:  {employee_record['extension']}")
        print(f"4.  First Name:  {employee_record['f_name']}")
        print(f"5.  Last Name:  {employee_record['l_name']}")
        print(f"6.  Allergies: {employee_record['allergies']}")
      
        correct = input("Is this correct? (Y/N) ").strip().upper()
        if correct == "Y":
            break
        if correct != "N":
            input("Please enter Y or N. Press Enter to continue...")
            continue

        try:
            change = int(input("What number would you like to change? ").strip())
        except ValueError:
            input("Please enter a number (1-6). Press Enter to continue...")
            continue


        match change:
            case 1:
                while True:
                    try:
                        employee_id = int(input("New employee ID: ").strip())
                        break
                    except ValueError:
                        print("Employee ID must be a whole number.")
                        continue
                    except Exception as e:
                        right_now = datetime.datetime.now()
                        with open("final_project\\error.txt", "a") as f:
                            f.write(f"{right_now}:  {e}\n")
                        continue
            case 2:
                employee_record["office"] = input("New office number: ").strip()
            case 3:
                employee_record["extension"] = input("New extension: ").strip()
            case 4:
                employee_record["f_name"] = input("New first name: ").strip()
            case 5:
                employee_record["l_name"] = input("New last name: ").strip()
            case 6:
                employee_record["allergies"] = input("New allergies: ").strip()
            case _:
                input("Please choose a number 1-6. Press Enter to continue...")

    with open("final_project\\employees.txt", "a") as f:
            f.write(f"{id}:{employee_record}\n")
    

    return employee_id
