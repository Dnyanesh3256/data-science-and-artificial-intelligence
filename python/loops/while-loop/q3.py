# accept a number and check if it is palindromic number

n = int(input("enter the number : "))
on = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if rev == on:
    print(f"{on} is a palindromic number")
else:
    print(f"{on} is not a palindromic number")