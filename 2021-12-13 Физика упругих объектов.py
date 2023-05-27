# ПОдключим библиотеки
import pygame as pg
import pymunk.pygame_util
from random import randrange

# Откалибруем системы координат обоих библиотек
pymunk.pygame_util.positive_y_is_up = False

# Первоначальные настройки графического модуля PyGame
RES = WIDTH, HEIGHT = 900, 720
FPS = 60
pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_option = pymunk.pygame_util.DrawOptions(surface)

# Переменные модуля физического моделирования PyMunk
space = pymunk.Space()
space.gravity = 0, 8000

# Создадим статичную платформу
segment_shape = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH, HEIGHT), 26)
space.add(segment_shape)
segment_shape.elasticity = 0.4 # 0.4
segment_shape.friction = 1.0

# Функция создания квадратиков в модуле PyMunk
def create_square(space, pos):
    square_mass, square_size = 1, (20, 20)
    square_moment = pymunk.moment_for_box(square_mass, square_size)
    square_body = pymunk.Body(square_mass, square_moment)
    # Считаем координаты курсора мыши - там и создадим квадратик
    square_body.position = pos
    square_shape = pymunk.Poly.create_box(square_body, square_size)
    square_shape.elasticity = 0 # 0.8
    square_shape.friction = 1.0
    # Цвет квадратика - случайный
    square_shape.color = [randrange(256) for i in range(4)]
    space.add(square_body, square_shape)

# Цикл постоянной отрисовки экрана
while True:
    surface.fill(pg.Color('white'))
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        # Спавн квадратиков
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                create_square(space, i.pos)
                print(i.pos)
    space.step(1 / FPS)
    space.debug_draw(draw_option)
    
    pg.display.flip()
    clock.tick(FPS)
