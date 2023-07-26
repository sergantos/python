import pygame
import random
import copy

MX = MY = 128 # РАзмер массива пламени 
S_FIRE = 2 # Размер ячейки пламени на экране 

SX = MX * S_FIRE
SY = MY * S_FIRE

scr=[]

line=[0]*MX # Созхдаем массив из нулей длиной МХ

# Создаем список списков из нулей длиной MY, в итоге получится квадратная таблица из нулей
x_y=[] 
for y in range(0,MY):
    x_y.append(copy.deepcopy(line))

# Создаем список из двух квадратных таблиц
scr=[]
for i in range(0,2):
    scr.append(copy.deepcopy(x_y))

iout=0 # Номер текущей активной страницы
pygame.init()
screen=pygame.display.set_mode((SX,SY)) # Задаем разрешение окна
running=True

pal=[] # Палитра для пламени

# Задаем плавный переход от черного к красному, а затем от красного к ярко-синему
for i in range(0,32):
    pal.append([i*8, 0, 0])
for i in range(63,31, -1):
    pal.append([255, 0 + (i-32)*8, 255 - (i-32)*8])

# -------------------------------------------------------------------------------------------------------
# Отрисовка закрашенного квадрата в нужных координатах, определенного размера.
# -------------------------------------------------------------------------------------------------------
def drawBox(x, y, size, color):
    pygame.draw.rect(screen, pal[color], (x, y, size, size))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    # Две нижние стоки в массиве заполняем случайными значениями или 0 или 63, это минимальный и максимальный цвета из палитры пламени
    for x in range(0, MX-1, 2):
        scr[iout][MY-1][x] = scr[iout][MY-2][x] = scr[iout][MY-1][x+1] = scr[iout][MY-2][x+1] = random.randint(0, 1) * 63
    
    # Проходим по всей нашей квадратной таблице, не трогая крайние точки по бокам.
    for x in range(1,MX-1):
        for y in range(MY-2,-1,-1):
            # Получаем среднее значение цвета точки и окружающих ее точек
            mid = round((scr[iout][y][x] + scr[iout][y][x-1] + scr[iout][y][x+1] + scr[iout][y+1][x]) / 4)
            if mid>1: # если цвет не нулевой, то уменьшаем его яркость
                mid -= 1
            
            scr[1-iout][y-1][x]=mid # записываем полученное значение обратно в массив, но в другую плоскость.
    iout = 1 -iout # меняем текущую плоскость на противоположную
    
    for y in range(0,MY-3):
        for x in range(0,MX):
            drawBox(x*S_FIRE, y*S_FIRE, S_FIRE, scr[iout][y][x])
    pygame.display.flip()
pygame.quit()