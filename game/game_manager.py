from config.settings import *
from enteties.enemy import Enemy
from attacks.attack_phase import AttackPhase
from game.boss import Boss
from ui.ui import UI
import pygame

class GameManager:
    ENEMY_PHASE = "enemy_phase"
    BOSS_PHASE = "boss_phase"
    VICTORY = "victory"
    GAME_OVER = "game_over"

    def __init__(self, hero):
        self.state = self.ENEMY_PHASE
        self.score = 0
        self.hero = hero
        self.enemy_spawner = Enemy()
        self.attack_phase = None
        self.border = None
        self.boss = Boss()
        self.boss_wait_start = 0
        self.ui = UI()

    def update(self, screen, keys, width, height):
        if self.state not in (self.VICTORY, self.GAME_OVER):
            self.hero.move(keys, width, height)

        # ---------- ENEMY PHASE ----------
        if self.state == self.ENEMY_PHASE:
            kills = self.enemy_spawner.move(self.hero)
            self.score += kills
            if self.score >= BOSS_TRIGGER_SCORE:
                self.state = self.BOSS_PHASE
                self.attack_phase = AttackPhase()
                self.hero.rect.center = (width // 4, height // 2)
                self.boss_wait_start = pygame.time.get_ticks()

        # ---------- BOSS PHASE ----------
        elif self.state == self.BOSS_PHASE:
            current_time = pygame.time.get_ticks()
            if current_time - self.boss_wait_start < 5000:
                screen.fill(BLACK)
                
                # Draw boss (right side)
                pygame.draw.circle(screen, RED, (width * 3 // 4, height // 2), 170)
                
                # Draw border
                pygame.draw.line(screen, GREEN, (width // 2, 65), (width // 2, height), 2)
                
                # Draw hero
                self.hero.draw(screen)
                
                # Draw score
                self.ui.draw_score(screen, self.score)
                
                # Optional: Timer text
                wait_seconds = 5 - (current_time - self.boss_wait_start) // 1000
                font = pygame.font.SysFont(None, 50)
                text = font.render(f"BOSS STARTING IN {wait_seconds}...", True, WHITE)
                screen.blit(text, (width // 2 - text.get_width() // 2, 20))
                
                return # Skip updating attacks until wait is over

            if self.attack_phase:
                self.attack_phase.update(self.hero, screen)
                if self.attack_phase.game_over:
                    self.state = self.GAME_OVER
                elif self.attack_phase.finished:
                    self.state = self.VICTORY

        # ---------- VICTORY / GAME OVER ----------
        elif self.state == self.VICTORY:
            self.ui.draw_win(screen, width, height)
        elif self.state == self.GAME_OVER:
            self.ui.draw_lose(screen, width, height)

    def draw(self, screen):       
        if self.state == self.ENEMY_PHASE:
            self.hero.draw(screen)
            self.enemy_spawner.draw(screen)
            self.ui.draw_score(screen, self.score)

        elif self.state == self.BOSS_PHASE:
            # Drawing is handled in update() for attacks
            pass

        elif self.state == self.VICTORY:
            self.ui.draw_win(screen, width, height)