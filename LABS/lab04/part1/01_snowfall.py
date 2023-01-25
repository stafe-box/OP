from random import randint

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, 600)
        self.y = sd.random_number(450, 570)
        self.length = 20

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.COLOR_WHITE)

    def move(self):
        self.y -= 20
        self.x += sd.random_number(-10, 10)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def can_fall(self):
        return self.y > 20


flake = Snowflake()


def get_flakes(count):
    lists_snowflake = []
    for _ in range(count):
        lists_snowflake.append(Snowflake())
    return lists_snowflake


def get_fallen_flakes():
    numbers = 0
    for _ in flakes:
        if not flake.can_fall():
            numbers += 1
    return numbers


def append_flakes(count):
    for _ in range(count):
        flakes.append(Snowflake())

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=3)
k = 1 
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()
    if fallen_flakes != 0:
        print(fallen_flakes)
    if fallen_flakes:
        k += 1
        append_flakes(count= k)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()