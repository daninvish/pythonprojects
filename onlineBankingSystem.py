def deposit(account_balance):
    if option == 2:
        try:
            deposit_amount = int(input("Enter the amount you want to deposit: "))
            account_balance += deposit_amount
            print(f"Deposit successful. New balance: ${account_balance}\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return account_balance

def withdraw(account_balance):
    if option == 3:
        try:
            withdraw_amount = int(input("Enter the amount you want to withdraw: "))
            if withdraw_amount <= account_balance:
                account_balance -= withdraw_amount
                print(f"Withdrawal successful. New balance: ${account_balance}")
            else:
                print("Insufficient funds.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return account_balance

def balance(account_balance):
    if option == 1:
        print(f"Your account balance is: ${account_balance}")

def exit():
    print("Exiting the banking system...")

# Initialize account balance
account_balance = 0  # Replace with actual initial balance

print("#############################################\n")
print("########### ONLINE BANKING SYSTEM ###########\n")
print("#############################################\n")
print("Welcome to Centenary Mobile Banking System\n")
while True:
    print("Please select any option from 1 to 4: ")
    print('1: Check Account Balance\n'
          '2: Make Deposit\n'
          '3: Withdraw Money\n'
          '4: Exit')

    try:
        option = int(input("Select option: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 4.")
        continue

    if option == 1:
        balance(account_balance)
    elif option == 2:
        account_balance = deposit(account_balance)
    elif option == 3:
        account_balance = withdraw(account_balance)
    elif option == 4:
        exit()
        break
    else:
        print("Invalid option. Please try again.")