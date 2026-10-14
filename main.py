import turtle
import math
import random

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
# ОТКЛЮЧАЕМ АНИМАЦИЮ ШАГОВ (это делает работу мгновенной)
screen.tracer(0)

# Настройка черепашки
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

# Список цветов для анимации
colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"]

# Основной цикл рисования
for i in range(120):
    t.penup()
    t.goto(0, 40)
    
    # Вычисление координат сердца
    angle = i * (math.pi * 2) / 120
    x = 16 * (math.sin(angle) ** 3) * 15
    y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 15
    
    # Выбор случайного цвета
    c = random.choice(colors)
    t.color(c)
    t.pendown()
    t.goto(x, y)
    
    # Рисование маленькой звездочки в точке (x, y)
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

# ОБНОВЛЯЕМ ЭКРАН (показываем сразу весь готовый рисунок)
screen.update()

# Оставить окно открытым по завершении
turtle.done()
