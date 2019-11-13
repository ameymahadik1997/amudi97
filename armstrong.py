#To print whether the number enetered is a armstrong number or not
c=0
sumall=0
num1=int(input('Enter The number to be checked if Armstrong or not=>'))
num2=str(num1)
l=len(num2)
while c<l:
    i=num2[c]
    j=int(i)
    sumall=sumall+j**3
    c=c+1
if sumall==num1:
    print('The number entered by the user=',num1,'is an Armstrong number')
else:
    print('The number entered by the user=',num1,'is not an Armstrong number')
