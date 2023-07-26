import pygame

MX = 800
MY = 600
mid_mx = MX // 2 # Середина экрана
mid_my = MY // 2 # Середина экрана

pygame.init()
screen = pygame.display.set_mode((MX, MY))

running = True
treug=[[1,2,3],[100,50,1],[150,200,1]] # Наш треугольник
clock = pygame.time.Clock()

def conv3d(argument):
# Функция конвертирует 3d координаты x,y,z в плоскостные displ_x, displ_y
    x=argument[0]
    y=argument[1]
    z=argument[2]
    if z!=0:
        displ_x = round(x * 300 / z) + mid_mx
        displ_y = round(y * 300 / z) + mid_my
    else:
        displ_x = round(x * 300 ) + mid_mx
        displ_y = round(y * 300 ) + mid_my
    return (displ_x, displ_y)
    
def drawfig():
# Функция рисует нашу фигуру на поверхности
    pygame.draw.circle(screen, [255,0,0], conv3d(treug[0]), 2)
    pygame.draw.circle(screen, [0,255,0], conv3d(treug[1]), 2)
    pygame.draw.circle(screen, [0,0,255], conv3d(treug[2]), 2)
    pygame.draw.line(screen, (255,0,0), conv3d(treug[0]), conv3d(treug[1]))
    pygame.draw.line(screen, (0,255,0), conv3d(treug[1]), conv3d(treug[2]))
    pygame.draw.line(screen, (0,0,255), conv3d(treug[2]), conv3d(treug[0]))
    

# Main
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Main cicle

    # print(treug[0][2])
    
    for d_cor in range(1, 300):
        screen.fill((0, 0, 0)) # Очистили экран
        # treug[0][0]=d_cor
        treug[0][2]=d_cor
        # treug[0][2]=d_cor
        drawfig()
        pygame.display.update()
    # clock.tick(60)
pygame.quit()
