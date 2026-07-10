# REGISTER
def register(name, email, department, designation, salary, password):

    emp_id = max(employees.keys()) + 1

    employees[emp_id] = {
        "name": name,
        "email": email,
        "department": department,
        "designation": designation,
        "salary": salary,
        "password": password
    }

    print("\nEmployee Registered Successfully")
    print("Employee ID :", emp_id)
