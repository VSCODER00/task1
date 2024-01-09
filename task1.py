
import pygame
import numpy as np
import sys

class RobotChallenge:
    def __init__(self, arena_size=500, robot_radius=10):
        self.arena_size = arena_size
        self.robot_radius = robot_radius
        self.robot_pos = np.array([arena_size // 2, arena_size // 2], dtype=np.float64)
        self.direction = np.array([1, 0], dtype=np.float64)
        self.speed = 2

    def update(self):
        
        self.robot_pos += self.direction * self.speed

       
        if (
            self.robot_pos[0] - self.robot_radius < 0
            or self.robot_pos[0] + self.robot_radius > self.arena_size
            or self.robot_pos[1] - self.robot_radius < 0
            or self.robot_pos[1] + self.robot_radius > self.arena_size
        ):
            
            rotation_angle = np.random.uniform(0, 2 * np.pi)
            rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                                        [np.sin(rotation_angle), np.cos(rotation_angle)]])
            self.direction = np.dot(rotation_matrix, self.direction)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 128, 255), self.robot_pos.astype(int), self.robot_radius)

def main():
    pygame.init()

    arena_size = 500
    screen = pygame.display.set_mode((arena_size, arena_size))
    pygame.display.set_caption("Robot Challenge")

    clock = pygame.time.Clock()
    robot_challenge = RobotChallenge(arena_size)

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

if __name__ == "__main__":
    main()
