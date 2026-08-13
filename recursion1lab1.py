'''#A
def count_down(n):
    i=n
    if i>=0:
        print('Launch')
        print(f'rocket launching in {i} seconds')
        return count_down(n-1)
n=int(input("Enter the countdown seconds:"))
count_down(n)
 
#C
def searching_emp_id(emp_list, key):
    for i in range(len(emp_list)):
        if emp_list[i] == key:
            return i
    return -1
emp_ids = []
n = int(input('Enter number of elements in the list: '))
for i in range(n):
    print("Enter employee id:")
    emp_ids.append(int(input()))
key = int(input("Enter the employee id to search: "))
result = searching_emp_id(emp_ids, key)
if result != -1:
    print(f"Employee ID found at index: {result}")
else:
    print("Employee ID not found.")
''' 
#B
def compound_interest_recursive(principal, rate, periods): 
    # Base case: no periods left, return the accumulated amount 
    if periods == 0: 
        return principal 
    next_principal = principal * (1 + rate) 
    return compound_interest_recursive(next_principal, rate, periods - 1)nb    
p = float(input("Enter the principle: ")) 
r = float(input("Enter the rate of interest (as a %): ")) / 100
t = int(input("Enter the time period: ")) 
total_amount = compound_interest_recursive(p, r, t)
interest = total_amount - p
print("The interest is:", interest)
'''
#D
def factorial(n):
    if(n==1):
        return 1
    return*factorial(n-1)
n=int(input("enter a number:"))
factorial(n)
#E
def fib(n):
    if(n<=1);
      return(n)
    return fib(n-1)+fib(n-2)
print(20)
'''



