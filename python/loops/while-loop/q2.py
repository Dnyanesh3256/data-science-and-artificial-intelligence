# accept a number and print its reverse

n = int(input("enter the number : "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print(rev)