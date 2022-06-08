import sys
import pygame
import pygame.freetype
from Classes.Level import Level

level1 = Level()
screen = pygame.display.set_mode((1280, 720))

level1.level_setup(screen)
level1.game_loop(screen)


# from Classes.Paddle import Paddle
# from Classes.Ball import Ball
# from Classes.Level import Level
# from Classes.Brick import Brick
# from Classes.Bricks import Bricks
# from Classes.LeftScreen import Score
# from Classes.Shield import Shield
#

# paddle = Paddle(640, 680)
# ball = Ball((2 * paddle.x + paddle.width) / 2, paddle.y - 20)
# level1 = Level()
# bricks = Bricks()
# brick1 = Brick(200, 100)
# brick2 = Brick(270, 100)
# score = Score()
# shield = Shield(710)
#
# for i in range(12):
#     for j in range(10):
#         bricks.add_brick(270 + +20 + 75 * i, 70 + 30 * j)
#
# screen.fill((0, 0, 0))
# pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
# paddle.draw(screen)
# ball.draw(screen)
# bricks.draw(screen)
# shield.draw(screen)
# pygame.display.flip()
# score.display(screen)
# while True:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit(0)
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             level1.toggle_pause()
#     keys = pygame.key.get_pressed()
#
#     if not level1.pause:
#         screen.fill((0, 0, 0))
#         pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
#         paddle.draw(screen)
#         ball.draw(screen)
#         bricks.draw(screen)
#         shield.draw(screen)
#         score.display(screen)
#         ball.move()
#         ball.check_hit_paddle(paddle.x, paddle.y, paddle.width)
#         ball.check_hit_wall()
#         for brick in bricks.bricks_array:
#             if ball.check_hit_brick(brick.x,brick.y,brick.width,brick.height):
#                 bricks.bricks_array.remove(brick)
#
#         pygame.display.flip()
#
#         if keys[pygame.K_d]:
#             paddle.move_right()
#         if keys[pygame.K_a]:
#             paddle.move_left()
#
#
