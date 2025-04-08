import pygame


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 120
        self.height = 12
        self.acceleration = 0.2
        self.max_speed = 2
        self.velocity = 0
        self. friction = 0.95

    def move_right(self):
        if self.velocity < self.max_speed:
            self.velocity += self.acceleration
        return self.x

    def move_left(self):
        if self.velocity > -self.max_speed:
            self.velocity -= self.acceleration
        return self.x

    def update(self):
        max_velocity = 2
        self.velocity = max(-max_velocity, min(self.velocity, max_velocity))
        self.x += self.velocity

        if self.x < 180:
            self.x = 180
            self.velocity = 0
        elif self.x + self.width > 1280:
            self.x = 1280 - self.width
            self.velocity = 0

        self.velocity *= self.friction
        if abs(self.velocity) < 0.1:
            self.velocity = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height))
