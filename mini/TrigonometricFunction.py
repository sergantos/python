import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
z = np.cos(x)

# Расставим значения по осям х и у
xnumbers = np.linspace(0, 7, 15)
ynumbers = np.linspace(-1, 1, 11)

plt.plot(x, y, color="r", label="sin")
plt.plot(x, y, color="g", label="cos")
plt.xlabel("Угол в радианах")
plt.ylabel("Функция")
plt.title("График тригономических функций")
plt.xticks(xnumbers)
plt.yticks(ynumbers)
plt.legend()
plt.grid()
plt.axis([0, 6.5, -1.1, 1.1])
plt.show()