
from task1 import RobotChallenge, main
import pygame
import sys

if __name__ == "__main__":
    pygame.init()

    arena_size = 500
    screen = pygame.display.set_mode((arena_size, arena_size))
    pygame.display.set_caption("Robot Challenge")

    clock = pygame.time.Clock()
    robot_challenge = RobotChallenge(arena_size)

    
    pygame.time.delay(100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        robot_challenge.update()

        screen.fill((255, 255, 255))
        robot_challenge.draw(screen)

        pygame.display.flip()
        clock.tick(60)
