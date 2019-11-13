#Plaindrome function to check whether user entry is palindrome or not?
def palindrome(str1):
    str2=str1[::-1]
    if str2==str1:
        print(str1,' is Palindrome')
    else:
        print(str1,'is not a palindrome')


palindrome('nitin')
palindrome('nit')
palindrome('malayalam')
palindrome('mom')
palindrome('raviraj')
