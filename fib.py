#To print fibonacci series till 10:-
a=0
b=1
c=0
m=10
print('The Fibonacci series=>',end='')
print(a,',',b,end='')
for i in range(2,m):
    c=a+b
    a=b
    b=c
    if (c<=m):
        print(',',c,end='')
        
    
