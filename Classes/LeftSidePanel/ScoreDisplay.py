import pygame.freetype
from Classes.LeftSidePanel.Display import Display

pygame.init()


class ScoreDisplay(Display):
    def __init__(self, y):
        super().__init__(y)
        self.score = 0
        self.font_name = "assets/8-BIT WONDER.TTF"

    def show(self):
        return self.score

    def add_score(self, a):
        self.score += a
        return self.score

    def display(self, screen):
        self.draw_text("Score".format(self.show()), 20, 90, self.y, screen)
        self.draw_text("{}".format(self.show()), 20, 90, self.y+40, screen)
