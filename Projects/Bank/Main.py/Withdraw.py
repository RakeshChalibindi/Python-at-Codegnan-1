def withdraw(account: int, withdraw_amount: int) -> str:

    if withdraw_amount <= users[account]["balance"]:

        users[account]["balance"] -= withdraw_amount

        return f"Withdrawal Successful\nAvailable Balance : {users[account]['balance']}"

    else:
        return "Insufficient Balance"