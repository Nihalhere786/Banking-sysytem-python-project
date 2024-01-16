class Banking_system:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self, entered_pin):
        return entered_pin == self.pin

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited Rs{amount}. Current balance: Rs{self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdraw Rs{amount}. Current balance: Rs{self.balance}"
        else:
            return "Insufficient fund. Withdrawal failed."

def main():
    account_number = "16340100023999"
    pin = "1999"
    current_balance = 10000

    user_account = Banking_system(account_number, pin, current_balance)

    # Login
    entered_pin = input("Enter your PIN: ")
    if user_account.login(entered_pin):
        print("Login successful,Welcome to Indian Bank!")
    else:
        print("Incorrect PIN")
        return

    while True:
        print("\nselect your transaction:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Exit")

        choice = input("Enter your transaction (1/2/3): ")

        if choice == "1":
            withdraw_amount = float(input("Enter the Withdrawal amount: "))
            print(user_account.withdraw(withdraw_amount))
        elif choice == "2":
            deposit_amount = float(input("Enter the Deposit amount: "))
            print(user_account.deposit(deposit_amount))
        elif choice == "3":
            print("Thank You for using Indian Bank")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3"
                  ".")

if __name__ == "__main__":
    main()