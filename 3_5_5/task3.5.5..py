class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if type(a) in (int, float) and self.MIN_DIMENSION <= a <= self.MAX_DIMENSION:
            self.__a = a
        else:
            print("Size Error")
            return 0

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        if type(b) in (int, float) and self.MIN_DIMENSION <= b <= self.MAX_DIMENSION:
            self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        if type(c) in (int, float) and self.MIN_DIMENSION <= c <= self.MAX_DIMENSION:
            self.__c = c

    def volume(self):
        return self.a * self.b * self.c

    def __eq__(self, other):
        return self.volume() == other.volume()


d = Dimensions("d", 2, 2)
s = Dimensions(2, 2, 2)
f = Dimensions(1, 2, 2)
d.a = 1000000
print(d.a)
# print(s.c)
print(d == s)

