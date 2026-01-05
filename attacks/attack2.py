from game.boundary_wall import BoundaryWall
from config.settings import *
from pygame.locals import *
import pygame

WIDTH, HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT


class ThunderNightmare:
    def __init__(self):
        self.finished = False
        self.state = "WAIT1"
        self.state_start_time = pygame.time.get_ticks()

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
    
    def draw(self, screen):
        pygame.draw.line(screen, RED, self.diag_start_pos, self.diag_end_pos, self.diag_width)
        pygame.draw.line(screen, RED, self.second_diag_start_pos, self.second_diag_end_pos, self.second_diag_width)
        pygame.draw.line(screen, RED, self.hor_start_pos, self.hor_end_pos, self.hor_width)
        pygame.draw.line(screen, RED, self.ver_start_pos, self.ver_end_pos, self.ver_width)

    def update(self, player, screen):
        screen.fill(BLACK)

        # draw the boss
        pygame.draw.circle(screen, RED, (WIDTH * 3 // 4, HEIGHT // 2), 170)

        # draw the top line
        pygame.draw.line(screen, GREEN, (0, 65), (WIDTH, 65), 2)

        BoundaryWall().draw_border(screen)

        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH // 2, HEIGHT)
        player.draw(screen)

        current_time = pygame.time.get_ticks()
        elapsed = current_time - self.state_start_time

        if self.state == "WAIT1":
            if elapsed >= 2000:
                self.state = "ATTACK1"
                self.state_start_time = current_time

        elif self.state == "ATTACK1":
            seconds_left = 5 - elapsed // 1000
            timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, WHITE)
            screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

            self.draw(screen)

            # check if player collides with line
            if player.rect.clipline(self.coll_diag_line):
                run = False
            if player.rect.clipline(self.coll_second_diag_line):
                run = False
            if player.rect.clipline(self.coll_hor_line):
                run = False
            if player.rect.clipline(self.coll_ver_line):
                run = False

            if elapsed >= 5000:
                self.state = "WAIT2"
                self.state_start_time = current_time

        elif self.state == "WAIT2":
            if elapsed >= 2000:
                self.state = "ATTACK2"
                self.state_start_time = current_time

        elif self.state == "ATTACK2":
            seconds_left = 5 - elapsed // 1000
            timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, WHITE)
            screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

            self.draw(screen)

            # check if player collides with line
            if player.rect.clipline(self.coll_diag_line):
                return "GAME_OVER"
            if player.rect.clipline(self.coll_second_diag_line):
                return "GAME_OVER"
            if player.rect.clipline(self.coll_hor_line):
                return "GAME_OVER"
            if player.rect.clipline(self.coll_ver_line):
                return "GAME_OVER"

            if elapsed >= 5000:
                self.finished = True
            
        return self.finished

thunder = ThunderNightmare()


def attack2_main(player, screen):
    return thunder.update(player, screen)