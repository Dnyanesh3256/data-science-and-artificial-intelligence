# count the frequency of each element in a list

l1 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 6]

d1 = {}

for i in l1:
    if i in d1.keys():
        d1[i] += 1
    else:
        d1[i] = 1

print(d1)