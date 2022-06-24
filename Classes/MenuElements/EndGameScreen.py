import pygame


class EndGameScreen:
    def __init__(self, score, levels):
        self.font_name = "assets/8-BIT WONDER.TTF"
        self.run_display = False
        self.score = score
        self.levels = levels
        self.name = ''

    def draw_text(self, text, size, x, y, screen):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)

    def update(self,score,levels):
        self.score = score
        self.levels = levels
        return [self.score,self.levels]

    def draw_eog(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (400, 80), (880, 80), 3)
        self.draw_text("Game Over", 50, 640, 140, screen)
        pygame.draw.line(screen, (255, 255, 255), (400, 200), (880, 200), 3)
        self.draw_text("Levels Cleared: {}".format(self.levels), 30, 640, 270, screen)
        self.draw_text("Total Points: {}".format(self.score), 30, 640, 320, screen)
        self.draw_text("Name:{}".format(self.name),30,640,370,screen)
