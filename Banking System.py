menu = """
[d] Deposit 
[s] Withdraw 
[e] Statement 
[q] Quit

=> """

balance = 0 
limit = 500 
statement = "" 
withdrawal_count = 0 
WITHDRAWAL_LIMIT = 3

while True:

option = input(menu)

if option == "d":
    amount = float(input("Enter the deposit amount: "))

    if amount > 0:
        balance += amount
        statement += f"Deposit: $ {amount:.2f}\n"

    else:
        print("Operation failed! The amount entered is invalid.")

elif option == "s":
    amount = float(input("Enter the withdrawal amount: "))

    exceeded_balance = amount > balance
    exceeded_limit = amount > limit
    exceeded_withdrawals = withdrawal_count >= WITHDRAWAL_LIMIT

    if exceeded_balance:
        print("Operation failed! You don't have enough balance.")

    elif exceeded_limit:
        print("Operation failed! The withdrawal amount exceeds the limit.")

    elif exceeded_withdrawals:
        print("Operation failed! Maximum number of withdrawals exceeded.")

    elif amount > 0:
        balance -= amount
        statement += f"Withdrawal: $ {amount:.2f}\n"
        withdrawal_count += 1

    else:
        print("Operation failed! The amount entered is invalid.")

elif option == "e":
    print("\n================ STATEMENT ================")
    print("No transactions have been made." if not statement else statement)
    print(f"\nBalance: $ {balance:.2f}")
    print("==========================================")

elif option == "q":
    break

else:
    print("Invalid operation, please select the desired operation again.")
