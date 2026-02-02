class Demo:
    a = 25   # public variable
    _b = 15     # protected variable
    __c = 18    # private variable

    def show(self):
        print(f"a: {self.a}")
        print(f"b: {self._b}")
        print(f"c: {self.__c}")

class One(Demo):
    def show(self):
        print(super().a)
        print(super()._b)
        # print(super().__c)

do = Demo()
do.show()

print()

oo = One()
oo.show()