# pylint:disable=E1120
import random
import datetime
import time
import cmath
import os
from colorama import Fore, Back, Style
print("Hello", Fore.GREEN + input("Enter Your Name : "), "\n Welcome to ........")
print(Fore.RED)
time.sleep(random.randint(1, 3))


def main():
    print()
    print("    _    _     ____  _   _    _ ")
    print("   / \  | |   |  _ \| | | |  / \ ")
    print("  / _ \ | |   | |_) | |_| | / _ \ ")
    print(" / ___ \| |___|  __/|  _  |/ ___ \ ")
    print("/_/   \_\_____|_|   |_| |_/_/   \_\ ")
    print(Fore.YELLOW)
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")
    print(Fore.RED)

    print("The Mini Projects Toolsbox with PyThon")
    print(Fore.YELLOW)
    menulist = "\n".join(["Project List", "1 : Handsome Test Based On Numbers", "2 : Check Leap Year", "3 : Strong Password Generator ", "4 : When You will Be 100yrs", "5 : Calculate Your Current Age", "6 : Currency Converter",
                         "7 : Draw Table Of Any Number", "8 : Find Roots of Quadratic Equations", "9 : Guess The Number - Game ", "10: Number Magic Trick", " ", "Enter 100 to See My Info"])  # Menulist of main Programs in This scripy
    print("------------------------------------------------------------")  # For Design
    print(menulist)  # showing menulist
    print("------------------------------------------------------------")
    print(Fore.CYAN)
    # User Input To Run Next Script
    chs = int(input("Enter Any Choice From Above List ]->> "))
    print(Fore.GREEN)
    print()
    print()
    if chs == 1:  # Program 1
        print()
        print("Your choice is Handsome Test ")
        print()
        num = int(input("Enter any Number Related to You: > "))
        print(Fore.RED)
        print(" Sorry User We have Problem With  This Program On Your Device, \n We hope You will Like our other programs")
        print(Fore.GREEN)
        """first = num//10
		last = num % 10
		add = 0
		while first != 0:
		      a = first % 10
		      add = add+a
		      first = first//10
		      print()
		      if add == last:
		          print(" You are Handsome")
		      else:
		          print("You are Not Handsome")"""
    elif chs == 2:  # Program 2
        print()
        print("You Choose to Check Your Year is leap or not")
        print()
        leap = int(input("Enter Year your You want to Check Leap/Not Leap == "))
        print()
        if leap % 4 == 0:  # Dividing Year By 4 and Checking Reminder
            print(leap, " is the leap year")
        else:
            print(leap, " Is not a leap year")
        print()
    elif chs == 3:  # Program 3
        print("You Choose Password generator")
        print()
        pas1 = "qwertyuiopasdfghjklmnbvcxz1234567890"  # List Of characters
        # Number Of Charactrlers you want
        pas3 = int(input("How Much Long pass you want = "))
        # How Much Password You want
        pas2 = int(input("How many Password You want = "))
        print()
        print("Your Passwords are")
        for i in range(pas2):  # Getting range from pas2
            password = ' '
            for p in range(pas3):
                password += random.choice(pas1)  # Generating Random Tags
            print(password)
            # print("done")
            print()
    elif chs == 4:  # Program 4
        print("You Choose When Your will 100 years old")
        from datetime import datetime  # Importing Some Modules
        name = input("Enter you name:\t")  # Entering  Name and Age
        age = int(input("Enter age:\t"))
        # Subtracting Age From 100 date
        fyear = int((100-age) + datetime. now().year)
        print("At Year ", fyear)
        print('Hello %s. You are now %s years old. You will turn 100 years old in %s.' % (
            name, age, fyear))
    elif chs == 5:  # Program 5
        import datetime
        print("You Choose To Calculate your Current Age")
        print()
        birth_year = int(input("Enter your year of birth: \n"))
        birth_month = int(input("Enter your month of birth: \n"))
        birth_day = int(input("Enter your day of birth: \n"))
        current_year = datetime.date.today().year
        current_month = datetime.date.today().month
        current_day = datetime.date.today().day
        age_year = current_year - birth_year
        age_month = abs(current_month-birth_month)
        age_day = abs(current_day-birth_day)

        print("Your exact age is: ", age_year, "Years",
              age_month, "months and", age_day, "days")
    elif chs == 6:  # Program 6
        print("You Choose Currency Converter")
        print("This Tool will convert indian ruppies to EUR, GBP, JPY, AUD, CAD")
        ruppee = float(input("Enter How Much Ruppies You Want to convert = "))
        print("Converting.......")
        time.sleep(random.randint(1, 3))
        print("{}  Ruppies Will be \n {} EUR (EUROS) \n {} GBP (British Pounds) \n {} JPY (Japanese yen) \n {} AUD (Australian Doller) \n {} CAD (Canedian Doller)".format(
            ruppee,  ruppee*float(0.012), ruppee*float(0.0099), ruppee*float(1.49), ruppee*float(0.018), ruppee*float(0.017)))
    elif chs == 7:  # Program 7
        print("You choose to draw A Table Of Any Number")
        table = int(input("Enter the Number Which Table You want = "))
        print("The Table of ", table)
        print("Computing.......")
        time.sleep(random.randint(1, 3))
        for i in range(1, 11):
            print("{}    x    {}    =  {} ".format(table, i, table*i))
    elif chs == 8:  # Program 8
        print("You Choose To Solve A Quadratic Equation ")
        print()
        print("You Have Enter the Values Accroding to \n ax² + bx + = 0")
        a = float(input("Enter Value of a = "))
        b = float(input("Enter Value of b = "))
        c = float(input("Enter Value of c = "))
        print('Equation: %dx² + %dx + %d = 0' % (a, b, c))
        print("calculating......")
        time.sleep(random.randint(1, 3))
        D = b**2 - 4 * a * c
        print()
        print('Your Equations Roots:')
        print((-b - cmath.sqrt(D)) / (2 * a))
        print((-b + cmath.sqrt(D)) / (2 * a))
    elif chs == 9:  # Program 9
        maxn = 100
        n = random.randint(1, maxn)
        print('Welcome to guess the number game!')
        print('Guess the number from 1 to %d' % maxn)
        guess = None
        while guess != n:
            guess = int(input('Your try: '))
            if guess > n:
                print('Your Guess is Too high')
            if guess < n:
                print('Your Guesa is Too low')
        print('Congratulations,You Entered the Correct Number. \n You won!')
    elif chs == 10:  # Program 10
        #magicl = 2468
        magicn = random.randint(1, 11)
        print(" You Choose Magic Number Trick")
        print()
        time.sleep(4)
        print(" Here Guess A Number and put it in Your Head")
        print()
        time.sleep(4)
        print("Now Add Same Number Of your Friend In It ")
        print()
        time.sleep(5)
        print(" Now add {} in it ".format(magicn))
        print()
        time.sleep(5)
        print("Now Divide Your Answer by 2")
        time.sleep(4)
        print("Just Give Your Friend his Number back \n means Just subtract number from your answer ")
        print()
        time.sleep(5)
        print(" Now, I'm Guessing your answer.....")
        time.sleep(4)
        magicz = int(input(
            ("I Guessed Your answer \n Enter 0 if you want see my guessed answer |=> ")))
        if magicz == 0:
            print("Your Answer is {}".format(magicn/2))
        time.sleep(4)
        print()
        magicr = int(input("Enter 1 if i Guess correct or 0 for wrong - "))
        print()
        if magicr == 1:
            print("Thanks For Playing Our Game")
        else:
            print(" You Must Followed Wrong Step, Try again")
    elif chs == 100:
        print()

        print(Fore.GREEN)
        print("------------------------------------------------------------")
        print("------------------------------------------------------------")
        print()

        print("# ¥ About Me ¥")
        print("# Created by   :- Vinay Ghate")

        print(Fore.YELLOW)
    print()  # Add Options Before This
    print("------------------------------------------------------------")
    time.sleep(4)
    print(Fore.YELLOW)
    choise = int(input(
        "Enter Any Even Number To Open Main menu again \n and Odd Number To End This program \n >>>"))
    time.sleep(4)
    if (choise) >= 1:
        os.system('cls||clear')
        main()
        print("########################################")
    else:
        exit  # Want To print ###### line before this and also add if want run


main()
