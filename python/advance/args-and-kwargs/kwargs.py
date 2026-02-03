def information(**kwargs):
    print(kwargs)
    print("Your information: ")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

information(name="Akshay", age=19, designation="Engineer")