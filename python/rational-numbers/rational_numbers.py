from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        gcd = 1
        if numer == 0:
            self.numer = numer
            self.denom = 1
        else:
            for c in range(1, abs(numer) + 1):
                if numer % c == 0 and denom % c == 0:
                    gcd = c
            numer = numer // gcd
            denom = denom // gcd
            if (numer > 0 and denom < 0) or (numer < 0 and denom < 0):
                numer = -numer
            if denom < 0:
                denom = -denom
            self.numer = numer
            self.denom = denom

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
        numer = self.numer
        denom = self.denom
        if numer < 0:
            numer = -self.numer
        if denom < 0:
            denom = -self.denom
        return Rational(numer, denom)

    def __pow__(self, power):
        if power == 0:
            return Rational(1, 1)
        elif power > 0:
            return Rational(self.numer ** power, self.denom ** power)
        elif power < 0:
            return Rational(self.denom ** power, self.numer ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
