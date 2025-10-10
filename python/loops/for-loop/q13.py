# count all letters, digits and special symbols from a given string

str = "P@#yn26at^&i5ve"

chars = 0
digits = 0
spch = 0

for ch in str:
    if ch.isalpha():
        chars += 1
    elif ch.isdigit():
        digits += 1
    else:
        spch += 1

print(f"Characters count : {chars}\n Digits count : {digits}\n Special characters count : {spch}")