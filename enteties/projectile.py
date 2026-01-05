import pygame
from config.settings import *

class Projectile:
    SPEED = PROJECTILE_SPEED
    SIZE = PROJECTILE_SIZE
    COLOR = GREY

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dx = direction[0]
        self.dy = direction[1]
        self.size = Projectile.SIZE
        self.color = Projectile.COLOR
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
