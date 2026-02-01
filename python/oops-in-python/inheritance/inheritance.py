class Car: # parent class
    color = "black"

    def greet(self):
        print("I am class Car")

class Swift(Car): # child class
    pass

so = Swift()
print(so.color)
so.greet()