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
            self.real * other.real + self.imaginary * other.imaginary * -1,
            self.real * other.imaginary + self.imaginary * other.real
        )

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2),
            -1 * self.real * other.imaginary + self.imaginary * other.real
        )

    def __abs__(self):
        pass

    def conjugate(self):
        pass

    def exp(self):
        pass

print(ComplexNumber(1.0, 0.0) / ComplexNumber(2.0, 0.0))