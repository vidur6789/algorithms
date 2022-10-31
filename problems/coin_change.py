import math
amount = 0.49

coins = [1.0, 0.25, 0.1, 0.05, 0.01]

num_coins = []
remainder = amount
for coin in coins:
    count = remainder // coin
    num_coins.append(count)
    remainder = round(remainder % coin, 2)
    print(remainder, coin)


print(num_coins)
