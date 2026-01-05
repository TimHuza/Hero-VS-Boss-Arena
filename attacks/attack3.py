from game.boundary_wall import BoundaryWall
from config.settings import *
from pygame.locals import *
import pygame

WIDTH, HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT


class GauntletDeath:
    def __init__(self):
        self.size = 70
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.gauntlet_rect = pygame.Rect(self.x // 2 - 25, self.y, self.size, self.size)
        self.dx = 5
        self.dy = 20
        self.start_time = pygame.time.get_ticks()
        self.finished = False
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.gauntlet_rect)

    def move(self):
        self.gauntlet_rect.x += self.dx
        self.gauntlet_rect.y += self.dy
        
        if self.gauntlet_rect.right >= WIDTH // 2 or self.gauntlet_rect.left <= 0:
            self.dx = -self.dx
        if self.gauntlet_rect.bottom >= HEIGHT or self.gauntlet_rect.top <= 67:
            self.dy = -self.dy

    def update(self, player, screen):
        screen.fill(BLACK)

        # draw the boss
        pygame.draw.circle(screen, RED, (WIDTH * 3 // 4, HEIGHT // 2), 170)

        # draw the top line
        pygame.draw.line(screen, GREEN, (0, 65), (WIDTH, 65), 2)

        elapsed = pygame.time.get_ticks() - self.start_time
        seconds_left = 15 - elapsed // 1000
        timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, WHITE)
        screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH // 2, HEIGHT)
        player.draw(screen)

        BoundaryWall().draw_border(screen)

        self.draw(screen)
        self.move()

        # check if gauntlet collides with player
        if self.gauntlet_rect.colliderect(player.rect):
            return "GAME_OVER"
            
        # check if 15 seconds have passed
        if elapsed >= 15000:
            self.finished = True

        return self.finished


gauntlet = GauntletDeath()


def attack3_main(player, screen):
    if gauntlet.finished:
        gauntlet.reset()
    return gauntlet.update(player, screen)