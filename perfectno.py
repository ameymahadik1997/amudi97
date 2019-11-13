#To find whether the number enetered is a perfect number or not
while True:
    b=0
    a=int(input('Enter the number to be checked if perfect number or not=>'))
    for i in range(1,a):
        if a%i==0:
            b=b+i
    if b==a:
        print('The number entered=',a,'is a perfect number')
        break
    else:
        print('The number entered=',a,'is not a perfect number')
    
