import pygame
import sys
import pygame.freetype  # Import the freetype module.
from Classes.Menu import Menu

menu = Menu([320,270])
pygame.init()
screen = pygame.display.set_mode((1280, 720))
GAME_FONT = pygame.freetype.SysFont("Comic Sans MS", 24)
running = True

while running:
    screen.fill((0, 0, 0))
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

    pygame.display.flip()



    pygame.display.flip()

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((0,0,0))
#     # You can use `render` and then blit the text surface ...
#     text_surface, rect = GAME_FONT.render("Hello World!", (255, 255, 255))
#
#     # or just `render_to` the target surface.
#     GAME_FONT.render_to(screen, (40, 350), "Hello World!", (0, 0, 0))
#
#
