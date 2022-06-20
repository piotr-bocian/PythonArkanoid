import threading

import pygame
import time


class PowerUp:
    def __init__(self, x, y, time, type):
        self.x = x
        self.y = y
        self.radius = 18
        self.speed = .2
        self.used = False
        self.hit = False
        self.type = type
        self.time = time
        self.timeout = 0

    def fall(self):
        self.y += self.speed

    def fallen(self):
        if self.y >= 720:
            return True
        return False

    def map_type_to_color(self):
        if self.type == 1 or self.type == 4:
            return (0, 255, 0)
        elif self.type == 2 or self.type == 3:
            return (255, 0, 0)
        elif self.type == 5:
            return (255, 51, 204)

    def draw(self, screen):
        pygame.draw.circle(screen, self.map_type_to_color(), (self.x, self.y), self.radius)

    def effect(self, paddle, ball,lives):
        if not self.used:
            self.x = 90
            self.y = 320
            self.speed = 0
            if self.type == 1:
                self.stretch_paddle(paddle)
            elif self.type == 2:
                self.shrink_paddle(paddle)
            elif self.type == 3:
                self.speed_ball_up(ball)
            elif self.type == 4:
                self.speed_ball_down(ball)
            elif self.type == 5:
                self.add_life(lives)

    def stretch_paddle(self, paddle):
        global start
        if not self.hit:
            start = time.time()
            paddle.width += 80
            self.hit = True
        lap = time.time()
        self.timeout += lap - start
        start = lap
        if self.timeout >= self.time:
            paddle.width = 120
            self.used = True

    def shrink_paddle(self, paddle):
        global start
        if not self.hit:
            start = time.time()
            paddle.width -= 40
            self.hit = True
        lap = time.time()
        self.timeout += lap - start
        start = lap
        if self.timeout >= self.time:
            paddle.width = 120
            self.used = True

    def speed_ball_up(self, ball):
        global start
        if not self.hit:
            start = time.time()
            ball.x_speed *= 2
            ball.y_speed *= 2
            self.hit = True
        lap = time.time()
        self.timeout += lap - start
        start = lap
        if self.timeout >= self.time:
            ball.x_speed /= 2
            ball.y_speed /= 2
            self.used = True

    def speed_ball_down(self, ball):
        global start
        if not self.hit:
            start = time.time()
            ball.x_speed /= 2
            ball.y_speed /= 2
            self.hit = True
        lap = time.time()
        self.timeout += lap - start
        start = lap
        if self.timeout >= self.time:
            ball.x_speed *= 2
            ball.y_speed *= 2
            self.used = True

    def add_life(self,lives):
        lives += 1

    def check_hit_paddle(self, x, y, width):
        if x <= self.x <= x + width and self.y + self.radius >= y:
            return True
