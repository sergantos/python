import pygame
import math


# Значение экрана
ScreenX=800
ScreenY=600
pygame.init()
screen = pygame.display.set_mode((ScreenX, ScreenY))
running = True
polScreenX = ScreenX // 2 # Середина экрана
polScreenY = ScreenY // 2 # Середина экрана

countPoints=500 # Кол-во точек в елочке
radius=100 # Радиус точки
fis=0 # угол поворота елочки
PI=3.14 # Число Пи
a_x = 0.5 # Коэфициент по Х
a_y = 0.25 # Коэфициент по У
isk : float = 1 # искажение
delta_isk : float = 0.1

# Заполняем массив точек первоначальными данными
yraz = ScreenY-30 # Размер елочки
points=[]
for ind in range(0, countPoints):
    pass

# Процедура отрисовывает точку по координате Y и углу fi
def tree(xpos, ypos):
    global isk, delta_isk
    for z in range(0,360):
        x_disp = xpos + radius * math.cos(z) # Координата Х вывода точки
        y_disp = ypos - radius * math.sin(z) / isk # Координата У вывода точки
        pygame.draw.circle(screen, (255, 255, 255), (x_disp, y_disp), 2)
    isk = isk + delta_isk
    if isk >1.5 or isk <0:
        delta_isk = -delta_isk
                
#        print(x_disp, " ", y_disp)

# Главный цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0)) # Очистили экран
    tree(polScreenX, polScreenY)
       
    pygame.display.flip()
pygame.quit()
