# check if list is sorted or not

nums = [10, 12, 14, 16, 18, 20]

for i in range(0, len(nums)-1):
    if nums[i] < nums[i+1]:
        continue
    else:
        print("your list is not sorted")
        break

else:
    print("your list is sorted")