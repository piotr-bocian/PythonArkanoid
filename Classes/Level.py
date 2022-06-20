import sys
import pygame
from Classes.Paddle import Paddle
from Classes.Ball import Ball
from Classes.Brick import Brick
from Classes.Bricks import Bricks
from Classes.LeftScreen import Score
from Classes.Shield import Shield
from Classes.PowerUp import PowerUp
from math import pi
from Classes.LivesDisplay import LivesDisplay
from Classes.LevelDisplay import LevelDisplay
import random
import time


class Level:
    def __init__(self,livescount,no):
        self.initial = True
        self.finished = False
        self.failed = False
        self.pause = False
        self.points = 0
        self.lives = 3
        self.paddle = Paddle(640, 680)
        self.ball = Ball((2 * self.paddle.x + self.paddle.width) / 2, self.paddle.y - 20)
        self.bricks = Bricks()
        self.score = Score()
        self.pu = None
        self.shield = False
        self.lives = LivesDisplay(livescount)
        self.level = LevelDisplay(no)

    def check_if_finished(self):
        if len(self.bricks.bricks_array) == 0:
            self.finished = True

    def toggle_pause(self):
        if self.pause:
            self.pause = False
            print(self.pause)
            return
        self.pause = True

    def draw_countdown(self, screen, x,y,w,h):
        time = 2*pi/self.pu.time*(self.pu.time-self.pu.timeout)
        pygame.draw.arc(screen,(255,255,255),[x,y,w,h],0,time,6)


    def level_setup(self, screen):

        # for i in range(11):
        #     self.bricks.add_brick(212 + 95 * i, 70)
        self.bricks.pattern_generator()
        self.bricks.create_bricks_from_pattern()
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
        self.paddle.draw(screen)
        self.ball.shoot()
        self.ball.draw(screen)
        # self.bricks.draw(screen)
        pygame.display.flip()
        self.score.display(screen)
        self.lives.display(screen)
        self.level.display(screen)

    def game_loop(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        while not self.failed:
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
                        self.finished = False
                keys = pygame.key.get_pressed()

                screen.fill((0, 0, 0))
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
                self.paddle.draw(screen)
                self.ball.draw(screen)
                self.bricks.draw(screen)
                self.score.display(screen)
                self.lives.display(screen)
                self.level.display(screen)
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
                    self.lives.display(screen)
                    self.level.display(screen)
                    self.check_if_finished()
                    self.ball.move()
                    if self.pu:
                        if not self.pu.used:
                            self.pu.draw(screen)
                            self.pu.fall()
                    self.ball.check_hit_paddle(self.paddle.x, self.paddle.y, self.paddle.width)
                    self.ball.check_hit_wall()
                    if self.ball.check_if_fallen():
                        self.lives.lives -= 1
                        self.paddle.x = 640
                        self.ball.x = 700
                        self.ball.y = self.paddle.y - 20
                        self.pu = None
                        self.paddle.width = 120
                        self.initial = True
                        self.finished = True
                    for brick in self.bricks.bricks_array:
                        if self.ball.check_hit_brick(brick.x, brick.y, brick.width, brick.height):
                            if brick.is_powerUp() and not self.pu:
                                self.pu = PowerUp(brick.x,brick.y,5,brick.pick_powerUp())
                            self.score.score += brick.points
                            self.bricks.bricks_array.remove(brick)
                    if self.shield:
                        self.ball.check_hit_shield()
                    if self.pu:
                        if not self.pu.fallen():
                            if self.pu.check_hit_paddle(self.paddle.x, self.paddle.y, self.paddle.width):
                                self.pu.effect(self.paddle, self.ball,self.lives)
                            if self.pu.hit and not self.pu.used:
                                self.pu.effect(self.paddle, self.ball,self.lives)
                                self.draw_countdown(screen, self.pu.x - self.pu.radius - 12,
                                                    self.pu.y - self.pu.radius - 12,
                                                    2 * self.pu.radius + 24, 2 * self.pu.radius + 24)
                            if self.pu.used:
                                self.pu = None
                        else:
                            self.pu = None
                    pygame.display.flip()

                    if keys[pygame.K_d]:
                        self.paddle.move_right()
                    if keys[pygame.K_a]:
                        self.paddle.move_left()