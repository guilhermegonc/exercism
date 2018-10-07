from __future__ import division


class Rational:
    def __init__(self, numerator, denominator):
        if numerator == 0:
            numerator, denominator = 0, 1

        if denominator < 0:
            numerator, denominator = -numerator, -denominator

        for c in range(1, denominator + 1):
            if numerator % c == 0 and denominator % c == 0:
                self.numer, self.denom = numerator // c, denominator // c

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        if self.numer < 0:
            return Rational(-self.numer, self.denom)
        return Rational(self.numer, self.denom)

    def __pow__(self, power):
        if power > 0:
            return Rational(self.numer ** power, self.denom ** power)
        if power < 0:
            return Rational(self.denom ** power, self.numer ** power)
        return Rational(1, 1)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)