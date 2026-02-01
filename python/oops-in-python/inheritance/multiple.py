class Father:
    def dad(self):
        print("I am Father")

class Mother:
    def mom(self):
        print("I am Mother")

class Child(Father, Mother):
    pass

co = Child()
co.dad()
co.mom()