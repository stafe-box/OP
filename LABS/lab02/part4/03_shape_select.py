# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код

def n_angle(start_x, start_y, rotation, size, angles, color):
    start = sd.get_point(start_x, start_y)
    for i in range (rotation, rotation+360, (360//angles)):
        start = sd.vector(start, i, size, color=colors[color], width=3)


def color_choice():
    n=0
    while n not in range(1,7):
        n = int(input('Choose a color:\n   1-White\n   2-Black\n   3-Red\n   4-Blue\n   5-Green\n   6-Yellow\n>>>'))
    return n-1


def shape_choice():
    n=0
    while n not in range(1,5):
        n = int(input('Choose the shape:\n   1-Triangle\n   2-Sqare\n   3-Pentagon\n   4-Hexagon\n>>>'))
    return n+2
    

colors=[sd.COLOR_WHITE, 
sd.COLOR_BLACK, 
sd.COLOR_RED, 
sd.COLOR_BLUE, 
sd.COLOR_GREEN, 
sd.COLOR_YELLOW]


sd.resolution = (1200, 600)
color=color_choice()
shape=shape_choice()
start_x, start_y = 500, 200
n_angle(start_x, start_y, 0, 100, shape, color)

sd.pause()
