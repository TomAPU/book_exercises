class Fraction:
    def __init__(self, numerator, denominator):
        assert denominator>0, "denominator must be greater than 0"
        self._numerator = numerator
        self._denominator = denominator

    def __str__(self):
        return "%d/%d" % (self._numerator, self._denominator)

    def __add__(self, other):
        if self._denominator == other._denominator:
            n = self._numerator + other._numerator
            d = self._denominator
        else:
            d = self._denominator * other._denominator
            n = self._numerator*other._denominator + self._denominator*other._numerator
        return Fraction(n, d)

    def __sub__(self, other):
        if self._denominator == other._denominator:
            n = self._numerator - other._numerator
            d = self._denominator
        else:
            d = self._denominator * other._denominator
            n = self._numerator*other._denominator - self._denominator*other._numerator
        return Fraction(n, d)

    def __mul__(self, other):
        n = self._numerator * other._numerator
        d = self._denominator * other._denominator

        return Fraction(n, d)

    def __div__(self, other):
        assert other._numerator != 0, "zero div"
        n = self._numerator * other._denominator
        d = self._denominator * other._numerator

        if d < 0:
            d = -d
            n= -n

        return Fraction(n, d)

    # The division operator (/) is implemented by these methods. The __truediv__() method is used when __future__.division is in effect, otherwise __div__() is used. If only one of these two methods is defined, the object will not support division in the alternate context; TypeError will be raised instead.
    def __truediv__(self, other):
        return self.__div__(other)

if __name__ == '__main__':
    f1 = Fraction(1, 3)
    f2 = Fraction(-1, 4)
    f3 = f1 + f2
    print(str(f1))
    print(str(f2))
    print('+',str(f1+f2))
    print('-',str(f1-f2))
    print('*',str(f1*f2))
    print('/',str(f1/f2))

