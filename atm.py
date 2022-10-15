# issue - add set password function to ATM.
import time

print("Please insert Your CARD")

# for card processing
time.sleep(5)


def set_password():
    temp = int(input("Enter Your New Pin : "))
    temp2 = int(input("Confirm Your new Pin : "))
    if (temp == temp2):
        global password
        password = temp2
        print("Your Pin is Successfully created")
    else:
        print("Pin do not matched.")


set_password()

print("-----Welcome to our bank-----")
# taking atm pin from user
pin = int(input("Enter your ATM pin : "))

# user account balance
balance = 5000

# checking pin is valid or not
if pin == password:
    # loop will run user get free
    while True:

        # Showing  info to user

        print(""" 
			1 == balance
			2 == withdraw balance
			3 == deposit balance
            4 == Set Password
			4 == exit
			"""
              )

        try:
            # taking an option from user
            option = int(input("Please enter your choice "))
        except:
            print("Please enter valid option")

        # for option 1
        if option == 1:
            print(f"Your current balance is {balance}")

        elif (option == 2):
            withdraw_amount = int(input("Please enter the Withdraw Amount"))
            if (withdraw_amount < balance):
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your updated balance is {balance}")
            else:
                print("Insufficient Balance.")

        elif option == 3:
            deposit_amount = int(input("Please enter Deposit Amount"))

            balance = balance + deposit_amount

            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is {balance}")

        elif option == 4:
            print("Thanks for Banking with us.")
            break
        else:
            print("Choose a valid option")


else:
    print("wrong pin Please try again")
