# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Water:
    def __str__(self):
        return ' воды '

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Steam(self, other)
        elif isinstance(other, Earth):
            return Dirt(self, other)
        elif isinstance(other, Solod):
            return Pivko(self, other)


class Air:
    def __str__(self):
        return ' воздуха '

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Lightning(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dust(part1=self, part2=other)


class Fire:
    def __str__(self):
        return ' огоня '

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam(part1=self, part2=other)
        elif isinstance(other, str):
            return other + ' ' + str(self)
        elif isinstance(other, Air):
            return Lightning(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Lava(part1=self, part2=other)


class Earth:
    def __str__(self):
        return ' земли '

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt(part1=self, part2=other)
        elif isinstance(other, Air):
            return Dust(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Lava(part1=self, part2=other)


class Solod:
    def __str__(self):
        return ' солода '

    def __add__(self, other):
        if isinstance(other, Water):
            return Pivko(part1=self, part2=other)


class Storm:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Шторм состоит из' + str(self.part1) + 'и' + str(self.part2)


class Steam:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пар состоит из' + str(self.part1) + 'и' + str(self.part2)


class Dirt:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Грязь состоит из' + str(self.part1) + 'и' + str(self.part2)


class Lightning:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Молния состоит из' + str(self.part1) + 'и' + str(self.part2)


class Dust:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пыль состоит из' + str(self.part1) + 'и' + str(self.part2)


class Lava:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Лава состоит из' + str(self.part1) + 'и' + str(self.part2)


class Pivko:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пивко состоит из' + str(self.part1) + 'и' + str(self.part2)


print(Earth() + Fire())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
print(Solod() + Water())
