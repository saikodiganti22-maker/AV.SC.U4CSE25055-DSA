#PYTHON FUNCTION 
'''  
def greet():
    print('Hello World!')    
greet()
print('Outside function')
  
def greet(name):
    print("Hello", name)
greet("John")
 
# function with two arguments
def ad_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)
ad_numbers(5, 4)
 
 
# Return statement
def find_sq(num):
    result = num * num
    return result
square = find_sq(3)
print('Square:', square)
 
#Python libRARY FUNCTIONS
import math
sq_root = math.sqrt(4)
print("Square Root of 4 is",sq_root)
power = pow(2, 3)#pow() is the builtin function which is power
print("2 to the power 3 is",power)
          
def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)
add_numbers(2, 3)
 
#Function Argument with Default Values
def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)
add_numbers(2, 3)
add_numbers(a = 2)
add_numbers()
 
# program to find sum of multiple numbers 
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Sum = ", result)
find_sum(2743685486,654965476476434929469297)
find_sum(52346777777777777777777777775287437347,436623563765743276510923847566547838)
find_sum(7,8,9)
find_sum(8,59)

# GLOBAL AND LOCALLLL VVARIABLE
message = 'Hello'
def greet():
    print('Local', message)
greet()
print('Global', message)
 
def outer():
    message = 'local' 
    def inner():
        nonlocal message
        message = 'nonlocal'
        print("inner:", message)
    inner()
    print("outer:", message)
outer()
 
# global variable
c = 1  
def add():
    print(c)
add()

c = 1 
def add():
    global c 
    c = c + 2
    print(c)
add()
 
#Recursion function
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
n=900
print("The factorial of",n,factorial(n))
'''
 
