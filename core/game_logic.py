import random
from core.constants import MAX_LINES, ROWS, COLUMNS, symbol_count, symbol_multiplier
from ui.display import print_slot_machine
from utils.validators import get_bet, bet_validator, check_winnings

# Returns the cyliners with the random symbols, 
# which will be displayed once the user spins the slot.
def get_slot_machine_spin(rows, cols, symbols):
    
    all_symbols = []
    """
    For each available symbol, we will add that symbol mentioned number of times to the all_symbols list.
    For example, if we have symbols = {"A": 2, "B": 4}, then all_symbols will be ["A", "A", "B", "B", "B", "B"].
    """
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    """
    For available number of columns, we will create a list of lists (columns).
    Each column will contain a list of randomly selected symbols from all_symbols.
    When the symbol is selected, the same symbol will also be removed from the current_symbols list.
    When the list of symbol reaches the required number of rows, we will add that to the columns list.
    """
    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

# Code to handle and verify the money deposits.
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        
        """
        Check if the input is a digit and convert it to an integer
        If the input is not a digit, it will prompt the user to enter a valid amount
        """
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"${amount} added to the wallet!")
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

# Code to get the user preference of number of lines to bet on.
def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1 - {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
        print("Invalid number of lines.")

# Code to spin the slot machine once.
def spin(balance):
    # Gets and validates each spin
    lines = get_number_of_lines()
    validation_result = bet_validator(balance, lines)

    if validation_result is None:
        return None
    elif validation_result == 'deposit':
        return 'deposit'

    bet, total_bet = validation_result
    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)

    # Code to verify and disaply the Winnings.
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_multiplier)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet
