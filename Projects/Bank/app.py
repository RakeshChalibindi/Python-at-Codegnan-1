

# user tables

users = {
    1234:{"name":"Rakesh","Email":"naidurakesh357@gmail.com","balance":100000,"password":"1234"},
    1235:{"name":"srinu","Email":"chalibindirakesh357@gmail.com","balance":200000,"password":"1235"}
    }



# service

def register(name:str,email:str,initial_deposite:int,password:str):
    pass


#register

def login(account:int,password:str)->bool:
    pass


#balance function defination

def balance(account:int)->int:
    pass


#withdraw function defination

def withdraw(account:int, withdraw_amount:int)->str:
    pass

#Deposite function defination

def deposite(account:int, deposite_amount:int):
    pass


# Transfer function defination

def transfer(sender:int, reciever:int, transfer_amount:int):
    pass


# Ministatement function defination

def ministatement(account:int):
    pass

# logout function defination

def logout():
    pass



# main function

if __name__ == "__main__":


    print("Welcome to the small scale bank")
    print("1. Register \n 2.Login")
    choice = int(input("select your choice:"))

    #calling register function

    if choice == 1:
        print("Registation page under development process.....")

    #calling login function

    elif choice == 2:
        account = int(input("Enter your account number:"))
        password = input("Enter your password:")
        login_val = login(account=account, password=password)
        
        while login_val:
            print("The small scale Bank providing services")
            print("1. Balance \n 2. Withdrawal \n 3.Deposite \n 4.Transfer \n 5.Ministatement \n 6.Logout")
            choice = int(input("Enter your choice(1-6):"))

            if choice == 1:
                # call balance function
                current_balance = balance(account=account)
                print("Current Balance is:{current_balance}")


            elif choice == 2:
                amount = int(input("Enter your withdraw amount:"))
                #call  withdraw function
                res = withdraw(account=account,withdraw_amount=amount)
                print(res)

            
