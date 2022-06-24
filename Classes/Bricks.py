import pygame
import random
import numpy as np
from Classes.Brick import Brick


class Bricks:
    def __init__(self):
        self.bricks_array = []
        self.pattern = []

    def add_brick(self, x, y):
        brick = Brick(x, y)
        self.bricks_array.append(brick)
        return self.bricks_array

    def remove_brick(self, brick):
        self.bricks_array.remove(brick)
        return self.bricks_array

    def draw(self, screen):
        for brick in self.bricks_array:
            brick.draw(screen)

    def map_index_to_cords(self, i, j):
        x = 212 + j * 90
        y = 70 + i * 32
        return [x, y]

    def pattern_generator(self):
        self.pattern = [[None] * 11 for _ in range(1)]
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                x = random.randint(0, 1)
                self.pattern[i][j] = x
                self.pattern[i][10 - j] = self.pattern[i][j]
        return self.pattern

    def create_bricks_from_pattern(self):
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                if self.pattern[i][j] == 1:
                    cords = self.map_index_to_cords(i, j)
                    self.add_brick(cords[0], cords[1])
        return self.bricks_array

