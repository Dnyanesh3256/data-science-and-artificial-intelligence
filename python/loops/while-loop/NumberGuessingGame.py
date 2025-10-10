# create a random number guessing game with python

import random

num = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("guess the number between 1 to 100 : "))

    if guess == num:
        tries += 1
        print(f"congratulations! you guessed the number in {tries} tries")
        break
    
    elif guess < num:
        tries += 1
        print("go a little higher")

    else:
        tries += 1
        print("go a little lower")