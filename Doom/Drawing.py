from pickle import UNICODE
import pygame
from settings import *
from player import Player
from map import world_map

class Drawing():
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
    
    def background(self):
        pygame.draw.rect(self.sc, SKYBLUE, (0, 0, WIDTH, HALF_HEIGTH))
        pygame.draw.rect(self.sc, GREEN, (0, HALF_HEIGTH, WIDTH, HALF_HEIGTH))
    
    def draw_map(self, player):
        pygame.draw.circle(self.sc, DARKGREEN, (player.x // 4, player.y // 4), 3)
        pygame.draw.line(self.sc, DARKGREEN, (player.x // 4, player.y // 4), (player.x // 4 + WIDTH // 4 * math.cos(player.angle), player.y // 4 + WIDTH // 4 * math.sin(player.angle) ))
        for x, y in world_map: 
            pygame.draw.rect(self.sc, DARKGRAY, (x // 4, y // 4, TILE // 4, TILE // 4), 2) 
    
    def world(self, sc, player_pos, player_angle):
        cur_angle = player_angle - HALF_FOV
        xo, yo = player_pos
        for ray in range(NUM_RAYS):
            sin_a = math.sin(cur_angle)
            cos_a = math.cos(cur_angle)
            for depth in range(MAX_DEPTH):
                x = xo + depth * cos_a
                y = yo + depth * sin_a
                # pygame.draw.line(sc, DARKGRAY, player_pos, (x, y), 2)
                if (x // TILE * TILE, y // TILE * TILE) in world_map:
                    depth *= math.cos( player_angle - cur_angle )
                    proj_height = PROJ_COEFF / depth
                    c = 255 / (1 + depth * depth * 0.00002)
                    color = (c, c // 2, c // 3)
                    pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGTH - proj_height // 2, SCALE, proj_height))
                    break
            cur_angle += DELTA_ANGLE
    
    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render('FPS: ' + display_fps, 0, RED)
        self.sc.blit(render, (20 , 20))
    
    def mapping(a, b):
        return (a // TILE) * TILE, (b // TILE) * TILE
    
    def ray_casting(sc, player_pos, player_angle):
        ox, oy = player_pos
        xm, ym = mapping(ox, oy)
        cur_angle = player_angle - HALF_FOV
        for ray in range(NUM_RAYS):
            sin_a = math.sin(cur_angle)
            cos_a = math.cos(cur_angle)
            # verticals
            x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
            for i in range(0, WIDTH, TILE):
                depth_v = (x - ox) / cos_a
                y = oy + depth_v * sin_a
                if mapping(x + dx, y) in world_map:
                    break