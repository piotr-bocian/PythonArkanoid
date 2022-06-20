import pygame
import pygame.freetype

pygame.init()

class LivesDisplay:
    def __init__(self,lives):
        self.lives = lives
        self.font_name = "assets/8-BIT WONDER.TTF"

    def show(self):
        return self.lives

    def draw_text(self, text, size, x, y, screen):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)

    def display(self, screen):
        self.draw_text("Lives".format(self.show()), 20, 90,200, screen)
        self.draw_text("{}".format(self.show()), 20, 90, 240, screen)