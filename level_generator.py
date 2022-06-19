import random
import math

def pattern_generator():
    row = [None] * 11
    pattern = [row] * 6
    for i in range(len(pattern)):
        for j in range(math.floor(len(row)/2)+1):
            pattern[i][j] = random.randint(0, 1)
            pattern[i][10-j] = pattern[i][j]
    return pattern

print(pattern_generator())

