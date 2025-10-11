# find the second greatest element

nums = [13, 8, 25, 65, 70, 45, 49, 72, 71]

max = -1
secMax = -1

for i in nums:
    if i > max:
        secMax = max
        max = i

    elif i > secMax:
        secMax = i

print(secMax)