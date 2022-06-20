import pygame


class Game:
    def __init__(self):
        self.lives = 30
        self.finished = False
        self.points = 0
        self.levels = []

    def add_life(self):
        self.lives += 1

    def sub_life(self):
        self.lives -= 1

    def check_if_end(self):
        if self.lives == 0:
            self.finished = True

    def add_level_points(self,level):
        self.points += level.points

