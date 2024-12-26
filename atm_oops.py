  #        ***ATM-OOPS***
from datetime import datetime

class ATM:
    def __init__(self):
        self.balance = 100000

    def show_menu(self):
        print("\nWelcome to BVK ATM")
        print("1. Credit amount")
        print("2. Debit amount")
        print("3. Balance enquiry")
        print("4. Exit")

    def get_option(self):
        return input("Choose an option: ")

    def credit_amount(self):
        amount = float(input("Enter credit amount: "))
        if amount > 0:
            self.balance += amount
            print("Amount credited successfully.")
            self.print_receipt("Credited", amount)
        else:
            print("Please enter a valid amount.")

    def debit_amount(self):
        amount = float(input("Enter withdrawal amount: "))
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            print("Amount debited successfully.")
            self.print_receipt("Debited", amount)
        else:
            print("Please enter a valid amount.")

    def balance_enquiry(self):
        print(f"Your current balance is: Rs {self.balance}/-")

    def print_receipt(self, transaction_type, amount):
        choice = input("Do you want a receipt? (Yes/No): ").lower()
        if choice == 'yes':
            print("\n", "BVK".center(30, " "))
            print("-" * 30)
            print(datetime.now())
            print(f"{transaction_type} amount: Rs {amount}/-")
            print(f"Current balance: Rs {self.balance}/-")
            print("-" * 30)
        else:
            print("Thank you for using BVK ATM.")

    def run(self):
        while True:
            self.show_menu()
            option = self.get_option()

            if option == '1':
                self.credit_amount()
            elif option == '2':
                self.debit_amount()
            elif option == '3':
                self.balance_enquiry()
            elif option == '4':
                print("Thank you for using BVK ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Run the ATM
atm = ATM()
atm.run()