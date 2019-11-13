#Student name and course joined
class Student:
	def __init__(self):
		self.__sname=input('Enter The Student Name=>')
		self.__course=input('Enter The course joined=>')
		
	def showinfo(self):
		print('Student Name=',self.__sname,',Thanks for joining course= ',self.__course)
	
		
	def __del__(self):
		print('Thanks for using destructor :).')

def main():
	s1=Student()
	s2=Student()
	s1.showinfo()
	del s1
	s2.showinfo()
	del s2

if __name__=='__main__':
	main()
