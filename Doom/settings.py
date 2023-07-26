# Game setting

import math

WIDTH = 1200
HEIGTH = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGTH = HEIGTH // 2
FPS = 60
TILE = 100

# FPS setting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 1200
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player
player_pos = (HALF_WIDTH, HALF_HEIGTH)
player_angle = 0
player_speed = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (73, 255, 76)
DARKGREEN = (0, 127, 14)
BLUE = (0, 0, 220)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)