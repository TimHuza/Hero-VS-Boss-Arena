import pygame
from pygame.locals import *
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


class ThunderNightmare:
    def __init__(self):
        # border
        self.border_start = (WIDTH // 2, 67)
        self.border_end = (WIDTH // 2, HEIGHT)
        self.border_width = 2

        # first diagonal line
        self.diag_start_pos = (0, 67)
        self.diag_end_pos = (WIDTH // 2, HEIGHT)
        self.diag_width = 2
        self.coll_diag_line = (self.diag_start_pos, self.diag_end_pos)

        # second diagonal line
        self.second_diag_start_pos = (WIDTH // 2, 67)
        self.second_diag_end_pos = (0, HEIGHT)
        self.second_diag_width = 2
        self.coll_second_diag_line = (self.second_diag_start_pos, self.second_diag_end_pos)

        # horizontal line
        self.hor_start_pos = (0, HEIGHT // 2 + 32)
        self.hor_end_pos = (WIDTH // 2, HEIGHT // 2 + 32)
        self.hor_width = 2
        self.coll_hor_line = (self.hor_start_pos, self.hor_end_pos)

        # vertical line
        self.ver_start_pos = (WIDTH * 3 // 12, 67)
        self.ver_end_pos = (WIDTH * 3 // 12, HEIGHT)
        self.ver_width = 2
        self.coll_ver_line = (self.ver_start_pos, self.ver_end_pos)
    

    def draw_border(self):
        pygame.draw.line(screen, border, self.border_start, self.border_end, self.border_width)
    
    def draw(self):
        pygame.draw.line(screen, red, self.diag_start_pos, self.diag_end_pos, self.diag_width)
        pygame.draw.line(screen, red, self.second_diag_start_pos, self.second_diag_end_pos, self.second_diag_width)
        pygame.draw.line(screen, red, self.hor_start_pos, self.hor_end_pos, self.hor_width)
        pygame.draw.line(screen, red, self.ver_start_pos, self.ver_end_pos, self.ver_width)



player = Player()
thunder = ThunderNightmare()


def main():
    state = "WAIT1"
    state_start_time = pygame.time.get_ticks()
    
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

        thunder.draw_border()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw()

        current_time = pygame.time.get_ticks()
        elapsed = current_time - state_start_time

        if state == "WAIT1":
            if elapsed >= 2000:
                state = "ATTACK1"
                state_start_time = current_time

        elif state == "ATTACK1":
            seconds_left = 5 - elapsed // 1000
            timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, white)
            screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

            thunder.draw()

            # check if player collides with line
            if player.rect.clipline(thunder.coll_diag_line):
                run = False
            if player.rect.clipline(thunder.coll_second_diag_line):
                run = False
            if player.rect.clipline(thunder.coll_hor_line):
                run = False
            if player.rect.clipline(thunder.coll_ver_line):
                run = False

            if elapsed >= 5000:
                state = "WAIT2"
                state_start_time = current_time

        elif state == "WAIT2":
            if elapsed >= 2000:
                state = "ATTACK2"
                state_start_time = current_time

        elif state == "ATTACK2":
            seconds_left = 5 - elapsed // 1000
            timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, white)
            screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

            thunder.draw()

            # check if player collides with line
            if player.rect.clipline(thunder.coll_diag_line):
                run = False
            if player.rect.clipline(thunder.coll_second_diag_line):
                run = False
            if player.rect.clipline(thunder.coll_hor_line):
                run = False
            if player.rect.clipline(thunder.coll_ver_line):
                run = False

            if elapsed >= 5000:
                attack3_main()
                run = False
            
        clock.tick(60)
        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()