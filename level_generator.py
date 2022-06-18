import random

def level_generator():
    row = [None]*11
    bricks = [row]*6
    for i in range(5):
        for j in range(6):
            bricks[i][j] = random.randint(0,1)
            bricks[i][-j] = bricks[i][j]
    return bricks

print(level_generator())
