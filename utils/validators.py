from core.constants import MIN_BET_AMOUNT, MAX_BET_AMOUNT

# Code to get the bet amount from user
def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? - ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET_AMOUNT <= amount <= MAX_BET_AMOUNT:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET_AMOUNT} and ${MAX_BET_AMOUNT}")
        else:
            print("Invalid input. Please enter a number.")

# Code to check the validity of the bet placed by user.
def bet_validator(balance, lines):
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet <= balance:
            print(f"Your bet for ${bet} on {lines} lines is added. Total bet = ${total_bet}")
            return bet, total_bet
        else:
            print(f"Not enough balance. Needed: ${total_bet}, Available: ${balance}")
            choice = input("Press 'd' to deposit more, 'q' to quit, or any key to try again: ").lower()
            if choice == 'q':
                return None
            elif choice == 'd':
                return 'deposit'

# Check and returns the winning lines & amount back to user
def check_winnings(columns, lines, bet, multiplier):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        if all(column[line] == symbol for column in columns):
            winnings += multiplier[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
