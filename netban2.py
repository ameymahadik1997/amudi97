#Netbanking (Transfer between two object)
class invalidPin(Exception):
    pass
class insufficientBalance(Exception):
    pass
class Netbanking:
        temp=0
        c=1
        def __init__(self,balance,pin):
                self.balance=balance
                self.pin=pin
        def showinfo(self,other):
                print('User1 Balance=',self.balance)
                print('User2 Balance=',other.balance)
                
        def check(self):
                self.amt=int(input('enter money='))
                Netbanking.temp=self.amt
                if self.amt<self.balance:
                        b=self.balance-Netbanking.temp
                        print('User1 to transfer amount will have now balance=',b)
                else:
                        Netbanking.c='CHECK'
                        raise insufficientBalance('Insufficient Balance')
                        
        def transfer(self,other):
                if Netbanking.c!='CHECK':
                        other.balance=self.balance+Netbanking.temp
                        print('User2 to get amount will have balance=',other.balance)
                
                
def xyz():
        c1=Netbanking(2000,121)
        c2=Netbanking(2000,213)
        c1.showinfo(c2)
        passw=int(input('Enter the user1 pin=>'))
        if passw==c1.pin:
            try:
                c1.check()
            except insufficientBalance as ib:
                print(ib)
            c1.transfer(c2)
        else:
            try:
                raise invalidPin('Invalid Pin')
            except invalidPin as ip:
                print(ip)
            
xyz()
