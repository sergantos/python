import time
import pygame
from random import choice
import os

''' Алгоритм формирования лабиринта методом Recursive Backtracker (поиск в глубину)'''

RES = WIDTH, HEIGHT = 1202, 962
TILE = 48
cols, rows = WIDTH // TILE, HEIGHT // TILE

pygame.init()

sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

class Cell:
    def __init__(self, x, y): # Первоначальные значения ячейки
        self.x, self.y = x, y
        self.walls = {'top': True, 'bottom': True, 'left': True, 'right': True}
        self.visited = False
    
    def draw(self): # Отрисовка ячейки вместе с ее стенами
        x, y = self.x * TILE, self.y * TILE
        if self.visited:
            pygame.draw.rect(sc, (0,0,0), (x, y, TILE, TILE))
        if self.walls['top']:
            pygame.draw.line(sc, (255,0,0), (x, y), (x + TILE, y), 2)
        if self.walls['right']:
            pygame.draw.line(sc, (255,0,0), (x + TILE, y), (x + TILE, y + TILE), 2)
        if self.walls['bottom']:
            pygame.draw.line(sc, (255,0,0), (x + TILE, y + TILE), (x, y + TILE), 2)
        if self.walls['left']:
            pygame.draw.line(sc, (255,0,0), (x,y + TILE), (x, y), 2)
    
    def draw_current_cell(self): # Выбранную ячейку закрасим зелененьким
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(sc, (0,255,0), (x + 3, y + 3, TILE - 5, TILE - 5))

    def check_cell(self, x, y): # Проверка - не вышла ли выбранная ячейка за границы поля
        find_index = lambda x, y: x + y * cols
        if x < 0 or x> cols - 1 or y < 0 or y > rows - 1:
            return False # Ячейка вышла - возвращаем False
        return grid_cells[find_index(x, y)] # Ячейка в допустимой области - возвращаем ячейку по одномерному индексу

    def check_neighbors(self): # Возвращает случайную ячейку из соседей выбранной ячейки
        neighbors = []
        # Проверим на наличие соседей по кругу выбранной ячейки
        top = self.check_cell(self.x, self.y - 1) 
        bottom = self.check_cell(self.x, self.y + 1)
        right = self.check_cell(self.x + 1, self.y)
        left = self.check_cell(self.x - 1, self.y)
        # Если сосед не вышел за пределы поля и непосещен - добавим его в наш массив
        if top and not top.visited:
            neighbors.append(top)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if right and not right.visited:
            neighbors.append(right)    
        if left and not left.visited:
            neighbors.append(left)
        # Возвращаем случайную ячейку из нашего списка а если массив пустой возвращаем False
        return choice(neighbors) if neighbors else False 

def remove_walls(current, next): # Сносим стены между текущей и следующей ячейкой
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False

grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)] # Формируем список всех ячеек
current_cell = grid_cells[0] # Начальная ячейка 0
stack = [] # Стэк пуст

while True:
    sc.fill(pygame.Color('darkslategray'))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    [cell.draw() for cell in grid_cells] # Отрисуем все ячейки
    current_cell.visited = True
    current_cell.draw_current_cell()
    
    next_cell = current_cell.check_neighbors() # Получим следующую случайную ячейку
    if next_cell:
        next_cell.visited = True
        stack.append(current_cell)
        remove_walls(current_cell, next_cell)
        current_cell = next_cell
    elif stack:
        current_cell = stack.pop()
        
    pygame.display.flip()
    clock.tick(60)
    
    if current_cell == grid_cells[0]:
        print('Конец формирования лабиринта')
        time.sleep(5)
        exit()