from config.settings import *
import pygame


class BoundaryWall:
    def __init__(self):
        self.start = BORDER_START
        self.end = BORDER_END
        self.width = BORDER_WIDTH
        self.color = BORDER_COLOR

    def draw_border(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)