from pygame.locals import *
from random import randint
import pygame
import sys, os

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1300, 700

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hero vs Boss Arena")

font = pygame.font.SysFont("comicsans", 30)

base_path = os.path.dirname(__file__)
coin_path = os.path.join(base_path, "data", "imgs", "coin.png")

BOSS_TRIGGER_SCORE = 15

MIN_ENEMIES_ON_SCREEN = 6

ATTACK_4_BONUS_SCORE = 20

HERO_SPEED = 4
HERO_SIZE = 50

ENEMY_SPEED = 1
ENEMY_SIZE = 35

PROJECTILE_SPEED = 8
PROJECTILE_SIZE = 20

BOSS_CENTER = (WIDTH * 3 // 4, HEIGHT // 2)
BOSS_RADIUS = 170

BORDER_START = (WIDTH // 2, 67)
BORDER_END = (WIDTH // 2, HEIGHT)
BORDER_WIDTH = 2
FPS = 60


THUNDER_ATTACK_DURATION = 5
THUNDER_ATTACK_REPEATS = 2

GAUNTLET_DX = 5
GAUNTLET_DY = 20

ASTEROID_FALL_SPEED = randint(2, 8)
ASTEROID_SPAWN_RATE = 30

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
COLORKEY = (55, 155, 255)
BORDER_COLOR = (0, 128, 255)
GREY = (128, 128, 128)

shopbackground = pygame.image.load(os.path.join(base_path, "data", "imgs", "shopbkrd.png")).convert()
menubackground = pygame.image.load(os.path.join(base_path, "data", "imgs", "background.png")).convert()
shopbtn = pygame.image.load(os.path.join(base_path, "data", "imgs", "shopbtn.png")).convert_alpha()
playbtn = pygame.image.load(os.path.join(base_path, "data", "imgs", "startbtn.png")).convert_alpha()
quitbtn = pygame.image.load(os.path.join(base_path, "data", "imgs", "quitbtn.png")).convert_alpha()

left_btn_img = pygame.image.load(os.path.join(base_path, "data", "imgs", "leftbutton.png")).convert_alpha()
right_btn_img = pygame.image.load(os.path.join(base_path, "data", "imgs", "rightbutton.png")).convert_alpha()
backbtn = pygame.image.load(os.path.join(base_path, "data", "imgs", "backbtn.png")).convert_alpha()
return_btn_img = pygame.image.load(os.path.join(base_path, "data", "imgs", "returnbtn.png")).convert_alpha()

left_btn_rect = left_btn_img.get_rect(topleft=(400, 300))
right_btn_rect = right_btn_img.get_rect(topleft=(700, 300))
backbtn_rect = backbtn.get_rect(topleft=(533, 475))
playbtn_rect = playbtn.get_rect(topleft=(457, 128))
shopbtn_rect = shopbtn.get_rect(topleft=(455, 284))
quitbtn_rect = quitbtn.get_rect(topleft=(455, 438))
return_btn_rect = return_btn_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
quitbtn_rect_loss = quitbtn.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
player_color = WHITE

win_img = pygame.image.load(os.path.join(base_path, "data", "imgs", "win.png")).convert()
win_btn_rect = return_btn_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))

colors = [
    (0, 0, 255),
    (0, 255, 0),
    (255, 0, 0),
    (255, 165, 0),
    (128, 0, 128),
    (255, 192, 203),
    (255, 255, 0),
    (0, 255, 255),
    (165, 42, 42),
    (255, 255, 255)
]


def buttons():
    screen.blit(playbtn, playbtn_rect)
    screen.blit(shopbtn, shopbtn_rect)
    screen.blit(quitbtn, quitbtn_rect)


def start_screen(player):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if playbtn_rect.collidepoint(event.pos):
                    return
                elif shopbtn_rect.collidepoint(event.pos):
                    shop_screen(player)
                elif quitbtn_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        screen.blit(menubackground, (0, 0))
        buttons()
        pygame.display.update()
        clock.tick(FPS)


def shop_screen(player):
    global player_color
    color_index = colors.index(player_color)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if left_btn_rect.collidepoint(event.pos):
                    color_index = (color_index - 1) % len(colors)
                    player_color = colors[color_index]
                if right_btn_rect.collidepoint(event.pos):
                    color_index = (color_index + 1) % len(colors)
                    player_color = colors[color_index]
                if backbtn_rect.collidepoint(event.pos):
                    return
        screen.blit(shopbackground, (0, 0))
        screen.blit(left_btn_img, left_btn_rect)
        screen.blit(right_btn_img, right_btn_rect)
        screen.blit(backbtn, backbtn_rect)
        player_rect = pygame.Rect(WIDTH // 2 - player.size // 2 - 10, HEIGHT // 2 - player.size // 2 - 30, player.size, player.size)
        pygame.draw.rect(screen, player_color, player_rect)
        pygame.display.update()
        clock.tick(FPS)


def loss_screen():
    global player, enemy, coin, coin_score, enemy_score, player_skin_index, player_color

    while True:
        screen.fill(BLACK)

        screen.blit(return_btn_img, return_btn_rect)
        screen.blit(quitbtn, quitbtn_rect_loss)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if return_btn_rect.collidepoint(event.pos):
                    enemy_score = 0
                    player = Player()
                    enemy = Enemy()
                    coin = Coin()
                    start_screen(player)
                    return
                if quitbtn_rect_loss.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(FPS)


def win_screen():
    global player, enemy, coin, coin_score, enemy_score, player_color

    while True:
        screen.fill(BLACK)
        screen.blit(win_img, (0, 0))
        screen.blit(return_btn_img, win_btn_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if win_btn_rect.collidepoint(event.pos):
                    enemy_score = 0
                    coin_score = 0
                    player = Player()
                    enemy = Enemy()
                    coin = Coin()
                    start_screen(player)
                    return

        pygame.display.update()
        clock.tick(FPS)


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


class Player:
    def __init__(self):
        self.x = WIDTH // 2 - 25
        self.y = HEIGHT // 2 - 25
        self.size = 50
        self.speed = 4
        self.color = player_color
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.projectiles = []
        self.projectile_speed = Projectile.SPEED
        self.shoot_on_screen = False
        self.shoot_direction = (0, 0)
        self.cooldown = 0

    def move(self, keys):
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 67:
            self.rect.top = 67
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        shoot = False

        if keys[K_LEFT]:
            self.shoot_direction = (-self.projectile_speed, 0)
            shoot = True
        elif keys[K_RIGHT]:
            self.shoot_direction = (self.projectile_speed, 0)
            shoot = True
        elif keys[K_UP]:
            self.shoot_direction = (0, -self.projectile_speed)
            shoot = True
        elif keys[K_DOWN]:
            self.shoot_direction = (0, self.projectile_speed)
            shoot = True

        for p in self.projectiles[:]:
            if p.rect.right < 0 or p.rect.left > WIDTH or p.rect.bottom < 90 or p.rect.top > HEIGHT:
                self.projectiles.remove(p)

        if self.cooldown > 0:
            self.cooldown -= 1

        if shoot and self.cooldown == 0:
            if len(self.projectiles) < 4:
                self.projectiles.append(Projectile(self.rect.centerx - 10, self.rect.centery - 10, self.shoot_direction))
                self.cooldown = 20

        for projectile in self.projectiles:
            projectile.move()

    def draw(self, screen):
        self.color = player_color
        pygame.draw.rect(screen, self.color, self.rect)
        for p in self.projectiles:
            p.draw(screen)


class PlayerAttack:
    def __init__(self):
        self.x = WIDTH
        self.y = HEIGHT
        self.size = 50
        self.speed = 4
        self.color = WHITE
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self, keys):
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH // 2:
            self.rect.right = WIDTH // 2
        if self.rect.top < 67:
            self.rect.top = 67
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Enemy:
    def __init__(self):
        self.size = ENEMY_SIZE
        self.speed = ENEMY_SPEED
        self.color = RED
        self.enemies = []
       
    def move(self, player):
        enemies_killed = 0
       
        for enemy in self.enemies:
            if enemy.x < player.rect.x:
                enemy.x += self.speed
            if enemy.x > player.rect.x:
                enemy.x -= self.speed
            if enemy.y < player.rect.y:
                enemy.y += self.speed
            if enemy.y > player.rect.y:
                enemy.y -= self.speed

        for enemy in self.enemies[:]:
            if enemy.colliderect(player.rect):
                loss_screen()
                return 0

        for enemy in self.enemies[:]:
            for projectile in player.projectiles[:]:
                if enemy.colliderect(projectile.rect):
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                        enemies_killed += 1
                    if projectile in player.projectiles:
                        player.projectiles.remove(projectile)

        enemy_spawner(self.enemies)

        return enemies_killed
           
    def draw(self, screen):
        for enemy in self.enemies:
            pygame.draw.rect(screen, self.color, enemy)


def enemy_spawner(enemies):
    if len(enemies) < MIN_ENEMIES_ON_SCREEN:
        needed = MIN_ENEMIES_ON_SCREEN - len(enemies)
        for _ in range(needed):
            x = randint(0, WIDTH - ENEMY_SIZE)
            y = randint(67, HEIGHT - ENEMY_SIZE)
            enemies.append(pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE))


class Projectile:
    SPEED = PROJECTILE_SPEED
    SIZE = PROJECTILE_SIZE
    COLOR = GREY

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dx = direction[0]
        self.dy = direction[1]
        self.size = Projectile.SIZE
        self.color = Projectile.COLOR
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
       

class Coin:
    def __init__(self):
        self.img = pygame.image.load(coin_path)
        self.img.set_colorkey(COLORKEY)
        self.x = randint(0, WIDTH - 25)
        self.y = randint(67 - 25, HEIGHT - 25)
        self.size = 25
        self.rect = self.img.get_rect(topleft = (self.x, self.y))
        self.coin_on_screen = True

    def draw(self):
        screen.blit(self.img, self.rect)


class BoundaryWall:
    def __init__(self):
        self.start = BORDER_START
        self.end = BORDER_END
        self.width = BORDER_WIDTH
        self.color = BORDER_COLOR

    def draw_border(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)


class GroundDanger:
    SPEED = 1.3
    THICKNESS = 150

    def __init__(self):
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

attack1 = GroundDanger()


def attack1_main(player, screen):
    global attack1
    attack1 = GroundDanger()
    player.rect.center = (WIDTH // 4, HEIGHT // 2)

    state = "WAIT"
    state_start_time = pygame.time.get_ticks()
   
    run = True
    while run:
        clock.tick(60)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # draw the boss
        pygame.draw.circle(screen, RED, (WIDTH * 3 // 4, HEIGHT // 2), 170)

        # draw the top line
        pygame.draw.line(screen, GREEN, (0, 65), (WIDTH, 65), 2)
        
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw(screen)

        BoundaryWall().draw_border(screen)

        if state == "WAIT":
             if pygame.time.get_ticks() - state_start_time >= 2000:
                 state = "ATTACK"
                 attack1.start_time = pygame.time.get_ticks()

        elif state == "ATTACK":
            # Timer
            elapsed = pygame.time.get_ticks() - attack1.start_time
            seconds_left = 15 - elapsed // 1000
            timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, WHITE)
            screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

            attack1.draw_first_row(screen)
            attack1.draw_second_row(screen)
            attack1.draw_first_column(screen)
            attack1.draw_second_column(screen)

            if player.rect.colliderect(attack1.row1_rect) or player.rect.colliderect(attack1.row2_rect) or player.rect.colliderect(attack1.col1_rect) or player.rect.colliderect(attack1.col2_rect):
                loss_screen()
                return
            
            if elapsed >= 15000:
                attack2_main(player, screen)
                return

        pygame.display.update()
   

class ThunderNightmare:
    def __init__(self):
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

thunder = ThunderNightmare()


def attack2_main(player, screen):
    state = "WAIT1"
    state_start_time = pygame.time.get_ticks()
   
    run = True
    while run:
        screen.fill(BLACK)

        # draw the boss
        pygame.draw.circle(screen, RED, (WIDTH * 3 // 4, HEIGHT // 2), 170)

        # draw the top line
        start_point = (0, 65)
        end_point = (WIDTH, 65)
        line_width = 2
        pygame.draw.line(screen, GREEN, start_point, end_point, line_width)

        BoundaryWall().draw_border(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw(screen)

        current_time = pygame.time.get_ticks()
        elapsed = current_time - state_start_time

        if state == "WAIT1":
            if elapsed >= 2000:
                state = "ATTACK1"
                state_start_time = current_time

        elif state == "ATTACK1":
            seconds_left = 5 - elapsed // 1000
            timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, WHITE)
            screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

            thunder.draw(screen)

            # check if player collides with line
            if player.rect.clipline(thunder.coll_diag_line):
                pygame.quit()
                sys.exit()
            if player.rect.clipline(thunder.coll_second_diag_line):
                pygame.quit()
                sys.exit()
            if player.rect.clipline(thunder.coll_hor_line):
                pygame.quit()
                sys.exit()
            if player.rect.clipline(thunder.coll_ver_line):
                pygame.quit()
                sys.exit()

            if elapsed >= 5000:
                state = "WAIT2"
                state_start_time = current_time

        elif state == "WAIT2":
            if elapsed >= 2000:
                state = "ATTACK2"
                state_start_time = current_time

        elif state == "ATTACK2":
            seconds_left = 5 - elapsed // 1000
            timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, WHITE)
            screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

            thunder.draw(screen)

            # check if player collides with line
            if player.rect.clipline(thunder.coll_diag_line):
                pygame.quit()
                sys.exit()
            if player.rect.clipline(thunder.coll_second_diag_line):
                pygame.quit()
                sys.exit()
            if player.rect.clipline(thunder.coll_hor_line):
                pygame.quit()
                sys.exit()
            if player.rect.clipline(thunder.coll_ver_line):
                pygame.quit()
                sys.exit()

            if elapsed >= 5000:
                attack3_main(player, screen)
                run = False
           
        clock.tick(60)
        pygame.display.update()


class GauntletDeath:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = 70
        self.gauntlet_rect = pygame.Rect(self.x // 2 - 25, self.y, self.size, self.size)
        self.dx = 5
        self.dy = 20
   
    def move(self):
        self.gauntlet_rect.x += self.dx
        self.gauntlet_rect.y += self.dy
       
        if self.gauntlet_rect.right >= WIDTH // 2 or self.gauntlet_rect.left <= 0:
            self.dx = -self.dx
        if self.gauntlet_rect.bottom >= HEIGHT or self.gauntlet_rect.top <= 67:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.gauntlet_rect)

gauntlet = GauntletDeath()


def attack3_main(player, screen):
    start_time = pygame.time.get_ticks()
   
    run = True
    while run:
        screen.fill(BLACK)

        # draw the boss
        pygame.draw.circle(screen, RED, (WIDTH * 3 // 4, HEIGHT // 2), 170)

        # draw the top line
        start_point = (0, 65)
        end_point = (WIDTH, 65)
        line_width = 2
        pygame.draw.line(screen, GREEN, start_point, end_point, line_width)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        seconds_left = 15 - (pygame.time.get_ticks() - start_time) // 1000
        timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, WHITE)
        screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw(screen)

        BoundaryWall().draw_border(screen)

        gauntlet.move()
        gauntlet.draw(screen)

        # check if gauntlet collides with player
        if gauntlet.gauntlet_rect.colliderect(player.rect):
            loss_screen()
            return
           
        # check if 15 seconds have passed
        if pygame.time.get_ticks() - start_time > 15000:
            attack4_main(player, screen)
            run = False
           
        clock.tick(60)
        pygame.display.update()


class DodgeFight:
    def __init__(self):
        self.x = randint(0, WIDTH // 2 - 70)
        self.y = 0
        self.speed = randint(2, 8)
        self.size = 70
        self.dodge_rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self):
        if self.dodge_rect.bottom < 65:
            pass
        else:
            pygame.draw.rect(screen, RED, self.dodge_rect)

    def move(self):
        self.dodge_rect.move_ip(0, self.speed)

player = Player()
dodge_border = DodgeFight()
dodges = [DodgeFight(), DodgeFight(), DodgeFight(), DodgeFight(), DodgeFight(), DodgeFight(), DodgeFight()]

GAME_PLAYING = "playing"
GAME_WIN = "win"


def attack4_main(player, screen):
    start_time = pygame.time.get_ticks()
    game_state = GAME_PLAYING
   
    run = True
    while run:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # PLAYING STATE  
        if game_state == GAME_PLAYING:
            seconds_left = 15 - (pygame.time.get_ticks() - start_time) // 1000
            timer = pygame.font.SysFont(None, 50).render(str(max(seconds_left, 0)), True, WHITE)
            screen.blit(timer, (WIDTH // 2, HEIGHT // 65))

            # draw the boss
            pygame.draw.circle(screen, RED, (WIDTH * 3 // 4, HEIGHT // 2), 170)

            # draw the top line
            start_point = (0, 65)
            end_point = (WIDTH, 65)
            line_width = 2
            pygame.draw.line(screen, GREEN, start_point, end_point, line_width)

            keys = pygame.key.get_pressed()
            player.move(keys)
            player.draw(screen)

            BoundaryWall().draw_border(screen)

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
                        loss_screen()
                        return
                   
            # check if 15 seconds have passed
            if pygame.time.get_ticks() - start_time > 15000:
                win_screen()
                return

        clock.tick(60)
        pygame.display.update()

ui = UI()


player = Player()
player_attack = PlayerAttack()
circle_timer = 0
CIRCLE_DURATION = 30

enemy = Enemy()

coin = Coin()
coin_score = 0

enemy_score = 0


def main():
    global coin_score, enemy_score
    coin_respawn_time = 0

    while True:
        screen.fill(BLACK)
        ui.draw_score(screen, enemy_score)
        ui.draw_coin(screen, WIDTH, coin_score)

        # FOR TESTING
        if enemy_score >= BOSS_TRIGGER_SCORE:
            attack1_main(player_attack, screen)

        start_point = (0, 65)
        end_point = (WIDTH, 65)
        line_width = 2
        pygame.draw.line(screen, GREEN, start_point, end_point, line_width)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw(screen)

        enemy_score += enemy.move(player)
        enemy.draw(screen)

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
    start_screen(player)
    main()