from config.settings import *
from random import randint
from enteties.hero import Player
from enteties.projectile import Projectile
from enemies.enemy_spawner import enemy_spawner
import pygame
import sys


class Enemy:
    def __init__(self):
        self.size = ENEMY_SIZE
        self.speed = ENEMY_SPEED
        self.color = RED
        self.enemies = []
        
    def move(self, player):
        enemies_killed = 0
        
        for enemy in self.enemies:
            if enemy.x < player.rect.x:
                enemy.x += self.speed
            if enemy.x > player.rect.x:
                enemy.x -= self.speed
            if enemy.y < player.rect.y:
                enemy.y += self.speed
            if enemy.y > player.rect.y:
                enemy.y -= self.speed

        for enemy in self.enemies[:]:
            if enemy.colliderect(player.rect):
                pygame.quit()
                sys.exit()

        for enemy in self.enemies[:]:
            for projectile in player.projectiles[:]:
                if enemy.colliderect(projectile.rect):
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                        enemies_killed += 1
                    if projectile in player.projectiles:
                        player.projectiles.remove(projectile)

        enemy_spawner(self.enemies)

        return enemies_killed
            
    def draw(self, screen):
        for enemy in self.enemies:
            pygame.draw.rect(screen, self.color, enemy)