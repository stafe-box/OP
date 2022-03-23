# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см results/exercise_01_shapes.jpg

# TODO здесь ваш код

def triangle(start_x, start_y, rotation, size):
    start = sd.get_point(start_x, start_y)
    for i in range (rotation, rotation+360, 120):
        start = sd.vector(start, i, size, color=sd.COLOR_DARK_YELLOW, width=3)


def sqare(start_x, start_y, rotation, size):
    start = sd.get_point(start_x, start_y)
    for i in range (rotation, rotation+360, 90):
        start = sd.vector(start, i, size, color=sd.COLOR_DARK_YELLOW, width=3)


def pentagon(start_x, start_y, rotation, size):
    start = sd.get_point(start_x, start_y)
    for i in range (rotation, rotation+360, 72):
        start = sd.vector(start, i, size, color=sd.COLOR_DARK_YELLOW, width=3)


def hexagon(start_x, start_y, rotation, size):
    start = sd.get_point(start_x, start_y)
    for i in range (rotation, rotation+360, 60):
        start = sd.vector(start, i, size, color=sd.COLOR_DARK_YELLOW, width=3)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)
def n_angle(start_x, start_y, rotation, size, angles):
    start = sd.get_point(start_x, start_y)
    for i in range (rotation, rotation+360, (360//angles)):
        start = sd.vector(start, i, size, color=sd.COLOR_DARK_YELLOW, width=3)


def triangle_simple(start_x, start_y, rotation, size):
    n_angle(start_x, start_y, rotation, size, 3)


def sqare_simple(start_x, start_y, rotation, size):
    n_angle(start_x, start_y, rotation, size, 4)


def pentagon_simple(start_x, start_y, rotation, size):
    n_angle(start_x, start_y, rotation, size, 5)


def hexagon_simple(start_x, start_y, rotation, size):
    n_angle(start_x, start_y, rotation, size, 6)


# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

sd.resolution = (1200, 600)

triangle_simple(10, 10, 0, 100)
sqare_simple(150, 10, 0, 100)
pentagon_simple(300, 10, 0, 100)
hexagon_simple(550, 10, 0, 100)

sd.pause()
