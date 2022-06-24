import pygame


class Game:
    def __init__(self):
        self.lives = 3
        self.paused = False
        self.finished = False
        self.points = 0
        self.levels = []

    def check_if_end(self):
        if self.lives == 0:
            self.finished = True
        return self.finished

    def add_level_points(self,level):
        self.points += level.points
        return self.points

