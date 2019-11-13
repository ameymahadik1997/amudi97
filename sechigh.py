#To print the second highest number in the
given list
ch=[]
c=0
nums = [-1 , 14 , 23 , 0 , 2 , -9 , 19 , -8 , 3 ]
for i in nums:
	if i>0:
		ch.append(i)
print(nums)
ch.sort()
l=len(ch)
c=ch[l-2]#because range starts from 0 so 'l-1' gives an error of IndexError 
print('The second highest number in the given list =>',c)
	
