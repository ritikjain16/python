# (a+bi)+(c+di)=(a+c) + (b+d)i
# (a+bi)(c+di)=(ac-bd) + (ad+bc)i


class Complex:
    def __init__(self, r, i):
        self.real = r
        self.img = i

    def __add__(self, c):
        return Complex(self.real+c.real, self.img+c.img)    # (a+c) + (b+d)i

    def __mul__(self, c):
        mulReal = (self.real * c.real - self.img * c.img)     # (ac-bd)
        mulImg = (self.real * c.img + self.img * c.real)      # (ad+bc)i
        return Complex(mulReal, mulImg)

    def __str__(self):
        if self.img < 0:
            return f"{self.real} - {-self.img}i"
        else:
            return f"{self.real} + {self.img}i"


c1 = Complex(1, -4)
c2 = Complex(331, -37)
print(c1+c2)
print(c1*c2)
