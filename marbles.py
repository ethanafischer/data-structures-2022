import random

# 0 = white, 1 = black

a = [0, 0]
b = [1, 1]
c = [0, 1]
marbles = [a, b, c]


def loadmarbles(marbles):
    random.shuffle(marbles)
    bagpick = random.randint(0, 2)
    marblepick = random.randint(0, 1)
    marbles[bagpick][marblepick]


loadmarbles(marbles)

"""def loadmarbles() -> list[[int, int],[int, int], [int, int]]:
    load = random.randint(0, 2)
    if load"""
