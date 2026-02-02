class One:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hello {self.name}! you are {self.age} years old."
    
oo = One("Ajay", 25)
print(oo)