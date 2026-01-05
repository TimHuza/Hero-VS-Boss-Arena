from pygame.locals import *
from config.settings import *
from enteties.projectile import Projectile
import pygame


class Player:
    def __init__(self, x, y):
        self.size = HERO_SIZE
        self.speed = HERO_SPEED
        self.color = WHITE
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.projectiles = []
        self.projectile_speed = Projectile.SPEED
        self.shoot_on_screen = False
        self.shoot_direction = (0, 0)
        self.cooldown = 0

    def move(self, keys, width, height):
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 67:
            self.rect.top = 67
        if self.rect.bottom > height:
            self.rect.bottom = height

        shoot = False

        if keys[K_LEFT]:
            self.shoot_direction = (-self.projectile_speed, 0)
            shoot = True
        elif keys[K_RIGHT]:
            self.shoot_direction = (self.projectile_speed, 0)
            shoot = True
        elif keys[K_UP]:
            self.shoot_direction = (0, -self.projectile_speed)
            shoot = True
        elif keys[K_DOWN]:
            self.shoot_direction = (0, self.projectile_speed)
            shoot = True

        for p in self.projectiles[:]:
            if p.rect.right < 0 or p.rect.left > width or p.rect.bottom < 90 or p.rect.top > height:
                self.projectiles.remove(p)

        if self.cooldown > 0:
            self.cooldown -= 1


        if shoot and self.cooldown == 0:
            if len(self.projectiles) < 4:
                self.projectiles.append(Projectile(self.rect.centerx - 10, self.rect.centery - 10, self.shoot_direction))
                self.cooldown = 20

        for projectile in self.projectiles:
            projectile.move()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

        for projectile in self.projectiles:
            projectile.draw(screen)