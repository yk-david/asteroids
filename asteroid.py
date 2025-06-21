import pygame
import random
from circleshape import CircleShape
from constants import *

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
        else:
            angle = random.uniform(20, 50)
            new_velocity_1 = pygame.math.Vector2.rotate(self.velocity, angle)
            new_velocity_2 = pygame.math.Vector2.rotate(self.velocity, -angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            child_asteroid_1.velocity = new_velocity_1 * 1.2
            child_asteroid_2.velocity = new_velocity_2 * 1.2

