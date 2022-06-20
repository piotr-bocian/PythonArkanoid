import pygame
from random import random


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 12
        self.x_speed = 0
        self.y_speed = 0

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def shoot(self):
        self.x_speed = 0
        self.y_speed = .4

    def follow_paddle(self,paddle):
        self.x = (2 * paddle.x + paddle.width) / 2

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 150, 255), (self.x, self.y), self.radius)

    def check_hit_paddle(self, x, y, width):
        if x <= self.x <= x + width and self.y + self.radius >= y:
            self.y_speed *= -1

    def check_hit_wall(self):
        if self.x - self.radius <= 180 or self.x + self.radius >= 1280:
            self.x_speed *= -1
        if self.y - self.radius <= 0:
            self.y_speed *= -1

    def check_hit_brick(self,x,y,width,height):
        if x <= self.x <= x + width and (y >= self.y - self.radius >= y- height or y >= self.y + self.radius >= y - height):
            self.y_speed *= -1
            return True
        if y - height <= self.y <= y and (x <= self.x + self.radius <= x +width or x + width >= self.x - self.radius >= x ):
            self.x_speed *= -1
            return True
        return False

    def check_if_fallen(self):
        if self.y > 720:
            print("przegrales")
            return True

    def check_hit_shield(self):
        if self.y>=710:
            self.y_speed *=1
            return True

