def transfer(sender: int, receiver: int, transfer_amount: int):

    if receiver not in users:
        print("Receiver Account Not Found")
        return

    if transfer_amount <= users[sender]["balance"]:

        users[sender]["balance"] -= transfer_amount
        users[receiver]["balance"] += transfer_amount

        print("Transfer Successful")
        print(f"Available Balance : {users[sender]['balance']}")

    else:
        print("Insufficient Balance")