import pygame
from pygame.locals import *

# Text rendering reference: https://www.perplexity.ai/search/show-me-some-pygame-code-to-re-LhQAgCrEThCohZvixdV.ig

SHAPE_SPEED = 10

MY_KEY_MOVES = {
    K_s: (0, SHAPE_SPEED),
    K_w: (0, -SHAPE_SPEED),
    K_a: (-SHAPE_SPEED, 0),
    K_d: (SHAPE_SPEED, 0),
    K_q: (-SHAPE_SPEED, -SHAPE_SPEED),
    K_e: (SHAPE_SPEED, -SHAPE_SPEED),
    K_c: (SHAPE_SPEED, SHAPE_SPEED),
    K_z: (-SHAPE_SPEED, SHAPE_SPEED)
}


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


class FloatingText:
    def __init__(self, text: str, x: int, y: int, font_size: int):
        font = pygame.font.SysFont("Arial", font_size)
        self.text_image = font.render(text, True, (127, 0, 255))
        self.x = x
        self.y = y

    def draw(self, surface):
        rect = self.text_image.get_rect(center=(self.x, self.y))
        surface.blit(self.text_image, rect)

    def update(self):
        pass


def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 480))
    running = True
    shapes = [FloatingText("Purple!", 320, 240, 48)]
    current_background = pygame.Color(255, 255, 255)
    while running:
        pygame.time.delay(10)
        surface.fill(current_background)
        for circle in shapes:
            circle.update()
            circle.draw(surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                shapes.append(Circle(x, y))
            elif event.type == KEYDOWN:
                if event.key == K_b:
                    current_background = pygame.Color(0, 0, 255)
                elif event.key == K_p:
                    current_background = pygame.Color(127, 0, 255)
                elif event.key in MY_KEY_MOVES:
                    x_change, y_change = MY_KEY_MOVES[event.key]
                    for shape in shapes:
                        shape.x += x_change
                        shape.y += y_change

    pygame.quit()

if __name__ == '__main__':
    main()
