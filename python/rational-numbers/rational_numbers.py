from __future__ import division


class Rational:
    def __init__(self, num, den):  #  Num is short for numerator and den short for denominator
        if num == 0:
            num, den = 0, 1

        if den < 0:
            num, den = -num, -den

        for c in range(1, den + 1):
            if num % c == 0 and den % c == 0:
                self.num, self.den = num // c, den // c

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __repr__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, other):
        return Rational(self.num * other.den + other.num * self.den, self.den * other.den)

    def __sub__(self, other):
        return Rational(self.num * other.den - other.num * self.den, self.den * other.den)

    def __mul__(self, other):
        return Rational(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Rational(self.num * other.den, self.den * other.num)

    def __abs__(self):
        if self.num < 0:
            return Rational(-self.num, self.den)
        return Rational(self.num, self.den)

    def __pow__(self, power):
        if power > 0:
            return Rational(self.num ** power, self.den ** power)
        if power < 0:
            return Rational(self.den ** power, self.num ** power)
        return Rational(1, 1)

    def __rpow__(self, base):
        return base ** (self.num / self.den)
