#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код

zoo.insert(1, 'bear')
print (zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код

zoo.extend(birds)
print (zoo)

# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код

zoo.remove('elephant')#за что слона-то?
print (zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код

def fs(someone):#fs == find someone == найти кого-то
    global zoo
    return (zoo.index(someone)+1)

print('Лев в клетке № ',
    fs('lion'),
    ', а жаворонок в клтке № ',
    fs('lark'),
    sep = '')
