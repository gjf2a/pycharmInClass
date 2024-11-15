import pygame
from pygame.locals import *
from typing import Dict, Tuple
import random

class Explorer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (80, 60)
        self.image = pygame.image.load('Green_Saucer.png')

    def key_move(self, key: int, moves: Dict[int,Tuple[int, int]]):
        if key in moves:
            x_change, y_change = moves[key]
            self.move(x_change, y_change)

    def move(self, x_change, y_change):
        self.x += x_change
        self.y += y_change

    def contains(self, x, y):
        start_x = self.x - self.size[0] // 2
        end_x = start_x + self.size[0]
        start_y = self.y - self.size[1] // 2
        end_y = start_y + self.size[1]
        if start_x <= x <= end_x and start_y <= y <= end_y:
            return True
        else:
            return False

    def draw(self, surface):
        resized_image = pygame.transform.scale(self.image, self.size)
        image_rect = resized_image.get_rect()
        image_rect.center = (self.x, self.y)
        surface.blit(resized_image, image_rect)


class SpaceJunk:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random.randint(0, self.width)
        self.y = random.randint(0, self.height)
        self.size = random.randint(5, 20)
        self.x_velocity = random.randint(1, 5)
        self.y_velocity = random.randint(1, 5)
        if random.random() < 0.5:
            self.x_velocity *= -1
        if random.random() < 0.5:
            self.y_velocity *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, 'gray', (self.x, self.y), self.size)

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        if self.x > self.width:
            self.x = 0
        elif self.x < 0:
            self.x = self.width
        if self.y > self.height:
            self.y = 0
        elif self.y < 0:
            self.y = self.height


EXPLORER_SPEED = 5
KEY_MOVES = {
    K_w: (0, -EXPLORER_SPEED),
    K_s: (0, EXPLORER_SPEED),
    K_a: (-EXPLORER_SPEED, 0),
    K_d: (EXPLORER_SPEED, 0)
}

def draw_all(surface, explorer, junk):
    surface.fill('black')
    for junk_item in junk:
        junk_item.update()
        junk_item.draw(surface)
    explorer.draw(surface)
    pygame.display.update()


def captured_junk(junk, explorer):
    captured = []
    for junk_item in junk:
        if explorer.contains(junk_item.x, junk_item.y):
            captured.append(junk_item)
    return captured


def remove_captured(junk, captured):
    for c in captured:
        junk.remove(c)


def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 480))
    explorer = Explorer(320, 240)
    junk = []
    for i in range(20):
        junk.append(SpaceJunk(surface.get_width(), surface.get_height()))

    current_key = None
    running = True
    while running:
        pygame.time.delay(50)
        if current_key is not None:
            explorer.key_move(current_key, KEY_MOVES)

        captured = captured_junk(junk, explorer)
        remove_captured(junk, captured)

        draw_all(surface, explorer, junk)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                current_key = event.key
            elif event.type == KEYUP:
                current_key = None

    pygame.quit()

if __name__ == '__main__':
    main()