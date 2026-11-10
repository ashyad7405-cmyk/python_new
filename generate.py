"""import random

coin = random.choice(["heads","tails"])
print(coin)"""

from random import choice

coin =choice(["heads","tails"])
print(coin)

import random

num = random.randint(1,10)
print(num)

import random

cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)