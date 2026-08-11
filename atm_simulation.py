user = "Name@123"
uname = input("enter ur username : ")
upper: int = 0
lower: int = 0
digits: int = 0
special: int = 0
count: int = 0
if user == uname:
    pwd = input("enter ur password : ")
    if len(pwd) >= 8:
        for i in pwd:
            if i == " ":
                count += 1
        if count == 0:
            for i in pwd:
                if i.isupper() == True:
                    upper += 1
                elif i.islower() == True:
                    lower += 1
                elif i.isdigit() == True:
                    digits += 1
                else:
                    special += 1
        if upper > 0 and lower > 0 and digits > 0 and special > 0:
            print("\n")
            print("login successful!!")
            balance = 10000
            while True:
                print("\n")
                print("*" * 10)
                print("1. withdraw")
                print("2. deposit")
                print("3. balance")
                print("4. exit")
                print("*" * 10)
                print("\n")
                choice = int(input("Please enter your choice : "))
                if choice == 1:
                    try:
                        withdraw = int(
                            input("Please enter the amount u want to withdraw : ")
                        )
                        if withdraw <= balance:
                            balance = balance - withdraw
                            print("withdraw successful!!")
                        else:
                            print("Insufficient balance !!")
                    except ValueError:
                        print("Invalid input!! Please enter a valid amount.")
                elif choice == 2:
                    try:
                        deposit = int(input("Please enter the amount u want to deposit : "))
                        if deposit > 0:
                            balance = balance + deposit
                            print("Deposit successful!!")
                        else:
                            print("Invalid input!! Please enter a valid amount.")
                    except ValueError:
                        print("Invalid input!! Please enter a valid amount.")
                elif choice == 3:
                    print(f"Your current balance : {balance}")
                elif choice == 4:
                    print("Thank you for using our services!!")
                    break
                else:
                    print("invalid choice!!")
        else:
            print("Signup failed!!")
    else:
        print("Short password!!")
else:
    print("Invalid username!!")
