# VIEW PROFILE


def view_profile(emp_id):

    emp = employees[emp_id]

    print("\n========== EMPLOYEE PROFILE ==========")
    print("Employee ID :", emp_id)
    print("Name        :", emp["name"])
    print("Email       :", emp["email"])
    print("Department  :", emp["department"])
    print("Designation :", emp["designation"])
    print("Salary      :", emp["salary"])
    print("======================================")