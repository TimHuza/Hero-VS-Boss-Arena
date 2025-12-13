from pygame.locals import *
from random import randint
from attack3 import main as attack3_main
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
white = (255, 255, 255)
colorkey = (55, 155, 255)


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

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 67:
            self.rect.top = 67
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        

class Coin:
    def __init__(self):
        self.img = pygame.image.load("data/imgs/coin.png")
        self.img.set_colorkey(colorkey)
        self.x = randint(0, WIDTH - 25)
        self.y = randint(67 - 25, HEIGHT - 25)
        self.size = 25
        self.rect = self.img.get_rect(topleft = (self.x, self.y))
        self.coin_on_screen = True

    def draw(self):
        screen.blit(self.img, self.rect)


player = Player()
circle_timer = 0
CIRCLE_DURATION = 30

coin = Coin()
coin_score = 0

def main():
    global coin_score
    coin_respawn_time = 0

    while True:
        coin_text = font.render(f"Coins: {coin_score}", 1, white)
        screen.fill(black)
        screen.blit(coin_text, (WIDTH - 10 - coin_text.get_width(), 10))

        # FOR TESTING
        if coin_score == 1:
            attack3_main()

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

        if coin.coin_on_screen:
            coin.draw()
            if player.rect.colliderect(coin.rect):
                coin.coin_on_screen = False
                coin_score += 1
                coin_respawn_time = pygame.time.get_ticks() + 5000
        else:
            current_time = pygame.time.get_ticks()
            if current_time >= coin_respawn_time:
                coin.coin_on_screen = True
                coin.x = randint(0, WIDTH - 25)
                coin.y = randint(0, HEIGHT - 25)
                coin.rect = coin.img.get_rect(topleft = (coin.x, coin.y))
            
        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()