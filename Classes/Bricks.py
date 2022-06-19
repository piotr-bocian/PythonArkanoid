import pygame
import random
import numpy as np
from Classes.Brick import Brick

class Bricks:
    def __init__(self):
        self.bricks_array = []
        self.pattern = []

    def add_brick(self,x,y):
        brick = Brick(x,y)
        self.bricks_array.append(brick)

    def remove_brick(self, brick):
        self.bricks_array.remove(brick)

    def draw(self,screen):
        for brick in self.bricks_array:
            brick.draw(screen)

    def map_index_to_cords(self,i,j):
        x = 270+j*100
        y = 100+i*32
        return [x,y]

    def pattern_generator(self):
        row = [None] * 11
        self.pattern = [row] * 6
        for i in range(len(self.pattern)):
            for j in range(len(row)):
                self.pattern[i][j] = random.randint(0, 1)
                self.pattern[i][10-j] = self.pattern[i][j]
        return self.pattern
    
    def create_bricks_from_pattern(self):
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                if self.pattern[i][j] == 1:
                    cords = self.map_index_to_cords(i, j)
                    self.add_brick(cords[0],cords[1])
                    # self.add_brick(cords[0],cords[1])
        return self.bricks_array

bricks = Bricks()
bricks.pattern_generator()
print(bricks.pattern)
bricks.create_bricks_from_pattern()
print(bricks.bricks_array)
