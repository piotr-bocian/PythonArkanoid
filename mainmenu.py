import pygame
import sys
from Classes.Menu import Menu
from Classes.HallOfFame import HallOfFame
from Classes.Options import Options

menu = Menu([320,270])
hof = HallOfFame()
options = Options()
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

while running:
    screen.fill((0, 0, 0))
    if menu.run_display:
        menu.draw_menu(screen)
        menu.draw_cursor(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    menu.move_cursor_down()
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    menu.move_cursor_up()
                elif event.key == pygame.K_RETURN:
                    if menu.state == 2:
                        menu.run_display = False
                        options.run_display = True
                    elif menu.state == 3:
                        menu.run_display = False
                        hof.run_display = True
                    elif menu.state == 4:
                        sys.exit(0)

    elif hof.run_display:
        hof.draw_hof(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.run_display = True
                    hof.run_display = False
    elif options.run_display:
        options.draw_hof(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.run_display = True
                    hof.run_display = False
    pygame.display.flip()

