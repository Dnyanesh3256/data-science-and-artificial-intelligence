# print the sum of all even and odd numbers in a range separately

n = int(input("enter the number : "))
oddSum = 0
evenSum = 0

for i in range(1, n+1):
    if i%2 == 0:
        evenSum += i
    else:
        oddSum += i

print("Odd Sum : ", oddSum)
print("Even Sum : ", evenSum)