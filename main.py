import sys
import pygame
import pygame.freetype
from Classes.Level import Level

level1 = Level()
screen = pygame.display.set_mode((1280, 720))

level1.level_setup(screen)
level1.game_loop(screen)


