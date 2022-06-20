import pygame
import pygame.freetype

from Classes.LevelDisplay import LevelDisplay
from Classes.LivesDisplay import LivesDisplay
from Classes.ScoreDisplay import ScoreDisplay

pygame.init()


class LeftScreen:
    def __init__(self, no,lives, y):
        self.level = LevelDisplay(no,y)
        self.score = ScoreDisplay(y + 80)
        self.lives = LivesDisplay(lives, y + 160)
        self.font_name = "assets/8-BIT WONDER.TTF"

    def display(self, screen):
        self.level.display(screen)
        self.score.display(screen)
        self.lives.display(screen)
