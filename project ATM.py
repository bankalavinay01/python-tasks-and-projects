 #     *** PROJECT- ATM ***

balance = 100000

def credit():
    amount = int(input("Enter the amount to credit: "))
    global balance
    balance += amount
    print(f"Credited successfully. Your new balance is {balance}.")

def debit():
    amount = int(input("Enter the amount to debit: "))
    global balance
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"Debited successfully. Your new balance is {balance}.")

def show_balance():
    print(f"Your current balance is {balance}.")

def generate_pin():
    pin = input("Enter a new PIN: ")
    print("PIN generated successfully.")

while True: 
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Check Balance")
    print("4. Generate PIN")
    print("5. Exit")
    
    option = input("Enter your choice: ")
    
    if option == "1":
        credit()
    elif option == "2":
        debit()
    elif option == "3":
        show_balance()
    elif option == "4":
        generate_pin()
    elif option == "5":
        print("Thank you for visiting!")
        break
    else:
        print("Invalid option. Please enter a number between 1 and 5.")