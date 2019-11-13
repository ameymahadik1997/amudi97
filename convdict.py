#To print the count of the character in dictionary
ch=[]
dic={}
c=0
str1=''
list1=input('Enter a String of characters=>')
print(list1)
l=len(list1)
while c<l:
        b=list1[c]
        col=list1.count('{}'.format(b))
        c=c+1
        dic[b]=col
print('\n')
print(dic)
        


		

		
		

		
