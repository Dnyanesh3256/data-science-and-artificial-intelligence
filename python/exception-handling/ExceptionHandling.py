# divide by zero

print("start")

a = int(input("Enter the number : "))

try:
    print(10/a)

except Exception as err:
    print(f"sorry there is an error as {err}")

else:
    print("good there is no exception")
    
finally:
    print("I will run no matter what")

print("ok i have done the division")