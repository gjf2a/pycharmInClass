import pygame
from pygame.locals import *

import pygame_demo

def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 480))
    circle = pygame_demo.Circle(320, 240)
    running = True
    dragging = False
    while running:
        surface.fill(pygame.Color(255, 255, 255))
        circle.draw(surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if circle.contains(x, y):
                    dragging = True
                    circle.teleport(x, y)
            elif event.type == MOUSEBUTTONUP:
                dragging = False
            elif event.type == MOUSEMOTION:
                if dragging:
                    x, y = event.pos
                    circle.teleport(x, y)
    pygame.quit()

if __name__ == '__main__':
    main()