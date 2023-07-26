import random

# константы для направления движения
N, S, E, W = 1, 2, 4, 8
DX = { E: 1, W: -1, N: 0, S: 0 }
DY = { E: 0, W: 0, N: -1, S: 1 }
OPPOSITE = { E: W, W: E, N: S, S: N }

def generate_maze(width=16, height=8):
    # создаем пустую сетку клеток
    grid = [[0 for x in range(width)] for y in range(height)]
    
    # выбираем случайную стартовую клетку
    start_x = random.randint(0, width-1)
    start_y = random.randint(0, height-1)
    
    # помечаем ее как посещенную
    grid[start_y][start_x] |= S
    
    # создаем список стен, которые нужно проверить
    walls = [ (start_x, start_y, d) for d in (N, S, E, W) ]
    
    while walls:
        wall = walls.pop(random.randint(0, len(walls)-1))
        x, y, direction = wall
        
        # получаем координаты соседней клетки в направлении direction
        dx, dy = DX[direction], DY[direction]
        nx, ny = x + dx, y + dy
        
        # если соседняя клетка еще не посещена
        if nx >= 0 and nx < width and ny >= 0 and ny < height and grid[ny][nx] == 0:
            # отмечаем стену между текущей и соседней клетками как проход
            grid[y][x] |= direction
            grid[ny][nx] |= OPPOSITE[direction]
            
            # помечаем соседнюю клетку как посещенную и добавляем ее стены в список
            grid[ny][nx] |= S
            walls += [ (nx, ny, d) for d in (N, S, E, W) ]
    
    return grid

def draw_maze(grid):
    # символы для стен и проходов в лабиринте
    WALL = '█'
    PATH = ' '
    
    # отрисовываем верхнюю границу лабиринта
    print(WALL * (len(grid[0]) * 2 + 1))
    
    for y in range(len(grid)):
        # отрисовываем стену слева
        line = WALL
        for x in range(len(grid[0])):
            line += PATH if grid[y][x] & S != 0 else WALL
            line += PATH if grid[y][x] & E != 0 else WALL
        
        # отрисовываем правую стену и переходим на следующую строку
        print(line + WALL)
        
        # отрисовываем нижнюю стену после последней строки
        if y == len(grid)-1:
            print(WALL * (len(grid[0]) * 2 + 1))

grid = generate_maze(20, 20)
draw_maze(grid)