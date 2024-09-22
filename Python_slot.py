import random
def spin_row():
  symbols = ['🍒','🍉', '🍋', '⭐️', '🔔']

  result = [random.choice(symbols) for _ in range(3)]
  return result


def print_row(row):
  print("***************")
  print(" | ".join(row))
  print("***************")
def get_payout(row, bet):
  if row[0] == row[1] == row[2]:
    if row[0] == '🍒':
      return bet * 3
    elif row[0] == '🍉':
      return bet * 4
    elif row[0] == '🍋':
      return bet * 5
    elif row[0] == '🔔':
      return bet * 10
    elif row[0] == '⭐️':
      return bet * 20
  return 0


def main():
  balance = 100
  print("********")
  print("Welcome to python slots")
  print("symbols: 🍒 🍉 🍋 ⭐️ 🔔")
  print("********")

  while balance > 0:
    print(f"current balance: {balance}₹")
    bet = input("place your bet amount: ")

    if not bet.isdigit():
      print("please enter a valid amount: ")

    bet = int(bet)

    if bet > balance:
      print("insufficient balance")
      continue

    if bet <= 0:
      print("bet must be greater than 0")

    balance -= bet

    row = spin_row()
    print("spinning....\n")
    print_row(row)

    payout = get_payout(row, bet)

    if payout > 0:
      print(f"you won {payout}₹")
    else:
      print("sorry you lost this round")


    balance += payout

    play_again = input("do you want to play again? (Y/N)").upper()

    if play_again != 'Y':
      break

  print(f"Game over! Your final BALANCE Is {balance}₹")
if __name__ == '__main__':
  main()
