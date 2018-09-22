import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return f'{self.real} + {self.imaginary}i'

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real + self.imaginary * - other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real
        )

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imaginary ** 2
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) / denom,
            (- self.real * other.imaginary + self.imaginary * other.real) / denom
        )

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, - self.imaginary)

    def exp(self):
        return ComplexNumber(
            math.e ** self.real * math.cos(self.imaginary),
            math.sin(self.imaginary)
        )
