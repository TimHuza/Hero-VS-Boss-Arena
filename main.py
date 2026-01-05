from config.settings import *
from game.game_manager import GameManager
from enteties.hero import Player
from enteties.enemy import Enemy
import pygame, sys

pygame.init()

WIDTH, HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hero VS Boss Arena")

clock = pygame.time.Clock()

hero = Player(WIDTH // 2 - 25, HEIGHT // 2 - 25)
game_manager = GameManager(hero)


def main():
    run = True
    while run:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        start_point = (0, 65)
        end_point = (WIDTH, 65)
        line_width = 2
        pygame.draw.line(screen, GREEN, start_point, end_point, line_width)
        
        keys = pygame.key.get_pressed()

        game_manager.update(screen, keys, WIDTH, HEIGHT)
        game_manager.draw(screen)

        clock.tick(SCREEN_FPS)
        pygame.display.update()


if __name__ == "__main__":
    main()


