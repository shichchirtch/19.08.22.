class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        if isinstance(a, (int, float)) and self.MIN_DIMENSION <= a <= self.MAX_DIMENSION:
            self.__a = a
        if isinstance(b, (int, float)) and self.MIN_DIMENSION <= b <= self.MAX_DIMENSION:
            self.__b = b
        if isinstance(c, (int, float)) and self.MIN_DIMENSION <= c <= self.MAX_DIMENSION:
            self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        #print("setter_a")
        if type(a) in (int, float) and self.MIN_DIMENSION <= a <= self.MAX_DIMENSION:
            self.__a = a
        else:
            #print("Size Error")
            raise TypeError

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        if type(b) in (int, float) and self.MIN_DIMENSION <= b <= self.MAX_DIMENSION:
            self.__b = b
        else:
            #print("Size Error")
            raise TypeError

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        if type(c) in (int, float) and self.MIN_DIMENSION <= c <= self.MAX_DIMENSION:
            self.__c = c
        else:
            #print("Size Error")
            raise TypeError

    def volume(self):
        return self.a * self.b * self.c

    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, Dimensions):
            raise TypeError("Операнд справа должен иметь тип Dimentions")
        return other

    def __eq__(self, other):
        sc = self.verify_data(other)
        return self.volume() == sc.volume()

    def __lt__(self, other):
        sc = self.verify_data(other)
        return self.volume() < sc.volume()

    def __gt__(self, other):
        sc = self.verify_data(other)
        return self.volume() > sc.volume()

    def __le__(self, other):
        sc = self.verify_data(other)
        return self.volume() <= sc.volume()

    def __ge__(self, other):
        sc = self.verify_data(other)
        return self.volume() >= sc.volume()

class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        if isinstance(price, (int, float)):
            self.price = price
        if isinstance(dim, Dimensions):
            self.dim = dim
    def __str__(self):
        return f'{self.name} '



trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
#print(trainers)
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume())
#print(*lst_shop_sorted)


