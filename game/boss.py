from config.settings import *
import pygame


class Boss:
    def __init__(self):
        self.center = BOSS_CENTER
        self.radius = BOSS_RADIUS
        self.color = RED

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)