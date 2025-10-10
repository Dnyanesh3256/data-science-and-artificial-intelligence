# accept a number and check if it a perfect number or not. a number whose sum of factors is equal to the number itself

n = int(input("enter the number : "))
factSum = 0
for i in range(1, n):
    if n%i == 0:
        factSum += i

if factSum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")