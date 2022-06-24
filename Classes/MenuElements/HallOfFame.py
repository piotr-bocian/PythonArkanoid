import pygame
import csv


class HallOfFame:
    def __init__(self):
        self.font_name = "assets/8-BIT WONDER.TTF"
        self.run_display = False
        self.top = []

    def draw_text(self, text, size, x, y, screen):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)

    def find_top(self):
        self.top.clear()
        with open('Classes/MenuElements/hof.csv', newline='') as f:
            reader = csv.reader(f)
            hof = list(reader)
        f.close()
        hof = sorted(hof, key=lambda x: int(x[1]))
        if len(hof)>=3:
            self.top.append(hof[-1])
            self.top.append(hof[-2])
            self.top.append(hof[-3])
        return hof

    def draw_hof(self, screen):
        self.find_top()
        pygame.draw.line(screen, (255, 255, 255), (400, 80), (880, 80), 3)
        self.draw_text("Hall of Fame", 50, 640, 140, screen)
        pygame.draw.line(screen, (255, 255, 255), (400, 200), (880, 200), 3)
        if len(self.top)==3:
            self.draw_text("1 {}  {}".format(self.top[0][0], self.top[0][1]), 30, 640, 270, screen)
            self.draw_text("2 {}  {}".format(self.top[1][0], self.top[1][1]), 30, 640, 320, screen)
            self.draw_text("3 {}  {}".format(self.top[2][0], self.top[2][1]), 30, 640, 370, screen)
        else:
            self.draw_text("Play more games", 30, 640, 270, screen)
