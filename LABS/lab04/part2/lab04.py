
### Для решения интерактивных вопросов - смотрите car.py

def naturals():
    """Генератор для получения бесконечной последовательности натуральных чисел

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Получает элементы итерируемого объекта it, увеличенные в multiplier раз.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for i in it:
        yield i * multiplier

def hailstone(n):
    """
    Сиракузская последовательность. Если число n чётное - следующим будет половина n, если нечётное - то следующее: 3n + 1.
    Последовательность заканчивается на 1.
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    if n == 1:
        pass
    elif n % 2 == 1:
        n = n * 3 + 1
        yield from hailstone(n)
    else:
        n = n // 2
        yield from hailstone(n)


# Следующая задача - карточная игра Magic the Lambda-ing! (см. classes.py)
# Для класса Card нужно реализовать конструктор и метод power.
# Для класса Player - конструктор и методы draw и play.
# При реализации метода draw и конструктора используйте метод draw класса Deck.
# Запустить игру можно так: python3 cardgame.py

### Необязательно задание
# Реализовать методы effect для классов TutorCard, TACard, PrefessorCard -
# это сделает игру гораздо интереснее
