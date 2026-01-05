from game.boundary_wall import BoundaryWall
from config.settings import *
from pygame.locals import *
import pygame

WIDTH, HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT


class GauntletDeath:
    SPEED = 1.3
    THICKNESS = 150

    def __init__(self):
        self.finished = False

        # First row (top → down)
        self.row1_x = WIDTH // 4 - 150
        self.row1_top = 67
        self.row1_bottom = 67

        # Second row (bottom → up)
        self.row2_x = WIDTH // 4 + 150
        self.row2_bottom = HEIGHT
        self.row2_top = HEIGHT

        # First column (right → left)
        self.col1_right = WIDTH // 2
        self.col1_y = (HEIGHT + 67) // 2 - 150
        self.col1_left = WIDTH // 2

        # Second column (left → right)
        self.col2_left = 0
        self.col2_y = (HEIGHT + 67) // 2 + 150
        self.col2_right = 0

        # Collision rects (initialized empty)
        self.row1_rect = pygame.Rect(0, 0, 0, 0)
        self.row2_rect = pygame.Rect(0, 0, 0, 0)
        self.col1_rect = pygame.Rect(0, 0, 0, 0)
        self.col2_rect = pygame.Rect(0, 0, 0, 0)
        self.start_time = pygame.time.get_ticks()

    def draw_first_row(self, screen):
        self.row1_bottom += self.SPEED
        self.row1_rect = pygame.Rect(self.row1_x - self.THICKNESS // 2, self.row1_top, self.THICKNESS, self.row1_bottom - self.row1_top)
        pygame.draw.rect(screen, RED, self.row1_rect)

    def draw_second_row(self, screen):
        if self.row2_top > 67:
            self.row2_top -= self.SPEED
        self.row2_rect = pygame.Rect(self.row2_x - self.THICKNESS // 2, self.row2_top, self.THICKNESS, self.row2_bottom - self.row2_top)
        pygame.draw.rect(screen, RED, self.row2_rect)

    def draw_first_column(self, screen):
        if self.col1_left > 0:
            self.col1_left -= self.SPEED
        self.col1_rect = pygame.Rect(self.col1_left, self.col1_y - self.THICKNESS // 2, self.col1_right - self.col1_left, self.THICKNESS)
        pygame.draw.rect(screen, RED, self.col1_rect)

    def draw_second_column(self, screen):
        if self.col2_right < WIDTH // 2:
            self.col2_right += self.SPEED
        self.col2_rect = pygame.Rect(self.col2_left, self.col2_y - self.THICKNESS // 2, self.col2_right - self.col2_left, self.THICKNESS)
        pygame.draw.rect(screen, RED, self.col2_rect)

    def update(self, player, screen):
        screen.fill(BLACK)

        # draw the boss
        pygame.draw.circle(screen, RED, (WIDTH * 3 // 4, HEIGHT // 2), 170)

        # draw the top line
        pygame.draw.line(screen, GREEN, (0, 65), (WIDTH, 65), 2)
        
        # Timer
        elapsed = pygame.time.get_ticks() - self.start_time
        seconds_left = 15 - elapsed // 1000
        timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, WHITE)
        screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH // 2, HEIGHT)
        player.draw(screen)

        BoundaryWall().draw_border(screen)

        attack1.draw_first_row(screen)
        attack1.draw_second_row(screen)
        attack1.draw_first_column(screen)
        attack1.draw_second_column(screen)

        if player.rect.colliderect(attack1.row1_rect):
            return "GAME_OVER"
        if player.rect.colliderect(attack1.row2_rect):
            return "GAME_OVER"
        if player.rect.colliderect(attack1.col1_rect):
            return "GAME_OVER"
        if player.rect.colliderect(attack1.col2_rect):
            return "GAME_OVER"
            
        if elapsed >= 15000:
            self.finished = True
            
        return self.finished

attack1 = GauntletDeath()


def attack1_main(player, screen):    
    if attack1.finished:
        attack1.finished = False
        attack1.start_time = pygame.time.get_ticks()
    return attack1.update(player, screen)