class Animal:
    def show(self):
        print("I am Animal")

class Dog(Animal):
    def show(self):
        print("I am Dog")

do = Dog()
do.show()