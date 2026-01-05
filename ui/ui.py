from config.settings import *
import pygame


class UI:
    def __init__(self):
        self.font = pygame.font.SysFont("comicsans", 30)
        self.win_font = pygame.font.SysFont("comicsans", 60).render("Congrats! You won!", True, WHITE)
        self.lose_font = pygame.font.SysFont("comicsans", 60).render("You lost😢", True, WHITE)

    def draw_score(self, screen, score):
        score_text = self.font.render(f"Score: {score}", 1, WHITE)
        screen.blit(score_text, (0 + 10, 10))

    def draw_coin(self, screen, width, coin_score):
        coin_text = self.font.render(f"Coins: {coin_score}", 1, WHITE)
        screen.blit(coin_text, (width - 10 - coin_text.get_width(), 10))

    def draw_lose(self, screen, width, height):
        screen.blit(self.lose_font, (width // 2 - self.lose_font.get_width() // 2, height // 2 - 50))

    def draw_win(self, screen, width, height):
        screen.blit(self.win_font, (width // 2 - self.win_font.get_width() // 2, height // 65))