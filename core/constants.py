# These are the constant used for the slot machine, they can be changed to change the odds and structure of how the machine works.

# Denotes max number of lines that a user can bet on at once
MAX_LINES = 3

# Denotes the Min and Max per bet amount
MIN_BET_AMOUNT = 1
MAX_BET_AMOUNT = 100

# Denotes the columns or rotating plates in the slot machine, commonly kept at 3
ROWS = 3
COLUMNS = 3

# Indicates the symbols available on slot machine cylinder [Kept as 4 for simplicity but can be increased]
# The int defined for each symbol is to have different oods for each symbol showing their rarity [Lesser the count higher the win multiplier]
SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Indicates the multiplier in case user wins the game.
SYMBOL_MULTIPLIER = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}