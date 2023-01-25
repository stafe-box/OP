#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить список всех живущих на районе (пакет district) и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from pprint import pprint
from district.central_street.house1.room1 import folks as cent_h1_r1
from district.central_street.house1.room2 import folks as cent_h1_r2
from district.central_street.house2.room1 import folks as cent_h2_r1
from district.central_street.house2.room2 import folks as cent_h2_r2
from district.soviet_street.house1.room1 import folks as sov_h1_r1
from district.soviet_street.house1.room2 import folks as sov_h1_r2
from district.soviet_street.house2.room1 import folks as sov_h2_r1
from district.soviet_street.house2.room2 import folks as sov_h2_r2


people = [*cent_h1_r1, *cent_h1_r2, *cent_h2_r1, *cent_h2_r2,
          *sov_h1_r1, *sov_h1_r2, *sov_h2_r1, *sov_h2_r2]
n = 0
for _ in people:
    if not _:
        del people[n]
    n += 1
pprint("На районе живут: " + ', ' .join(map(str, people)))
