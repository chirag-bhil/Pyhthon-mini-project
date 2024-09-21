def show_balance():
  print(f"your balance is {balance:.2f}₹")

def deposit():
  amount = float(input("enter Amount to be deposited: "))
  if amount < 0:
    print("that is not a valid amount")
  else:
    return amount
def withdraw():
  amount = float(input("enter Amount to be withdraw: "))
  
  if amount > balance:
    print("insufficient balance")
  elif amount < 0:
    print("amount must be greater than 0")
  else:
    
    return amount

balance = 0
is_running = True

while is_running:
  print("Banking program")
  print("1.show balance")
  print("2.deposit")
  print("3.Withdraw")
  print("4.exit")
  
  choice = input("enter your choice(1-4)")
  
  if choice == '1':
    show_balance()
  elif choice == '2':
    
    new = deposit()
    balance += new
    print(f"{new}₹ deposited in your bank account")

    
  elif choice == '3':
    balance -= withdraw()
  elif choice == '4':
    is_running = False
  else:
    print("This is not valid choice")

print("thank you have a nice day")
