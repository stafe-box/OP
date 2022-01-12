#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

black = simple_draw.COLOR_BLACK
purple = simple_draw.COLOR_PURPLE
blue = simple_draw.COLOR_BLUE
cyan = simple_draw.COLOR_CYAN
dblue = simple_draw.COLOR_DARK_BLUE
dcyan = simple_draw.COLOR_DARK_CYAN
yellow = simple_draw.COLOR_YELLOW

def print_brick_line(start_x, start_y, wall_length, step_x, step_y, colored):
    for x in range(start_x, wall_length, step_x):
        point1 = simple_draw.get_point(x, start_y)
        point2 = simple_draw.get_point(x + step_x, start_y + step_y)
        simple_draw.rectangle(left_bottom=point1, right_top=point2, color=colored, width=2)

step_x = 100
step_y = 50
wall_length = 1200
simple_draw.resolution = (wall_length, 600)

k=0
for y in range(1, wall_length, step_y):
    k= k+1
    # Четное
    if k % 2 == 0:
        print_brick_line(start_x=(step_x-step_x), start_y=y, wall_length=wall_length, step_x=step_x, step_y=step_y, colored=yellow)
    # Нечётное
    else:
        print_brick_line(start_x=((step_x//2)-step_x), start_y=y, wall_length=wall_length, step_x=step_x, step_y=step_y, colored=yellow)



# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

simple_draw.pause()
