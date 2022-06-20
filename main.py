import sys
import pygame
from Classes.Level import Level
from Classes.Game import Game


screen = pygame.display.set_mode((1280, 720))
game = Game()
i = 1
while not game.finished:
    game.levels.append(Level(i))
    recent = game.levels[len(game.levels) - 1]
    recent.level_setup(screen)
    while not recent.failed or recent.finished:
        recent.game_loop(screen)
    i +=1



