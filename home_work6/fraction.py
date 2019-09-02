def common_denominator(numerator, denominator):
    while numerator % denominator != 0:
        old_num = numerator
        old_den = denominator
        numerator = old_den
        denominator = old_num % old_den

    return denominator


class Fraction:

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return str(self.num) + " / " + str(self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common_den = common_denominator(new_num, new_den)
        return Fraction(new_num // common_den, new_den // common_den)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common_den = common_denominator(new_num, new_den)
        return Fraction(new_num // common_den, new_den // common_den)

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common_den = common_denominator(new_num, new_den)
        return Fraction(new_num // common_den, new_den // common_den)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common_den = common_denominator(new_num, new_den)
        return Fraction(new_num // common_den, new_den // common_den)


if __name__ == '__main__':
    f1 = Fraction(2, 3)
    f2 = Fraction(3, 8)
    print(f1 / f2)
