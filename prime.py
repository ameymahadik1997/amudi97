#WAP to check whether the nymber entered by the user is prime or not
while True:
    a=int(input('Enter the number to be checked if prime or not=>'))
    if a==0:
        print('Number is a Zero')
    elif 0<a<=2:
        print('The Number entered=',a,'is a prime')
    elif a>2:
        for i in range(2,a):
            if a%i==0:
                print('The number entered=',a,'is not a prime')
                break
        else:
            print('The number entered=',a,'is a prime')
    elif a<0:
        print('Number is a Negative')

    else:
        print('Invalid')
