#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pygame import color
import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
r = 100
for r in range(100, 85, -5):
    sd.circle(sd.Point(110,500,), radius=r, color = sd.COLOR_DARK_PURPLE, width = 1)
# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код

black = sd.COLOR_BLACK
purple = sd.COLOR_PURPLE
blue = sd.COLOR_BLUE
cyan = sd.COLOR_CYAN
dblue = sd.COLOR_DARK_BLUE
dcyan = sd.COLOR_DARK_CYAN

color_list = [black, blue, purple, cyan, dblue, dcyan]

def bubble (x, y, rad, col, wid, dist):
        for rad in range(rad, (rad-dist*3), -dist):
            sd.circle(sd.Point(x,y,), radius=rad, color = col, width = wid)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for x in range(50, 1000, 100):
    bubble(x, 50, 50, black, 1, 10)
# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
for x in range(20, 20+40*9, 40):
    for y in range(120,120+40*2, 40):
        bubble(x, y, 20, purple, 1, 2)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
import random
for i in range(1, 100):
    x = random.randrange(0,1200)
    y = random.randrange(0, 600)
    rad = random.randrange(5, 100)
    col = random.choice(color_list)
    wid = random.randrange(1,3)
    dist = random.randrange(3,10)
    bubble (x, y, rad, col, wid, dist)
sd.pause()
