from __future__ import division


class Rational:
    def __init__(self, numerator, denominator):
        if numerator == 0:
            numerator, denominator = 0, 1

        if denominator < 0:
            numerator, denominator = -numerator, -denominator

        for c in range(1, denominator + 1):
            if numerator % c == 0 and denominator % c == 0:
                self.numerator, self.denominator = numerator // c, denominator // c

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __abs__(self):
        if self.numerator < 0:
            return Rational(-self.numerator, self.denominator)
        return Rational(self.numerator, self.denominator)

    def __pow__(self, power):
        if power > 0:
            return Rational(self.numerator ** power, self.denominator ** power)
        if power < 0:
            return Rational(self.denominator ** power, self.numerator ** power)
        return Rational(1, 1)

    def __rpow__(self, base):
        return base ** (self.numerator / self.denominator)
