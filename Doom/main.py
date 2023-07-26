import pygame
import math
from settings import *
from player import Player
from map import world_map
from Drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGTH))
clock = pygame.time.Clock()

player = Player()
drawing = Drawing(sc)

# Главный цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()     
    
    drawing.background()
    drawing.world(sc, player.pos, player.angle)
    drawing.draw_map(player)
    drawing.fps(clock)
 
    pygame.display.flip()
    clock.tick(FPS)