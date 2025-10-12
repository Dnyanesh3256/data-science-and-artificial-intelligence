d1 = {1:10, 2:20, 3:30, 4:20}

print(type(d1))

print(d1[2])

d1[5] = 50

print(d1.keys())

d1.popitem()

print(d1)

print("dictionary traversing : ")
for d in d1:
    print(f"key = {d}, value = {d1[d]}")