# This is a basic banking system implementation in Python that allows users to create accounts, log in, deposit and withdraw funds, check balances, and view mini statements. The system consists of two classes: Account and BankingSystem.

#         ***BANKING MANAGEMENT SYSTEM***

# Class to represent a user's bank account
class Account:
    # Constructor to initialize username, password, and balance (default is 0)
    def __init__(self, username, password, balance=0):
        self.username = username  # Account holder's username
        self.password = password  # Account password for login
        self.balance = balance    # Account balance

    # Method to deposit an amount into the account
    def deposit(self, amount):
        self.balance += amount  # Add the deposited amount to the current balance
        print(f"\nAmount deposited: {amount}")
        print(f"Total Balance: {self.balance}")

    # Method to withdraw an amount from the account
    def withdraw(self, amount):
        # Check if there is enough balance to withdraw
        if self.balance >= amount:
            self.balance -= amount  # Deduct the withdrawn amount
            print(f"\nAmount withdrawn: {amount}")
            print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient balance")  # Print error if balance is insufficient

    # Method to get the current balance
    def get_balance(self):
        return self.balance  # Return the current balance

    # Method to display a mini statement with username and balance
    def get_mini_statement(self):
        print("\n--- Mini Statement ---")
        print(f"Username: {self.username}")
        print(f"Current Balance: {self.balance}")


# Class to manage the banking system (accounts, login, etc.)
class BankingSystem:
    # Constructor to initialize an empty dictionary for accounts
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts (username as key, Account object as value)

    # Method to create a new account
    def create_account(self, username, password):
        # Check if the username already exists
        if username in self.accounts:
            print("Username already exists!")  # Print error if username is taken
        else:
            # Create a new Account object and add it to the accounts dictionary
            self.accounts[username] = Account(username, password)
            print("\nAccount created successfully. Welcome to BVK Bank!")

    # Method to login to an account
    def login(self, username, password):
        # Retrieve the account associated with the given username
        account = self.accounts.get(username)

        # Check if the account exists and the password is correct
        if account and account.password == password:
            print("Login successful!")  # Login successful message
            return account  # Return the account object
        else:
            print("Invalid username or password.")  # Print error if login fails
            return None


# Main function to run the program
def main():
    bank = BankingSystem()  # Create a BankingSystem object

    # Infinite loop for the main menu
    while True:
        print("\n--- Main Menu ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-3): ")

        # Option 1: Create a new account
        if choice == '1':
            username = input("Enter a username: ")  # Prompt for username
            password = input("Enter a password: ")  # Prompt for password
            bank.create_account(username, password)  # Call create_account method

        # Option 2: Login to an existing account
        elif choice == '2':
            username = input("Enter your username: ")  # Prompt for username
            password = input("Enter your password: ")  # Prompt for password
            account = bank.login(username, password)  # Attempt to login

            # If login is successful, display the banking menu
            if account:
                while True:
                    print("\n--- BVK Bank Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Mini Statement")
                    print("5. Logout")

                    # Get the user's choice from the banking menu
                    user_choice = input("Enter your choice (1-5): ")

                    # Option 1: Deposit money
                    if user_choice == '1':
                        amount = int(input("Enter amount to deposit: "))  # Prompt for deposit amount
                        account.deposit(amount)  # Call the deposit method

                    # Option 2: Withdraw money
                    elif user_choice == '2':
                        amount = int(input("Enter amount to withdraw: "))  # Prompt for withdrawal amount
                        account.withdraw(amount)  # Call the withdraw method

                    # Option 3: Check balance
                    elif user_choice == '3':
                        print(f"Current Balance: {account.get_balance()}")  # Display the current balance

                    # Option 4: Print mini statement
                    elif user_choice == '4':
                        account.get_mini_statement()  # Call the mini statement method

                    # Option 5: Logout
                    elif user_choice == '5':
                        print("\nThank you for using BVK Bank. Logging out...")
                        break  # Exit the inner loop (logout)

                    # Invalid choice in the banking menu
                    else:
                        print("Invalid choice. Please try again.")

        # Option 3: Exit the program
        elif choice == '3':
            print("\nThank you for using BVK Bank. Goodbye!")
            break  # Exit the outer loop (end program)

        # Invalid choice in the main menu
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the main function
if __name__ == "__main__":
    main()
