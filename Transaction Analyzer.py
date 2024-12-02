def print_transactions(transactions):
  for transaction in transactions:
    amount = transaction[0]
    statement = transaction[1]
    print(f"${amount} - {statement}")


def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_withdrawn = sum(deposits)
  print("Total withdrawn: ", total_withdrawn)

  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_deposited = sum(withdrawals)
  print("Total deposited: ", total_deposited)

  balance = total_deposited + total_withdrawn
  print("Balance: ", balance)


def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print("Largest withdrawal: ", largest_withdrawal, "\nLargest deposit: ", largest_deposit)

  deposit = [transaction[0] for transaction in transactions if transaction[0] > 0]
  total_deposit = sum(deposit)
  if len(deposit) > 0:
    average_deposit = total_deposit/len(deposit)
  elif len(deposit) == 0:
    average_deposit = 0
  print("Average deposit: ", average_deposit)

  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawals = sum(withdrawals)
  if len(withdrawals) > 0:
    average_withdrawals = total_withdrawals/len(withdrawals)
  elif len(withdrawals) == 0:
    average_withdrawals = 0
  print("Average withdrawals: ", average_withdrawals)


data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

while True:
  print("\nYou have options: print, analyze, stop")
  choice = input("Enter your choice ")
  if choice == "print":
    print_summary(data)
  elif choice == "analyze":
    analyze_transactions(data)
  elif choice == "stop":
    break
  else:
    print("Invalid choice")

