def my_decorator(func):
    def wrapper():
        print("this will run before the function")
        func()
        print("this will run after function")

    return wrapper

@my_decorator
def hello():
    print("hello user")

hello()