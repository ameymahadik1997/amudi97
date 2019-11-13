#To find sum of all even numbers and lowest odd number in the given list
s=0
a=0
ch=[]
nums = [-1 , 14 , 23 , 0 , 2 , -9 , 19 , -8 , 3 ]
print(nums)
for i in nums:
        if i%2==0:
                s=s+i
        else:
                ch.append(i)
                a=min(ch)
print('The lowest odd number=>',a)
s=s+a
print('The sum of all even numbers and lowest odd number in the given list=>',s)
