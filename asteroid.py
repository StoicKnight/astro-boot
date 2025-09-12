import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split_angle = random.uniform(20, 50)
        split_radius = self.radius - ASTEROID_MIN_RADIUS

        split_right = self.velocity.rotate(split_angle)
        split_left = self.velocity.rotate(-split_angle)

        asteroid = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid.velocity = split_right * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid.velocity = split_left * 1.5
