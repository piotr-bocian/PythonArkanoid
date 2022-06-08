import sys
import pygame
from Classes.Paddle import Paddle
from Classes.Ball import Ball
from Classes.Brick import Brick
from Classes.Bricks import Bricks
from Classes.LeftScreen import Score
from Classes.Shield import Shield


class Level:
    def __init__(self):
        self. initial = True
        self.pause = True
        self.number = 1
        self.paddle = Paddle(640, 680)
        self.ball = Ball((2 * self.paddle.x + self.paddle.width) / 2, self.paddle.y - 20)
        self.bricks = Bricks()
        self.score = Score()
        self.shield = Shield(710)

    def toggle_pause(self):
        if self.pause:
            self.pause = False
            print(self.pause)
            return
        self.pause = True

    def level_setup(self,screen):

        for i in range(12):
            for j in range(10):
                self.bricks.add_brick(270 + +20 + 75 * i, 70 + 30 * j)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
        self.paddle.draw(screen)
        self.ball.draw(screen)
        self.bricks.draw(screen)
        self.shield.draw(screen)
        pygame.display.flip()
        self.score.display(screen)

    def game_loop(self,screen):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.toggle_pause()
            keys = pygame.key.get_pressed()

            if not self.pause:
                screen.fill((0, 0, 0))
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
                self.paddle.draw(screen)
                self.ball.draw(screen)
                self.bricks.draw(screen)
                self.shield.draw(screen)
                self.score.display(screen)
                self.ball.move()
                self.ball.check_hit_paddle(self.paddle.x, self.paddle.y, self.paddle.width)
                self.ball.check_hit_wall()
                for brick in self.bricks.bricks_array:
                    if self.ball.check_hit_brick(brick.x, brick.y, brick.width, brick.height):
                        self.bricks.bricks_array.remove(brick)

                pygame.display.flip()

                if keys[pygame.K_d]:
                    self.paddle.move_right()
                if keys[pygame.K_a]:
                    self.paddle.move_left()