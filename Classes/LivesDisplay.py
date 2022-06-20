import pygame
import pygame.freetype
from Classes.Display import Display

pygame.init()


class LivesDisplay(Display):
    def __init__(self, lives, y):
        super().__init__(y)
        self.lives = lives
        self.font_name = "assets/8-BIT WONDER.TTF"

    def show(self):
        return self.lives

    def display(self, screen):
        self.draw_text("Lives".format(self.show()), 20, 90, self.y, screen)
        self.draw_text("{}".format(self.show()), 20, 90, self.y+40, screen)
