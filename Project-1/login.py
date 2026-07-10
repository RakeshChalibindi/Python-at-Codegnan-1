# LOGIN

def login(emp_id, password):

    if emp_id in employees:

        if employees[emp_id]["password"] == password:
            print("\nLogin Successful")
            return True

        else:
            print("Incorrect Password")
            return False

    else:
        print("Employee Not Found")
        return False