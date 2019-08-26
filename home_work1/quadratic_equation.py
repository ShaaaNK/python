import math
from decimal import Decimal


def quadratic_equation():
    a = Decimal(input("A: "))
    b = Decimal(input("B: "))
    c = Decimal(input("C: "))

    d = Decimal((b * b - 4 * a * c))

    if a == 0:
        x = -c / b
        print(x)
    elif d > 0:
        x1 = Decimal((-b + Decimal(math.sqrt(d))) / (2 * a))
        x2 = Decimal((-b - Decimal(math.sqrt(d))) / (2 * a))
        print(x1, "\t", x2)
    elif d == 0:
        x = Decimal(-b / (2 * a))
        print(x)
    else:
        print("NO Solution")


if __name__ == '__main__':
    quadratic_equation()
