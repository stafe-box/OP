#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

#(((sites [i][0]) - (sites [j][0])) ** 2 + ((sites [i][1]) - (sites [j][1])) ** 2) ** 0.5

distances = {}


# TODO здесь заполнение словаря

for i in sites:
    for j in sites:
        if (i != j):
            if (j+' - '+i) not in distances:
                    distances[i+' - '+j] = {((((sites [i][0]) - (sites [j][0])) ** 2 + ((sites [i][1]) - (sites [j][1])) ** 2) ** 0.5)}

print(distances)
