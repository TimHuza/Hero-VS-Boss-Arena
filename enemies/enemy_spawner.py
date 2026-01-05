from config.settings import *
from random import randint
from enteties.hero import Player
from enteties.projectile import Projectile
import pygame
import sys


def enemy_spawner(enemies):
    if len(enemies) < MIN_ENEMIES_ON_SCREEN:
        needed = MIN_ENEMIES_ON_SCREEN - len(enemies)
        for _ in range(needed):
            x = randint(0, SCREEN_WIDTH - ENEMY_SIZE)
            y = randint(67, SCREEN_HEIGHT - ENEMY_SIZE)
            enemies.append(pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE))
        