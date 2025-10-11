# find the greatest element and print its index too

nums = [7, 8, 5, 4, 3, 1]

max = -1
idx = -1

for i in range(0, len(nums)-1, 1):
    if max < nums[i]:
        max = nums[i]
        idx = i

print(f"maximum number is {max} and its index is {idx}")