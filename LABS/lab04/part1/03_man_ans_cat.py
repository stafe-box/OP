# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код
from termcolor import cprint
 
 
class Man:
 
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
 
    def __str__(self):
        return '{}: сытость {}'.format(
            self.name, self.fullness)
 
    def eat(self):
        if self.house.food >= 10:
            cprint('{}: поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{}: нет еды'.format(self.name))
 
    def work(self):
        cprint('{}: сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10
 
    def watch_mtv(self):
        cprint('{}: прогал на питоне весь день'.format(self.name))
        self.fullness -= 10
 
    def shopping(self):
        if self.house.money >= 50:
            cprint('{}: сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{}: деньги кончились!'.format(self.name))
 
    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{}: Вьехал в дом'.format(self.name))
 
    def pick_up_a_cat(self, cat):
        cat.house = self.house
        cprint(f'{self.name}: подобрал {cat.name}')
 
    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint(f'{self.name}: сходил за едой коту')
            self.house.cat_food += 50
            self.house.money -= 50
        else:
            cprint(f'{self.name}: деньги кончились!')
 
    def cleaning(self):
        if self.house.mud >= 100:
            cprint(f'{self.name}: убрался в доме')
            self.house.mud -= 100
            self.fullness -= 20
        else:
            cprint(f'{self.name}! В квартире очень грязно!')
 
    def act(self):
        if self.fullness <= 0:
            cprint('{}: R.I.P...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.house.money < 50:
            self.work()
        elif self.fullness <= 20:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.cat_food <= 20:
            self.buy_cat_food()
        elif self.house.mud >= 100:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.buy_cat_food()
        else:
            self.watch_mtv()
 
 
class Cat:
 
    def __init__(self, name):
        self.name = name
        self.cat_fullness = 50
        self.house = None
 
    def __str__(self):
        return f'{self.name}: сытость {self.cat_fullness}'
 
    def cat_sleep(self):
        self.cat_fullness -= 10
        cprint(f'{self.name}: спал весь день')
 
    def go_to_the_house(self, house):
        self.house = house
        self.cat_fullness -= 10
        cprint(f'{self.name}: въехал в дом')
 
    def eat(self):
        if self.house.cat_food >= 0:
            self.cat_fullness += 20
            self.house.cat_food -= 10
            cprint(f'{self.name}: поел')
        else:
            cprint(f'У котиков нет еды')
 
    def destroy_wallpaper(self):
        self.cat_fullness -= 10
        self.house.mud += 5
        cprint(f'{self.name}: драл обои')
 
    def act(self):
        if self.cat_fullness <= 0:
            cprint(f'{self.name}: R.I.P...')
            return
        dice_cat = randint(1, 6)
        if self.cat_fullness < 20:
            self.eat()
        elif dice_cat == 1:
            self.destroy_wallpaper()
        elif dice_cat == 2:
            self.eat()
        else:
            self.cat_sleep()
 
 
class House:
 
    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.mud = 0
 
    def __str__(self):
        return f'В доме:\nеды - {self.food}\nденег - {self.money}\nкошачей еды - {self.cat_food}\nзагрязненность - {self.mud}'
 
 
citizens = [
    Man(name='Програмистик'),
            ]
 
cats = [
    Cat(name='Сишка'),
    Cat(name='Питончик'),
        ]
 
 
for citizens_cats in cats:
    citizens[0].pick_up_a_cat(cat=citizens_cats)
    citizens.append(citizens_cats)
 
my_sweet_home = House()
 
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
 
for day in range(1, 30):
    print('_____________________ день {} _____________________'.format(day))
    for citisen in citizens:
        citisen.act()
    print('_____________________ в конце дня _____________________')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
