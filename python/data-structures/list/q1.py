# print positive and negative elements of an list

nums = [-2, 5, 45, -98, 18, -10]

print("positive elements : ")
for i in nums:
    if i >= 0:
        print(i)

for i in nums:
    if i < 0:
        print(i)