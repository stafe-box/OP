#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import random
import simple_draw

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

def emoji(pos_x, pos_y):
    simple_draw.circle(simple_draw.Point(pos_x, pos_y), radius=50, color=simple_draw.COLOR_YELLOW, width=50)
    simple_draw.circle(simple_draw.Point(pos_x, pos_y), radius=50, color=simple_draw.COLOR_BLACK, width=5)
    simple_draw.circle(simple_draw.Point(pos_x+20, pos_y+15), radius=10, color=simple_draw.COLOR_WHITE, width=10)
    simple_draw.circle(simple_draw.Point(pos_x-20, pos_y+15), radius=10, color=simple_draw.COLOR_WHITE, width=10)
    simple_draw.circle(simple_draw.Point(pos_x+20, pos_y+15), radius=10, color=simple_draw.COLOR_BLACK, width=2)
    simple_draw.circle(simple_draw.Point(pos_x-20, pos_y+15), radius=10, color=simple_draw.COLOR_BLACK, width=2)
    simple_draw.circle(simple_draw.Point(pos_x+17, pos_y+13), radius=3, color=simple_draw.COLOR_BLACK, width=3)
    simple_draw.circle(simple_draw.Point(pos_x-23, pos_y+13), radius=3, color=simple_draw.COLOR_BLACK, width=3)
    simple_draw.circle(simple_draw.Point(pos_x-7, pos_y-20), radius=7, color=simple_draw.COLOR_RED, width=7)
    simple_draw.circle(simple_draw.Point(pos_x-7, pos_y-20), radius=7, color=simple_draw.COLOR_BLACK, width=2)

simple_draw.resolution = (1200, 600)

for i in range(9):
    x = random.randrange(50, 1150)
    y = random.randrange(50, 550)
    emoji(x, y)
    

simple_draw.pause()
