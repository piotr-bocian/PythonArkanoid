import pygame.freetype

from Classes.LeftSidePanel.LevelDisplay import LevelDisplay
from Classes.LeftSidePanel.LivesDisplay import LivesDisplay
from Classes.LeftSidePanel.ScoreDisplay import ScoreDisplay

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
