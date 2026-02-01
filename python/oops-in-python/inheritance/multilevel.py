class GrandFather:
    def gf(self):
        print("I am GrandFather")

class Father(GrandFather):
    def fm(self):
        print("I am Father")

class Child(Father):
    pass

co = Child()
co.gf()
co.fm()