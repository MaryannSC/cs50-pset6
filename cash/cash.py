# cash. py caluculates the minimum number of coins
# required to give a user change

from cs50 import get_float

# get float input
while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break

cents = int(round((change * 100), 0))

coins = 0

# get number of quarters
coins = coins + cents // 25
cents = cents % 25

# get number of dimes
coins = coins + cents // 10
cents = cents % 10

# get number of nickels
coins = coins + cents // 5
cents = cents % 5

# remaining number is pennies
coins = coins + cents

print(coins)