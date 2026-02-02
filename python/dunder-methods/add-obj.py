class One:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return f"sum of ages: {self.age + other.age}"
    
oo = One("Amar", 25)
to = One("Raj", 26)

print(oo + to)