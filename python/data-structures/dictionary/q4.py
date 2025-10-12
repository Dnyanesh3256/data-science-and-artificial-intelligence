# write a python program to combine two dictionary by adding values for common keys

d1 = {1:10, 2:20, 3:30, 4:40}
d2 = {3:30, 4:40, 5:50, 6:60}

for d in d2:
    if d in d1.keys():
        d1[d] += d2[d]
    else:
        d1[d] = d2[d]

print(d1)