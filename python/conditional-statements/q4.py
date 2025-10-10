# Accept name and age from the user. Check if the user is a valid voter or not

age = int(input("enter your age : "))

if(age >= 18):
    print("you are a valid voter!")
else:
    print("you are not a valid voter!")