import pygame

from Classes.Brick import Brick

class Bricks:
    def __init__(self):
        self.bricks_array = []

    def add_brick(self,x,y):
        brick = Brick(x,y)
        self.bricks_array.append(brick)

    def remove_brick(self, brick):
        self.bricks_array.remove(brick)

    def draw(self,screen):
        for brick in self.bricks_array:
            brick.draw(screen)



