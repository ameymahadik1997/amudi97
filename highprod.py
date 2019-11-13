#To print the highest product of the numbers in the given list
b=1
nums = [-1 , 14 , 23 , 0 , 2 , -9 , 19 , -8 , 3 ]
print(nums)
for i in nums:
	if i==0 or i<0:
		pass
	else:
		b=b*i
		
print('The highest product of the Numbers in the list is=>',b)
