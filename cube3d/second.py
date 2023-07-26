import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

''' Этот код создает простую поверхность, состоящую из одного полигона, и добавляет его на 3D-график. Полигон окрашен в зеленый цвет с прозрачностью 0.25. '''

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Создание массива точек для отображения поверхности
x = np.array([0, 1, 1, 0])
y = np.array([0, 0, 1, 1])
z = np.array([0, 1, 0, 1])

# Создание набора полигонов
verts = [list(zip(x, y, z))]
poly = Poly3DCollection(verts, alpha=0.25)
poly.set_facecolor('g')

# Добавление полигонов на график
ax.add_collection3d(poly)

plt.show()

