#Menu driven calc usingfunctions and while true
def add():
    a=int(input("Enter Number 1="))
    b=int(input("Enter Number 2="))
    c=a+b
    print('The Addition of two numbers is',c)
def sub():
    a=int(input("Enter Number 1="))
    b=int(input("Enter Number 2="))
    c=a-b
    print('The Substraction of two numbers is',c)
def mul():
    a=int(input("Enter Number 1="))
    b=int(input("Enter Number 2="))
    c=a*b
    print('The Multiplication of two numbers is',c)
def div():
    a=int(input("Enter Number 1="))
    b=int(input("Enter Number 2="))
    c=a/b
    print('The Division of two numbers is',c)
def floor():
    a=int(input("Enter Number 1="))
    b=int(input("Enter Number 2="))
    c=a//b
    print('The Floor Division of two numbers is',c)
    

    
while True:
    print(' Enter "+" for add \n Enter "-" for minus \n Enter "*" for multiplication \n Enter "/" for division \n Enter "//" for floor division \n Enter "E" to exit' )
    ch=input(' Enter the Choice=>')
    if ch in '+':
        add()
    elif ch in '-':
        sub()
    elif ch in '*':
        mul()
    elif ch in '/':
        div()
    elif ch in '//':
        floor()
    elif ch in ('e','E'):
        print('Thanks for using Calculator')
        break
    else:
        print('Invalid Choice!')
