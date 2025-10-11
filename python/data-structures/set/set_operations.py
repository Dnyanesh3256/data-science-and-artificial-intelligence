s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

un = s1.union(s2)
print(un)

inters = s1.intersection(s2)
print(inters)

diff = s1.difference(s2)
diff2 = s2.difference(s1)
print(diff)
print(diff2)

sym_diff = s1.symmetric_difference(s2)
print(sym_diff)