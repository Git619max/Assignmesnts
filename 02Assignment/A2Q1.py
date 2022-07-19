def check_pal(str1):
    str2 = str1[::-1]
    if(str1==str2):
        print("palindrome")
    else:
        print("not palindrome")

word = input("Enter a string")
check_pal(word)