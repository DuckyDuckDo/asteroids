import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    # Initialize the game instance and the screen/clock
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Define the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)


    # Initialize asteroid field and player
    asteroid_field = AsteroidField()
    curr_player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Call the group.update function to update everything in group
        updatable.update(dt)
        screen.fill("black")

        # Draw the drawable objects
        for object in drawable:
            object.draw(screen)
        
        # Ends game if an asteroid collides with a player
        for object in asteroids:
            if object.check_collision(curr_player):
                print("Game Over")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
