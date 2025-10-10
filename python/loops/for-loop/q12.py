# check string is palindrome or not

str = "NAMAN"
res = ""
for i in range(len(str)-1, -1, -1):
    res += str[i]

if str == res:
    print(f"{str} string is palindrome string")
else:
    print(f"{str} is not a palindrome string")