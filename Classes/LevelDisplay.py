import pygame
import pygame.freetype
from Classes.Display import Display
pygame.init()


class LevelDisplay(Display):
    def __init__(self, level, y):
        super().__init__(y)
        self.level = level
        self.font_name = "assets/8-BIT WONDER.TTF"

    def show(self):
        return self.level

    def display(self, screen):
        self.draw_text("Level".format(self.show()), 20, 90, self.y, screen)
        self.draw_text("{}".format(self.show()), 20, 90, self.y+40, screen)
