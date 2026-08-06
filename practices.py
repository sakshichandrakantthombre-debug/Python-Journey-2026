#!/usr/bin/env python
# coding: utf-8

# In[3]:


def hello():
    print("Hello world")
hello()


# In[14]:


#add two numbers;
def add(a,b):
    return a+b
print(add(3,5))


# In[20]:


# sub three numbers:

def sub(a,b,c):
    return a-b-c
print(sub(13,7,2))


# In[21]:


# mul of the given numbers:
def add(a,b,c):
    return a*b*c
print(add(3,5,10))


# In[40]:


# even or odd number:

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "odd"
print(even_odd(7))



# In[48]:


#largest of two numbers;

def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(15, 25))


# In[50]:


# def the square 

def square(n):
    return n*n
x=square(5)
print(x+10)


# In[54]:


# cube of numbers:
def cube(n):
    return n*n*n
print(cube(5))


# In[58]:


# print the number of the given 1 to n:

def print_number(n):
    for i in range(1,n+1):
        print(i)
print_number(10)


# In[71]:


# print the reverse numbers of the given numbers:
def reverse_num(num):
    reverse=0
    while num > 0:
        digit = num%10
        reverse=reverse*10+digit
        num=num //10
    return reverse
print(reverse_num(1234))


# In[ ]:




