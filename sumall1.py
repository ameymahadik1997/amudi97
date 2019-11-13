#To print the sum of the digits in a given user number
a=input('Enter the Number=>')
c=len(a)
b=1
b1=0
sumall=0
while b<=c and b1<=c-1:
    l=a[b1:b]
    lint=int(l)
    sumall=sumall+lint
    b=b+1
    b1=b1+1
print('The addition of the digits of the number entered=>',sumall)
    
