l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ans = filter(lambda i : True if i%2 != 0 else False, l)

print(list(ans))