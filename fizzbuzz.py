#!/usr/bin/env python3
'''
Created on Apr 30, 2018
@author: Charles Liss
Fizz Buzz Game
1) Accepts the input of a number
2) If div 3 print fizz
3) If div 5 print buzz
4) if div by both print 3 and 5 fizz buzz

To Do Improvements
    1) Given a range of numbers
    2) Validate input method (greater than 0 and TypeInt)
    3) Write unit tests
    

'''

def main():
    inputValue = None
    while(inputValue != 0):
        inputValue = int(input('Give me a number: '))
        doMath(inputValue)
    print ('DONE') 


# class FizzBuzz:
#     def __init__(self, value):
#         self._value = value
#         
#     def value(self):
#         return._value
        
def doMath(value):
#  print('I have the number {} '.format(value))
# print(f'I have the number{value}')
# print(f'value is of type{type(value)}')
    if (value%15==0):
        print('FizzBuzz')
    elif (value%5==0):
        print('Buzz')
    elif(value%3==0):
        print('Fizz')
    else: (print(f'{value}'))
    
if __name__ == '__main__': main()

