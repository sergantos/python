import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Указываем координаты вершин куба
vertices = [(0, 0, 0), (0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1), (1, 1, 0)]

# Указываем, каким образом соединены вершины
faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 7, 3), (1, 5, 6, 2), (0, 1, 5, 4), (3, 2, 6, 7)]

# Создаем объект Poly3DCollection и добавляем его на график
cube = Poly3DCollection([vertices[face] for face in faces], alpha=.25, facecolor='blue', linewidth=1)
ax.add_collection(cube)

# Устанавливаем метки для каждого измерения
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()