# MAIN PROGRAM

if __name__ == "__main__":

    while True:

        print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
        print("1. Register Employee")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter Your Choice : "))

        if choice == 1:

            name = input("Enter Name : ")
            email = input("Enter Email : ")
            department = input("Enter Department : ")
            designation = input("Enter Designation : ")
            salary = int(input("Enter Salary : "))
            password = input("Create Password : ")

            register(
                name,
                email,
                department,
                designation,
                salary,
                password
            )

        elif choice == 2:

            emp_id = int(input("Enter Employee ID : "))
            password = input("Enter Password : ")

            login_status = login(emp_id, password)

            while login_status:

                print("\n========== EMPLOYEE MENU ==========")
                print("1. View Profile")
                print("2. Update Department")
                print("3. Update Designation")
                print("4. Update Salary")
                print("5. Change Password")
                print("6. Delete Employee")
                print("7. Logout")

                option = int(input("Enter Your Choice : "))

                if option == 1:

                    view_profile(emp_id)

                elif option == 2:

                    department = input("Enter New Department : ")

                    update_department(emp_id, department)

                elif option == 3:

                    designation = input("Enter New Designation : ")

                    update_designation(emp_id, designation)

                elif option == 4:

                    salary = int(input("Enter New Salary : ")

                    )

                    update_salary(emp_id, salary)

                elif option == 5:

                    password = input("Enter New Password : ")

                    change_password(emp_id, password)

                elif option == 6:

                    confirm = input("Are You Sure (yes/no) : ")

                    if confirm.lower() == "yes":

                        login_status = delete_employee(emp_id)

                elif option == 7:

                    login_status = logout()

                else:

                    print("Invalid Choice")

        elif choice == 3:

            print("Thank You for Using Employee Management System")
            break

        else:

            print("Invalid Choice")