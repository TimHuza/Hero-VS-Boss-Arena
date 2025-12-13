
from pygame.locals import *
from random import randint
from time import sleep
import pygame
import sys

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1300, 700

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hero vs Boss Arena")

score_font = pygame.font.SysFont("comicsans", 30)

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
        self.speed = 4
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


class DodgeFight:
    def __init__(self):
        self.x = randint(0, WIDTH // 2 - 70)
        self.y = 0
        self.speed = randint(2, 8)
        self.size = 70
        self.dodge_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.border_start = (WIDTH // 2, 67)
        self.border_end = (WIDTH // 2, HEIGHT)
        self.border_width = 2

    def draw_border(self):
        pygame.draw.line(screen, border, self.border_start, self.border_end, self.border_width)

    def draw(self):
        if self.dodge_rect.bottom < 65:
            pass
        else:
            pygame.draw.rect(screen, red, self.dodge_rect)

    def move(self):
        self.dodge_rect.move_ip(0, self.speed)


player = Player()
dodge_border = DodgeFight()
dodges = [DodgeFight(), DodgeFight(), DodgeFight(), DodgeFight(), DodgeFight(), DodgeFight(), DodgeFight()]

GAME_PLAYING = "playing"
GAME_WIN = "win"


def main():
    start_time = pygame.time.get_ticks()
    game_state = GAME_PLAYING
    
    run = True
    while run:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # PLAYING STATE  
        if game_state == GAME_PLAYING:
            seconds_left = 15 - (pygame.time.get_ticks() - start_time) // 1000
            timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, white)
            screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

            # draw the boss
            pygame.draw.circle(screen, red, (WIDTH * 3 // 4, HEIGHT // 2), 170)

            # draw the top line
            start_point = (0, 65)
            end_point = (WIDTH, 65)
            line_width = 2
            pygame.draw.line(screen, green, start_point, end_point, line_width)

            keys = pygame.key.get_pressed()
            player.move(keys)
            player.draw()

            dodge_border.draw_border()
            if pygame.time.get_ticks() - start_time > 1000:
                for dodge in dodges[:]:
                    dodge.draw()
                    dodge.move()

                    # remove dodge rect if it goes off screen
                    if dodge.dodge_rect.top > HEIGHT:
                        dodges.remove(dodge)
                        dodges.append(DodgeFight())

                    # check dodge rect collison with player
                    if dodge.dodge_rect.colliderect(player.rect):
                        run = False
                    
            # check if 15 seconds have passed
            if pygame.time.get_ticks() - start_time > 15000:
                game_state = GAME_WIN

        # WIN STATE           
        elif game_state == GAME_WIN:
            win_font = pygame.font.SysFont("comicsans", 60).render("Congrats! You won!", True, white)
            screen.blit(win_font, (WIDTH // 2 - win_font.get_width() // 2, 70))

        clock.tick(60)
        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()