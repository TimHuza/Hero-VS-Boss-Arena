from pygame.locals import *
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

black = (0, 0, 0)
white = (255, 255, 255)


class Player:
    def __init__(self):
        self.x = WIDTH // 2 - 25
        self.y = HEIGHT // 2 - 25
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
        self.rect.clamp_ip(screen.get_rect())

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


player = Player()
circle_timer = 0
CIRCLE_DURATION = 30


def main():
    while True:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw()
            
        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()