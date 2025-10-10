# check whether the number is prime or not

n = int(input("enter the number : "))
count = 0
for i in range(1, n+1):
    if n%i == 0:
        count += 1
    
if count == 2:
    print("entered number is prime number")
else:
    print("entered number is not a prime number")



