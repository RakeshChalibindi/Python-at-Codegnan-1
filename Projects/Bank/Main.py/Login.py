def login(account: int, password: str) -> bool:

    if account in users:

        if users[account]["password"] == password:
            print("\nLogin Successful")
            return True

        else:
            print("Incorrect Password")
            return False

    else:
        print("Account Not Found")
        return False
