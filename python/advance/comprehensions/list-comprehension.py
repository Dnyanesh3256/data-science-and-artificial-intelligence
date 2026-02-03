comprehension = [i for i in range(1, 51) if i%2 == 0]
print(comprehension)
print()

comprehension2 = ["EVEN" if(i%2==0) else "ODD" for i in range(1, 51)]
print(comprehension2)