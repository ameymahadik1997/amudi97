#Func with recursion to find factorial
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
        


print(factorial(10))
print(factorial(8))
print(factorial(15))
print(factorial(4))
print(factorial(6))
