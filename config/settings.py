from random import randint

# ===============================
# SCREEN SETTINGS
# ===============================

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 700
SCREEN_FPS = 60


# ===============================
# GAME PHASE SETTINGS
# ===============================

# Score required to trigger the boss phase
BOSS_TRIGGER_SCORE = 5

# Minimum enemies during enemy phase
MIN_ENEMIES_ON_SCREEN = 6

# Bonus score for surviving Attack 4
ATTACK_4_BONUS_SCORE = 20


# ===============================
# HERO SETTINGS
# ===============================

HERO_SPEED = 4
HERO_SIZE = 50


# ===============================
# ENEMY SETTINGS
# ===============================

ENEMY_SPEED = 2
ENEMY_SIZE = 35


# ===============================
# PROJECTILE SETTINGS
# ===============================

PROJECTILE_SPEED = 8
PROJECTILE_SIZE = 20


# ===============================
# BOSS SETTINGS
# ===============================

BOSS_CENTER = (SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT // 2)
BOSS_RADIUS = 170


# ===============================
# BOUNDARY WALL SETTINGS
# ===============================

BORDER_START = (SCREEN_WIDTH // 2, 67)
BORDER_END = (SCREEN_WIDTH // 2, SCREEN_HEIGHT)
BORDER_WIDTH = 2


# ===============================
# ATTACK SETTINGS
# ===============================

# Attack 2 (Thunder Nightmare)
THUNDER_ATTACK_DURATION = 5       # seconds
THUNDER_ATTACK_REPEATS = 2

# Attack 3 (Gauntlet Death)
GAUNTLET_DX = 5
GAUNTLET_DY = 20

# Attack 4 (Dodge Fight)
ASTEROID_FALL_SPEED = randint(2, 8)
ASTEROID_SPAWN_RATE = 30          # frames


# ===============================
# COLORS
# ===============================

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
COLORKEY = (55, 155, 255)
BORDER_COLOR = (0, 128, 255)
GREY = (128, 128, 128)