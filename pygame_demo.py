import pygame
from pygame.locals import *

class Circle:
    def __init__(self, x, y):
        self.radius = 50
        self.x = x
        self.y = y
        self.velocity_x = -1
        self.velocity_y = 1

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color(0, 255, 0), (self.x, self.y), self.radius)

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 480))
    running = True
    circles = []
    while running:
        pygame.time.delay(10)
        surface.fill(pygame.Color(255, 100, 100))
        for circle in circles:
            circle.update()
            circle.draw(surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                circles.append(Circle(x, y))

    pygame.quit()

if __name__ == '__main__':
    main()
