import sys
import pygame
from Classes.Paddle import Paddle
from Classes.Ball import Ball
from Classes.Brick import Brick
from Classes.Bricks import Bricks
from Classes.LeftScreen import Score
from Classes.Shield import Shield
import random


class Level:
    def __init__(self):
        self.initial = True
        self.finished = False
        self.pause = False
        self.points = 0
        self.paddle = Paddle(640, 680)
        self.ball = Ball((2 * self.paddle.x + self.paddle.width) / 2, self.paddle.y - 20)
        self.bricks = Bricks()
        self.score = Score()
        self.shield = False

    def check_if_finished(self):
        if len(self.bricks.bricks_array) == 0:
            self.finished = True

    def toggle_pause(self):
        if self.pause:
            self.pause = False
            print(self.pause)
            return
        self.pause = True

    def level_setup(self,screen):

        # for i in range(11):
        #     self.bricks.add_brick(220 + 95 * i, 70)
        self.bricks.pattern_generator()
        self.bricks.create_bricks_from_pattern()
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
        self.paddle.draw(screen)
        self.ball.shoot()
        self.ball.draw(screen)
        self.bricks.draw(screen)
        pygame.display.flip()
        self.score.display(screen)


    def game_loop(self,screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.initial = False
        keys = pygame.key.get_pressed()

        while self.initial:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.initial = False
            keys = pygame.key.get_pressed()

            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
            self.paddle.draw(screen)
            self.ball.draw(screen)
            self.bricks.draw(screen)
            self.score.display(screen)
            pygame.display.flip()

            if keys[pygame.K_d]:
                self.paddle.move_right()
                self.ball.follow_paddle(self.paddle)
            if keys[pygame.K_a]:
                self.paddle.move_left()
                self.ball.follow_paddle(self.paddle)

        while not self.finished:

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
                self.score.display(screen)
                self.check_if_finished()
                self.ball.move()
                self.ball.check_hit_paddle(self.paddle.x, self.paddle.y, self.paddle.width)
                self.ball.check_hit_wall()
                for brick in self.bricks.bricks_array:
                    if self.ball.check_hit_brick(brick.x, brick.y, brick.width, brick.height):
                        self.score.score += brick.points
                        self.bricks.bricks_array.remove(brick)
                        print(self.points)
                if self.shield:
                    self.ball.check_hit_shield()
                pygame.display.flip()

                if keys[pygame.K_d]:
                    self.paddle.move_right()
                if keys[pygame.K_a]:
                    self.paddle.move_left()