import random

def pattern_generator():
    pattern = [[None] * 11 for _ in range(6)]
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            x = random.randint(0, 1)
            pattern[i][j] = x
            pattern[i][10 - j] = pattern[i][j]
    return pattern

print(pattern_generator())

