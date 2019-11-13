#To find all double digit numbers that are divisible by 2 and 3 simultaneously
n=10
c=0
print('The double digit numbers divisible by 2 and 3 are=>',end='')
while n<100:
    if n%2==0 and n%3==0:
        print(n,end=' , ')
        c=c+1
  
    n=n+1
print('\n')
print('The total number of two digit numbers divisible by 2 and 3 simultaneously are=>',c)

    
    
