import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable =  pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(X, Y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        for thing in updatable:
            thing.update(dt)

        pygame.display.flip()

        # limit framerate to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
