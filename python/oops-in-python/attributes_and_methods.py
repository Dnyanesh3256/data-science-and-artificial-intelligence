class Car:
    year = 2020 # class attribute

    def __init__(self, color):
        self.color = color # instance attribute

    def method_one(self):
        print("i am instance method")

    @classmethod
    def method_two():
        print("i am class method")

    @staticmethod
    def method_three():
        print("i am static method")

obj = Car("red")

print(obj.year)
obj.method_one()

obj.method_three()