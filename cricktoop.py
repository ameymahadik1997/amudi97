#Cricketer class to find their age using datetime module
from datetime import datetime 
class Cricketer:
    def __init__(self,name,byear):
        self.name=name
        self.byear=byear
        print('Cricketer=',self.name,'their birth year =',self.byear)

    def age(self):
        self.n=datetime.now()
        self.diff=self.n.year-self.byear
        print("The Cricketer's age is=>",self.diff)

def xxyy():
    c1=Cricketer('Sachin',1976)
    c1.age()
    c2=Cricketer('Virat',1990)
    c2.age()
    


xxyy()
        
