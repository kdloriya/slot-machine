# Code tha handles the printing of slot machine after the spin,
# the actual result that will be displayed to the user.
def print_slot_machine(columns):
    try:
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                print(column[row], end=" | " if i != len(columns) - 1 else "")
            print()
    except Exception as e:
        print("Error printing slot machine:", e)
