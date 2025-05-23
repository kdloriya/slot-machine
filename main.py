from core.game_logic import deposit, spin

# Core function that handles the entire lifecycle of slot machine.
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit): ").lower()
        if answer == "q":
            break

        result = spin(balance)
        if result is None:
            print("Exiting the game.")
            break
        elif result == 'deposit':
            balance += deposit()
        else:
            balance += result

    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
