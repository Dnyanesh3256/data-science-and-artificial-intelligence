# separate each digit of a number and print it on the new line

n = 256

while n > 0:
    print(n%10)
    n //= 10