import pygame
import random


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
        return [self.x, self.y]

    def shoot(self):
        self.x_speed = random.random() * .5 + .2 * (-1) ** random.randint(0, 1)
        self.y_speed = -(1 - self.x_speed ** 2)
        return [self.x_speed, self.y_speed]

    def follow_paddle(self, paddle):
        self.x = (2 * paddle.x + paddle.width) / 2
        return self.x_speed

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 150, 255), (self.x, self.y), self.radius)

    def check_hit_paddle(self, paddle):
        if round(paddle.x) <= round(self.x) <= round(paddle.x) + paddle.width and round(
                self.y + self.radius) == paddle.y:
            if paddle.x + paddle.width / 3 <= self.x <= paddle.x + 2 * paddle.width / 3:
                if self.x_speed >= .01 and self.y_speed >= .01:
                    self.y_speed *= -.9
                    self.x_speed *= .9
                else:
                    self.y_speed *= -1
                    if self.x_speed > 0:
                        self.x_speed += .3
                    else:
                        self.x_speed -= .3
            else:
                if self.x_speed ** 2 + self.y_speed ** 2 <= 1.2:
                    self.y_speed *= -1.01
                    self.x_speed *= 1.2
                else:
                    self.shoot()

            return True
        return False

    def check_hit_wall(self):
        if self.x - self.radius <= 180 or self.x + self.radius >= 1280:
            self.x_speed *= -1
            return True
        if self.y - self.radius <= 0:
            self.y_speed *= -1
            return True

    def check_hit_brick(self, brick):
        if brick.x <= self.x <= brick.x + brick.width and (
                brick.y >= self.y - self.radius >= brick.y - brick.height or
                brick.y >= self.y + self.radius >= brick.y - brick.height):
            self.y_speed *= -1
            return True
        if brick.y - brick.height <= self.y <= brick.y and (
                brick.x <= self.x + self.radius <= brick.x + brick.width or
                brick.x + brick.width >= self.x - self.radius >= brick.x):
            self.x_speed *= -1
            return True
        return False

    def check_if_fallen(self):
        if self.y > 720:
            return True
        return False
