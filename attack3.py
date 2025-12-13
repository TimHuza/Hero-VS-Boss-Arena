from pygame.locals import *
from attack4 import main as attack4_main
import pygame
import sys

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1300, 700

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hero vs Boss Arena")

font = pygame.font.SysFont("comicsans", 30)

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
colorkey = (55, 155, 255)
border = (0, 128, 255)

# GauntletDeath().x // 2 - 25
class Player:
    def __init__(self):
        self.x = WIDTH
        self.y = HEIGHT
        self.size = 50
        self.speed = 3
        self.color = white
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self, keys):
        if keys[K_LEFT] or keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_RIGHT] or keys[K_d]:
            self.rect.x += self.speed
        if keys[K_UP] or keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_DOWN] or keys[K_s]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH // 2:
            self.rect.right = WIDTH // 2 
        if self.rect.top < 67:
            self.rect.top = 67
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


class GauntletDeath:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = 70
        self.gauntlet_rect = pygame.Rect(self.x // 2 - 25, self.y, self.size, self.size)
        self.border_start = (WIDTH // 2, 67)
        self.border_end = (WIDTH // 2, HEIGHT)
        self.border_width = 2
        self.dx = 5
        self.dy = 20
    
    def draw(self):
        pygame.draw.line(screen, border, self.border_start, self.border_end, self.border_width)
        pygame.draw.rect(screen, red, self.gauntlet_rect)

    def move(self):
        self.gauntlet_rect.x += self.dx
        self.gauntlet_rect.y += self.dy
        
        if self.gauntlet_rect.right >= WIDTH // 2 or self.gauntlet_rect.left <= 0:
            self.dx = -self.dx
        if self.gauntlet_rect.bottom >= HEIGHT or self.gauntlet_rect.top <= 67:
            self.dy = -self.dy


player = Player()
gauntlet = GauntletDeath()


def main():
    start_time = pygame.time.get_ticks()
    
    run = True
    while run:
        screen.fill(black)

        # draw the boss
        pygame.draw.circle(screen, red, (WIDTH * 3 // 4, HEIGHT // 2), 170)

        # draw the top line
        start_point = (0, 65)
        end_point = (WIDTH, 65)
        line_width = 2
        pygame.draw.line(screen, green, start_point, end_point, line_width)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw()

        gauntlet.draw()
        gauntlet.move()

        # check if gauntlet collides with player
        if gauntlet.gauntlet_rect.colliderect(player.rect):
            print("Collision detected!")
            run = False
            
        # check if 15 seconds have passed
        if pygame.time.get_ticks() - start_time > 15000:
            attack4_main()
            run = False
            
        clock.tick(60)
        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()