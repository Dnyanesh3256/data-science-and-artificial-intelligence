class Parent:
    def show(self):
        print("I am Parent")

class Child(Parent):
    def my(self):
        print("I am Child")

co = Child()
co.show()
co.my()