# write a python script to merge two python dictionaries

d1 = {1:10, 2:20, 3:30}
d2 = {4:40, 5:50, 6:60}

for d in d2:
    d1[d] = d2[d]

print(d1)