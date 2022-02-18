text1=str(input("Check whether it Palindrome or Not:"))
text2=text1[::-1]
if text1==text2:
    print(text1," is Palindrome")
else:
    print(text1," isn't Palindrome")
