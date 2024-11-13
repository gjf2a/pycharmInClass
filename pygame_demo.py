import pygame
from pygame.locals import *

class Circle:
    def __init__(self, x, y):
        self.radius = 50
        self.x = x
        self.y = y
        self.velocity_x = -1
        self.velocity_y = 1

    def contains(self, x: int, y: int) -> bool:
        distance = ((x - self.x) ** 2 + (y - self.y) ** 2)**(1/2)
        if distance <= self.radius:
            return True
        else:
            return False

    def teleport(self, x: int, y: int):
        self.x = x
        self.y = y

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
    current_background = pygame.Color(255, 255, 255)
    while running:
        pygame.time.delay(10)
        surface.fill(current_background)
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
            elif event.type == KEYDOWN:
                if event.key == K_b:
                    current_background = pygame.Color(0, 0, 255)
                if event.key == K_p:
                    current_background = pygame.Color(127, 0, 255)

    pygame.quit()

if __name__ == '__main__':
    main()
