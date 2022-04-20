#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def median(a,b,c):
    '''
    this is a function for calculating the median of given numbers
    
        parametrs:
            - a: first number
            - b: second number
            - c: third number
        
        return:
            - median of numbers
    '''
    if b < a and a < c:
        print(a)
    elif c < a and a < b:
        print(a)
    
    elif c < b and b < a:
        print(b)
    elif a < b and b < z:
        print(b)
    
    elif b < c and c < a:
        print(c)    
    elif a < c and c < b:
        print(c)


# In[ ]:


def main():
    
    firstNumber = float(input("Enter the first number: "))
    
    secondNumber = float(input("Enter the first number: "))
    
    thirdNumber = float(input("Enter the first number: "))
    
    median(firstNumber,secondNumber,thirdNumber)
    

