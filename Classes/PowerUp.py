import threading

import pygame
import time


class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 18
        self.speed = .3
        self.used = False
        self.hit = False
        self.type = 4

    def fall(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

    def effect(self, object):
        if not self.used:
            if self.type == 1:
                self.stretch_paddle(object)
            elif self.type == 2:
                self.shrink_paddle(object)
            elif self.type == 3:
                self.speed_ball_up(object)
            elif self.type == 4:
                self.speed_ball_down(object)

    def stretch_paddle(self, paddle):
        global timeout, start
        if not self.hit:
            start = time.time()
            timeout = 0
            paddle.width += 80
            self.hit = True
        lap = time.time()
        timeout += lap - start
        start = lap
        if timeout >= 10:
            paddle.width = 120
            self.used = True

    def shrink_paddle(self, paddle):
        global timeout, start
        if not self.hit:
            start = time.time()
            timeout = 0
            paddle.width -= 40
            self.hit = True
        lap = time.time()
        timeout += lap - start
        start = lap
        if timeout >= 10:
            paddle.width = 120
            self.used = True

    def speed_ball_up(self,ball):
        global timeout, start
        if not self.hit:
            start = time.time()
            timeout = 0
            ball.x_speed *= 2
            ball.y_speed *=2
            self.hit = True
        lap = time.time()
        timeout += lap - start
        start = lap
        if timeout >= 5:
            ball.x_speed /= 2
            ball.y_speed /= 2
            self.used = True

    def speed_ball_down(self, ball):
        global timeout, start
        if not self.hit:
            start = time.time()
            timeout = 0
            ball.x_speed /= 2
            ball.y_speed /= 2
            self.hit = True
        lap = time.time()
        timeout += lap - start
        start = lap
        if timeout >= 5:
            ball.x_speed *= 2
            ball.y_speed *= 2
            self.used = True

    def clear(self, paddle):
        paddle.width = 120
        self.used = True

    def check_hit_paddle(self, x, y, width):
        if x <= self.x <= x + width and self.y + self.radius >= y:
            return True
