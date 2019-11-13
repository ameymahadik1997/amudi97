#Swapping numbers
class Swap:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print('Number 1=',self.a)
        print('Number 2=',self.b)
    def swapNum(self,temp):
        self.temp=self.a
        self.a=self.b
        self.b=self.temp
        print('Swapped Numbers are shown below:-')
        print('Number 1=',self.a)
        print('Number 2=',self.b)

def main():
    s=Swap(10,20)
    s.swapNum(0)

if __name__=='__main__':
    main()
        
