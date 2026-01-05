
from game.boundary_wall import BoundaryWall
from config.settings import *
from pygame.locals import *
from random import randint
import pygame

WIDTH, HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT


class DodgeBlock:
    def __init__(self):
        self.size = 70
        self.reset()

    def reset(self):
        self.x = randint(0, WIDTH // 2 - 70)
        self.y = 0
        self.speed = randint(2, 8)
        self.dodge_rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self, screen):
        self.dodge_rect.y += self.speed

        if self.dodge_rect.bottom > 65:
            pygame.draw.rect(screen, RED, self.dodge_rect)

        if self.dodge_rect.top > HEIGHT:
            self.reset()


class DodgeFight:
    def __init__(self):
        self.reset()

    def reset(self):
        self.start_time = pygame.time.get_ticks()
        self.finished = False

        self.dodges = []

        self.dodges.append(DodgeBlock())
        self.dodges.append(DodgeBlock())
        self.dodges.append(DodgeBlock())
        self.dodges.append(DodgeBlock())
        self.dodges.append(DodgeBlock())
        self.dodges.append(DodgeBlock())
        self.dodges.append(DodgeBlock())
    
    def update(self, player, screen):
        screen.fill(BLACK)

        # boss
        pygame.draw.circle(screen, RED, (WIDTH * 3 // 4, HEIGHT // 2), 170)

        # top line
        pygame.draw.line(screen, GREEN, (0, 65), (WIDTH, 65), 2)

        # timer
        elapsed = pygame.time.get_ticks() - self.start_time
        seconds_left = 15 - elapsed // 1000
        timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, WHITE)
        screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH // 2, HEIGHT)
        player.draw(screen)

        BoundaryWall().draw_border(screen)

        # update dodge blocks
        for dodge in self.dodges:
            dodge.update(screen)

            if dodge.dodge_rect.colliderect(player.rect):
                return "GAME_OVER"

        if elapsed >= 15000:
            self.finished = True

        return self.finished


dodge_fight = DodgeFight()


def attack4_main(player, screen):
    if dodge_fight.finished:
        dodge_fight.reset()
    return dodge_fight.update(player, screen)