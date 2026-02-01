class Animal:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"hello... i am {self.name}")

class Human(Animal):
    pass

ho = Human("Akash")
ho.greet()