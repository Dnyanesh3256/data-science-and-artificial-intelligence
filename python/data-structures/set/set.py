s = {1, 2, 3, 4, "amay"}    # duplicates not allowed

print(s)

print(hash("ags")) 

for i in s:
    print(i)

s.add(55)
print(s)

s.remove("amay")
print(s)

s.discard("amay") # throws error

s.discard("amay") # dont throw error

print(s)
s.pop()
print(s)

s.clear()
print(s)