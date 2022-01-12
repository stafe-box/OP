#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.

sd.resolution = (1200, 600)
#sd.line(sd.Point(50, 50), sd.Point(350, 450), color = sd.COLOR_BLACK, width = 4)

j = 0
for i in rainbow_colors:
    sd.line(sd.Point(50 + j, 50), sd.Point(350 + j, 450), color = i, width = 4)
    j += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

j = 0
for i in rainbow_colors:
    sd.circle(sd.Point(600, 0), radius = 100 + j, color = i, width = 4)
    j += 5

sd.pause()
