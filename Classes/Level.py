import sys
import pygame
from Classes.Paddle import Paddle
from Classes.Ball import Ball
from Classes.Bricks import Bricks
from Classes.PowerUp import PowerUp
from Classes.LeftSidePanel.LeftScreen import LeftScreen
from Classes.ModalWindow import ModalWindow
from math import pi


class Level:
    def __init__(self, no,lives):
        self.number = no
        self.saved = False
        self.initial = True
        self.cleared = False
        self.failed = False
        self.pause = False
        self.lost = False
        self.points = 0
        self.lives = lives
        self.paddle = Paddle(640, 680)
        self.ball = Ball((2 * self.paddle.x + self.paddle.width) / 2, self.paddle.y - 20)
        self.bricks = Bricks()
        self.pu = None
        self.lscreen = LeftScreen(self.number, self.lives, 40)

    def check_if_finished(self):
        if len(self.bricks.bricks_array) == 0:
            self.pause = True
            self.cleared = True
            self.failed = True
            print(self.pause, self.cleared)
            return True
        return False

    def check_if_lost(self):
        if self.lives <= 0:
            self.pause = True
            self.lost = True
            self.failed = True
            return True
        return False

    def add_life(self):
        self.lives += 1
        return self.lives

    def sub_life(self):
        self.lives -= 1
        return self.lives

    def add_points(self,points):
        self.points += points
        return self.points

    def toggle_pause(self):
        if self.pause:
            self.pause = False
            return False
        self.pause = True
        return True

    def draw_countdown(self, screen, x, y, w, h):
        time = 2 * pi / self.pu.time * (self.pu.time - self.pu.timeout)
        pygame.draw.arc(screen, (255, 255, 255), [x, y, w, h], 0, time, 6)

    def level_setup(self, screen):
        self.bricks.pattern_generator()
        self.bricks.create_bricks_from_pattern()
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
        self.paddle.draw(screen)
        self.ball.draw(screen)
        pygame.display.flip()
        self.lscreen.display(screen)

    def game_loop(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            while not self.cleared and not self.lost and not self.saved:

                while self.initial and not self.saved:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit(0)
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            self.initial = False
                            self.failed = False
                            self.ball.shoot()
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            self.saved = True
                    keys = pygame.key.get_pressed()

                    screen.fill((0, 0, 0))
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
                    self.paddle.draw(screen)
                    self.ball.draw(screen)
                    self.bricks.draw(screen)
                    self.lscreen.display(screen)
                    pygame.display.flip()

                    if keys[pygame.K_d]:
                        self.paddle.move_right()
                        self.ball.follow_paddle(self.paddle)
                    if keys[pygame.K_a]:
                        self.paddle.move_left()
                        self.ball.follow_paddle(self.paddle)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.toggle_pause()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.saved = True
                keys = pygame.key.get_pressed()

                while not self.failed and not self.saved:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit(0)
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            self.toggle_pause()
                    keys = pygame.key.get_pressed()

                    if not self.pause and not self.saved:
                        screen.fill((0, 0, 0))
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
                        self.paddle.update()
                        self.paddle.draw(screen)
                        self.ball.draw(screen)
                        self.bricks.draw(screen)
                        self.lscreen.display(screen)
                        self.check_if_finished()
                        self.check_if_lost()

                        self.ball.move()

                        if self.pu:
                            if not self.pu.used:
                                self.pu.draw(screen)
                                self.pu.fall()

                        self.ball.check_hit_paddle(self.paddle)
                        self.ball.check_hit_wall()

                        for brick in self.bricks.bricks_array:
                            if self.ball.check_hit_brick(brick):
                                if brick.is_powerUp() and not self.pu:
                                    self.pu = PowerUp(brick.x, brick.y, 5, brick.pick_powerUp())
                                self.lscreen.score.add_score(brick.points)
                                self.bricks.bricks_array.remove(brick)
                                self.add_points(brick.points)

                        if self.pu:
                            if not self.pu.fallen():
                                if self.pu.check_hit_paddle(self.paddle.x, self.paddle.y, self.paddle.width):
                                    self.pu.effect(self.paddle, self.ball, self.lives)
                                if self.pu.hit and not self.pu.used:
                                    self.pu.effect(self.paddle, self.ball, self.lives)
                                    self.draw_countdown(screen, self.pu.x - self.pu.radius - 12,
                                                        self.pu.y - self.pu.radius - 12,
                                                        2 * self.pu.radius + 24, 2 * self.pu.radius + 24)
                                if self.pu.used:
                                    self.pu = None
                            else:
                                self.pu = None

                        if self.ball.check_if_fallen():
                            self.sub_life()
                            self.lscreen.lives.sub_lives()
                            self.paddle.x = 640
                            self.ball.x = 700
                            self.ball.y = self.paddle.y - 20
                            self.pu = None
                            self.paddle.width = 120
                            self.initial = True
                            self.failed = True



                        pygame.display.flip()

                        if keys[pygame.K_d]:
                            self.paddle.move_right()
                        if keys[pygame.K_a]:
                            self.paddle.move_left()
                        if keys[pygame.K_ESCAPE]:
                            self.saved = True
