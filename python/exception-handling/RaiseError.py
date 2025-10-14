# create your own error

# age = int(input("enter your age : "))

# if age < 10 or age > 18:
#     raise ValueError("your age must be between 10 and 18")
# else:
#     print("welcome to the club")

# print("the club will open soon!")

age = int(input("enter your age : "))

try:
    if age < 10 or age > 18:
        raise ValueError("your age must be between 10 and 18")
    else:
        print("welcome to the club")

except Exception as err:
    print(f"error occured as {err}")

print("the club will open soon!")