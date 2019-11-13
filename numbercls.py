#Number class to use different objects to increments and decrement
class Number:
    def __init__(self,__num):
        self.__num=__num
        print(self.__num)

    def increment(self):
        self.__num=self.__num+1

    def decrement(self):
        self.__num=self.__num-1

    def display(self):
        print(self.__num)



def main():
    a1=Number(10)
    a2=Number(20)
    a3=Number(30)
    a4=Number(40)
    a5=Number(50)
    a1.increment()
    a2.increment()
    a3.decrement()
    a4.increment()
    a5.decrement()
    a1.display()
    a2.display()
    a3.display()
    a4.display()
    a5.display()

if __name__=='__main__':
    main()
    
        
