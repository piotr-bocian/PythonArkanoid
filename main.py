import sys
import pygame
from Classes.Level import Level
from Classes.Game import Game


level1 = Level()
screen = pygame.display.set_mode((1280, 720))
game = Game()
while not game.finished:
    game.levels.append(Level())
    recent = game.levels[len(game.levels) - 1]
    recent.level_setup(screen)
    while not recent.finished:
        recent.game_loop(screen)


