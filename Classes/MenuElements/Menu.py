import pygame


class Menu:
    def __init__(self, cursor_center):
        self.cursor_center = cursor_center
        self.offset = -10
        self.font_name = "assets/8-BIT WONDER.TTF"
        self.state_list = ["New Game", "Load Game", "Options", "Hall of Fame", "Exit"]
        self.state = 0
        self.run_display = True

    def draw_text(self, text, size, x, y, screen):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)

    def draw_menu(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (400, 80), (880, 80), 3)
        self.draw_text("Arkanoid", 50, 640, 140, screen)
        pygame.draw.line(screen, (255, 255, 255), (400, 200), (880, 200), 3)
        self.draw_text("New Game", 30, 640, 270, screen)
        self.draw_text("Load Game", 30, 640, 320, screen)
        self.draw_text("Options", 30, 640, 370, screen)
        self.draw_text("Hall of Fame", 30, 640, 420, screen)
        self.draw_text("Exit", 30, 640, 470, screen)
        self.draw_text("Made by Piotr Bocian 2022", 15, 190, 700, screen)
        self.draw_cursor(screen)

    def draw_cursor(self, screen):
        points1 = [(self.cursor_center[0] + 50, self.cursor_center[1]),
                   (self.cursor_center[0] + 80, self.cursor_center[1]),
                   (self.cursor_center[0] + 60, self.cursor_center[1] - 10)]
        points2 = [(self.cursor_center[0] + 50, self.cursor_center[1]),
                   (self.cursor_center[0] + 80, self.cursor_center[1]),
                   (self.cursor_center[0] + 60, self.cursor_center[1] + 10)]
        pygame.draw.polygon(screen, (255, 255, 255), points1, 0)
        pygame.draw.polygon(screen, (180, 180, 180), points2, 0)

    def move_cursor_down(self):
        if self.cursor_center[1] < 470:
            self.cursor_center[1] += 50
            self.state += 1
        else:
            self.cursor_center[1] = 270
            self.state = 0

    def move_cursor_up(self):
        if self.cursor_center[1] > 270:
            self.cursor_center[1] -= 50
            self.state -= 1
        else:
            self.cursor_center[1] = 470
            self.state = len(self.state_list) - 1
        print(self.state)
