import pygame
import random
import math

vec2, vec3 = pygame.math.Vector2, pygame.math.Vector3

RES = WIDTH, HEIGHT = 1600, 900 # Разрешение экрана
FPS = 30 # Скорость обновления экрана
NUM_STARS = 1500
CENTER = vec2(WIDTH // 2, HEIGHT // 2)
COLORS = 'red green blue skyblue orange purple cyan magenta'.split()
Z_DISTANCE = 140 
ALPHA = 30

class Star:
    def __init__(self, app):
        self.screen = app.screen      # Указываем поверхность отображения звезды
        self.pos3d = self.get_pos3d()   # Получаем 3Д-координаты
        self.vel = random.uniform(0.45, 0.95)   # Случайная скорость движения звезды (от .05 до .25)
        self.color = random.choice(COLORS)  # Случайный цвет из нашего списка
        self.screen_pos = vec2(0, 0)    # координаты на экране
        self.size = 10  # Начальный радиус звезды
    
    def get_pos3d(self, scale_pos=35):
        angle = random.uniform(0.0, 2.0 * math.pi)  # Случайный угол от 0 до 180
        radius = random.randrange(HEIGHT // 4, HEIGHT // 3) * scale_pos         # Случайный радиус, увеличенный на коэффициент разброса
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        return vec3(x, y, Z_DISTANCE)
    
    def update(self):
        self.pos3d.z -= self.vel
        self.pos3d = self.get_pos3d() if self.pos3d.z < 1 else self.pos3d
        self.screen_pos = vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z + CENTER
        self.size = ( Z_DISTANCE - self.pos3d.z) / (0.2 * self.pos3d.z)
        # rotate xy
        self.pos3d.xy = self.pos3d.xy.rotate(0.5)
        # mouse
        mouse_pos = CENTER - vec2(pygame.mouse.get_pos())
        self.screen_pos -= mouse_pos
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, (*self.screen_pos, self.size, self.size))  # Звезда ввиде квадрата
        # pygame.draw.circle(self.screen, self.color, *self.screen_pos, self.size)  # Звезда ввиде круга
        # pygame.draw.circle(
            #     surface: Surface, 
            #     color: _ColorValue, 
            #     center: _Coordinate, 
            #     radius: float, 
            #     width: int = 0, 
            #     draw_top_right: bool | None = None, 
            #     draw_top_left: bool | None = None, 
            #     draw_bottom_left: bool | None = None, 
            #     draw_bottom_right: bool | None = None)

class StarField:
    def __init__(self, app):
        self.stars = [Star(app) for i in range(NUM_STARS)] 

    def run(self):
        [star.update() for star in self.stars]
        self.stars.sort(key=lambda star: star.pos3d.z, reverse=True)
        [star.draw() for star in self.stars]


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)  # Создаем поверхность для отрисовки
        self.alpha_surface = pygame.Surface(RES)
        self.alpha_surface.set_alpha(ALPHA)
        self.clock = pygame.time.Clock()    # Создаем экземпляр Clock для установки FPS
        self.starfield = StarField(self)
    
    def run(self):
        while True:
#            self.screen.fill('black')   # На каждой итерации закрашиваем весь экран в черный цвет
            self.screen.blit(self.alpha_surface, (0, 0))
            self.starfield.run()
            
            pygame.display.flip()   # обновляем кадр (отображаем что нарисовали в текущей итерации)
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]   # Проверяем на закрытие приложения
            self.clock.tick(FPS) # Устанавливаем FPS

# Главный цикл программы
if __name__ == '__main__':
    app = App() # Создаем экземпляр класса App
    app.run()   # Вызываем метод run