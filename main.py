import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for thing in updatable:
            thing.update(dt)
        pygame.Surface.fill(screen, color="black")
        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

        
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    



if __name__ == "__main__":
    main()