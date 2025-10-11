# write a function to check if string is palindrome or not

def isPalindrome(str):
    rev = ""
    for i in range(len(str)-1, -1, -1):
        rev += str[i]

    if str == rev:
        return f"{str} is palindrome string"
    else:
        return f"{str} is not a palindrome string"
    
print(isPalindrome("NAMAN"))

print(isPalindrome("ADITYA"))