def odd(n):
    if n%2 != 0:
        return True
    else:
        return False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ans = filter(odd, l)

print(list(ans))