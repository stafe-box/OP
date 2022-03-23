# -*- coding: utf-8 -*-
#from curses import COLORS
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр 01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см /results/exercise_02_global_color.jpg

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
    

colors=[sd.COLOR_WHITE, 
sd.COLOR_BLACK, 
sd.COLOR_RED, 
sd.COLOR_BLUE, 
sd.COLOR_GREEN, 
sd.COLOR_YELLOW]


sd.resolution = (1200, 600)
n=color_choice()
start_x, start_y = 100, 200
for i in range(3, 7, 1):
    n_angle(start_x, start_y, 0, 100, i, n)
    start_x+=200

sd.pause()
