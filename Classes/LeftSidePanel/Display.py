import pygame
import pygame.freetype

pygame.init()


class Display:
    def __init__(self,y):
        self.y = y
        self.font_name = "assets/8-BIT WONDER.TTF"

    def draw_text(self, text, size, x, y, screen):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)
