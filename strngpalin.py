#To print if palindrome
def palindrome(str1):
    str2=str1[::-1]
    if str2==str1:
        for i in str1:
            print(i,'\n')
    else:
        print(str1,'is not a palindrome')
    print('\n')


palindrome('nitin')
palindrome('nit')
palindrome('malayalam')
palindrome('mom')
palindrome('raviraj')
