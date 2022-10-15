class Account:
    def __init__(self):
        self.balance = 0
        print('Your Account is Created.')

    def deposit(self):
        amount = int(input('Enter the amount to deposit:'))
        self.balance += amount

    def withdraw(self):
        amount = int(input('Enter the amount to withdraw:'))
        if (amount > self.balance):
            print('Insufficient Balance!')
        else:
            self.balance -= amount

    def showbalance(self):
        print(f"Your Balance : {self.balance}")


print("<------------------------------------------------------------------>")
account = Account()
print("<------------------------------------------------------------------>")
cond = True
while (cond):
    option = int(input(
        "0) Exit \n1) Deposit Money \n2) Withdraw Money \n3) Show Balance \nChoose any Number Above : "))
    if (option == 0):
        print("Thanks for Banking with us.")
        cond = False
    elif (option == 2):
        account.withdraw()
        account.showbalance()
    elif (option == 1):
        account.deposit()
        account.showbalance()
    elif (option == 3):
        account.showbalance()
    else:
        print("Choose a Valid Option.")
    print("<------------------------------------------------------------------>")
