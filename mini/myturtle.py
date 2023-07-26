import turtle
ninja = turtle.Turtle() # Рисует стрелочка
ninja.color('red','green')  # Рисуем RED, черепашка GREEN
ninja.speed(10) # Скорость анимации
for i in range(180):
    ninja.forward(100)  # Движение вперед
    ninja.right(30)     # Поворот вправо
    ninja.backward(5)   # Движение назад
    ninja.right(30)
    ninja.forward(20)   
    ninja.left(60)      # Поворот влево
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()       # Не рисовать во время движения
    ninja.setposition(0,0)  # Устанавоиваем в новую позицию
    ninja.pendown()     # Рисовать во время движения
    
    ninja.right(1)

turtle.exitonclick()    # выйти при клике на канвасе
# turtle.clear()          # очищает холст от нарисованного
turtle.done()       # Конец