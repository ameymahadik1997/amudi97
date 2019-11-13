#Netbanking (Transfer between two object)
class InvalidPin(Exception):
        pass
class InsufficientBalance(Exception):
        pass
class Netbanking:
        temp=0
        c=1
        def __init__(self,balance,pin):
                self.balance=balance
                self.pin=pin
        def showinfo(self):
                print('User Balance=',self.balance,' ','Pin=',self.pin)
        def check(self):
                self.amt=int(input('Enter money='))
                Netbanking.temp=self.amt
                if self.amt<self.balance:
                        self.b=self.balance-Netbanking.temp
                        print('User1 to transfer amount will have balance=',self.b)
                else:
                        Netbanking.c='CHECK'
                        raise InsufficientBalance('Insufficient balance to complete process')
                        
                        
        def transfer(self):
                if Netbanking.c!='CHECK':
                        self.b=self.balance+Netbanking.temp
                        print('User2 to get amount will have balance=',self.b)
                        
        def inval(self):
                raise InvalidPin(' The Pin Entered is Invalid')
                
                
def xyz():
        c1=Netbanking(2000,121)
        c1.showinfo()
        c2=Netbanking(2000,213)
        c2.showinfo()
        passw=int(input('Enter the user1 pin=>'))
        if passw==c1.pin:
                try:
                        c1.check()
                        c2.transfer()
        
                except InsufficientBalance as ib:
                        print(ib)

  
        else:
                try:
                        c1.inval()
                except InvalidPin as ipin:
                        print(ipin)
          
xyz()
