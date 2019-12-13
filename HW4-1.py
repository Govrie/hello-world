#!/usr/bin/env python3 -tt
"""File: hello.py """

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        if self.imag == 0:
            return '{}'.format(self.real)
        if self.real == 0:
            return '{}i'.format(self.imag)
        if self.imag < 0:
            return '{}{}i'.format(self.real, self.imag)
        else:
            return '{}+{}i'.format(self.real, self.imag)

    def __add__(self, right_complex_number):  # +
        real = self.real + right_complex_number.real
        imag = self.imag + right_complex_number.imag
        return ComplexNumber(real, imag)

    def __sub__(self, right_complex_number):  # -
        real = self.real - right_complex_number.real
        imag = self.imag - right_complex_number.imag
        return ComplexNumber(real, imag)

    def __mul__(self, right_complex_number):  # *
        real = self.real * right_complex_number.real - self.imag * right_complex_number.imag
        imag = self.imag * right_complex_number.real + self.real * right_complex_number.imag
        return ComplexNumber(real, imag)

if __name__ == '__main__':
    x = ComplexNumber(3, 4)
    y = ComplexNumber(5, -1)
    print(x+y)
    print(x-y)
    print(x*y)
