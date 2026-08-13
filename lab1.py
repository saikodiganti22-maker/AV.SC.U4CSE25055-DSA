''''
#if-else statement
num=int(input('Enter your number:'))
if num>0:
    print("positive numder")
else:
    print('Negative number')

#indentation 
x=1
total=0
if x!=0:
    total+=x
    print(total)
print("This is always executed.")

#if,elif and else
number = -5
if number > 0:
    print('Positive number')
elif number < 0:
    print('Negative number')
else:
    print('Zero')
print('This statement is always executed')

#nested if
number = 5
if number >= 0:
    if number == 0:
      print('Number is 0')
    else:
        print('Number is positive')
else:
    print('Number is negative')
 
#Loops
languages = ['Swift', 'Python', 'Go']
for lang in languages:
    print(lang)
 
#indentaTION IN LOOPS
languages = ['Swift', 'Python', 'Go']
for lang in languages:
    print(lang)
    print('-----')
print('Last statement')

#LOOp through a string
language = 'Python'
for x in language:
    print(x)

#for loop in python range
for i in range(0, 4):
    print(i)
 
#Break statement
languages = ['Swift', 'Python', 'Go', 'C++']
for lang in languages:
    if lang == 'Go':
        break
    print(lang)
 
#continue statement
languages = ['Swift', 'Python', 'Go', 'C++']

for lang in languages:
    if lang == 'Go':
        continue
    print(lang)

#nested for loop
attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']
for attribute in attributes:
    for car in cars:
        print(attribute, car)
    print("-----")

#while loop
number = int(input('Enter a number: '))
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))
print('The end.')
'''
#pass statement
n = 10 
if n > 10:
    pass
print('Hello')
