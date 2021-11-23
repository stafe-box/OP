import math
from decimal import Decimal

def sphere(r):
    r = Decimal(r)
    pi = Decimal(22/7)
    v = Decimal(4/3) * pi * pow(r, 3)
    return v

def lenght(n):
    n = int(n)
    n = str(n)
    return len(n)

def is_pythagorean(x, y, z):
    return z**2 == x**2 + y**2

r = input('input radius >>> ')
print ("V = ", sphere(r), '\n')

n = input('input number >>> ')
print ("number lenght = ", lenght(n), '\n')

x = int(input('input lengh x >>> '))
y = int(input('input lengh y >>> '))
z = int(input('input lengh z >>> '))

print(is_pythagorean(x, y, z), '\n')
