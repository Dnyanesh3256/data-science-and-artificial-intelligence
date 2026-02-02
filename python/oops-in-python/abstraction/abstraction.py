from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(Abstract):
    def perimeter(self):
        print("perimeter in square")

    def area(self):
        print("area in square")

so = Square()
so.area()
so.perimeter()