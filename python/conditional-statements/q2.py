# accept the gender from the user as char and print the respective greeting message

gender = str(input("enter your gender (m or f) : "))

if(gender == "m" or gender == "M"):
    print("Good morning Sir!")
elif(gender == "f" or gender == "F"):
    print("Good morning Mam!")
else:
    print("enter correct gender")