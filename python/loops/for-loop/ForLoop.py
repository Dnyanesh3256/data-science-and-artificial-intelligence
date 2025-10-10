# for i in range(1, 21, 1):
#     print("hey boss!", i)

# for i in range(16, 0, -1):
#     print(i)

# for i in range(20, 51):
#     print(i)

# for i in range(-3, -16, -1):
#     print(i)

# num = int(input("which table do you want : "))
# for i in range(num, num*10+1, num):
#     print(i)

# name = "DNYANESHWAR TUPE"
# for i in range(len(name)):
#     print(name[i])
# for i in name:
#     print(i)

# for i in range(1, 21):
#     if i == 10:
#         continue
#     print(i)

# for i in range(1, 21):
#     if i == 10:
#         break
#     print(i)

for i in range(1, 21):
    if i == 100:
        print("break statement executed")
        break
    print(i)
else:
    print("break statement not executed")