def deposit(account: int, deposit_amount: int):

    users[account]["balance"] += deposit_amount

    print("Deposit Successful")
    print(f"Available Balance : {users[account]['balance']}")