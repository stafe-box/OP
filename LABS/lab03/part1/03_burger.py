#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера
# с помощью фукций из my_burger и вывести на консоль.

import my_burger
recipe = [my_burger.bun(), my_burger.cutlet(), my_burger.cheese(), my_burger.cutlet(
), my_burger.cheese(), my_burger.cucumbers(), my_burger.ketchup(), my_burger.mustard(), my_burger.bun()]
print("Рецепт двойного чизбургера: ", recipe)
print("Кушай на здоровье дорогой!!!")

# Создать рецепт своего бургера, по вашему вкусу.
BigMac = [my_burger.doublecg(), my_burger.special(), my_burger.cheese(),
          my_burger.cucumbers(), my_burger.salad(), my_burger.luk(), my_burger.bun(), my_burger.fin()]
print("Специальный рецепт: ", BigMac)
# Если не хватает ингридиентов - создать соответствующие функции в модуле my_burger
