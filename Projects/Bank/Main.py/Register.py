def register(name: str, email: str, initial_deposit: int, password: str):

    account = max(users.keys()) + 1

    users[account] = {
        "name": name,
        "Email": email,
        "balance": initial_deposit,
        "password": password
    }

    print("\nRegistration Successful")
    print(f"Your Account Number is : {account}")