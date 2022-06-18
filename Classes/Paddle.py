import pygame


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 120
        self.height = 12
        self.speed = .3
        self.friction = 0.9
        self.acceleration = 2
        self.velocity = 0

    def move(self):
        if self.velocity < self.speed:
            self.velocity += self.acceleration
            print(self.velocity)

        if self.velocity > -self.speed:
            self.velocity -= self.acceleration

        self.velocity *= self.friction
        self.x += self.velocity

    def move_right(self):
        if self.x + self.width < 1280:
            self.x += self.speed

    def move_left(self):
        if self.x > 180:
            self.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height))
