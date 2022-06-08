import pygame


class HallOfFame:
    def __init__(self):
        self.font_name = "assets/8-BIT WONDER.TTF"
        self.run_display = False

    def draw_text(self, text, size, x, y, screen):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)

    def draw_hof(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (400, 80), (880, 80), 3)
        self.draw_text("Hall of Fame", 50, 640, 140, screen)
        pygame.draw.line(screen, (255, 255, 255), (400, 200), (880, 200), 3)
