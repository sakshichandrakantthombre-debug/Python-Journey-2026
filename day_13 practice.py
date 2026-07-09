#!/usr/bin/env python
# coding: utf-8

# In[8]:


#calculate the BMI report of the body:
weight=int(input("Enter the number"))
height=float(input("Enter the number"))
BMI=weight/height**2
print("BMI report of the body", BMI, end=" ")


# In[10]:


# print the fibocies series given number:
n=int(input("Enter the number"))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    c= a+b
    a=b
    b=c


# In[17]:


# print the table of the given number:
n=int(input("Enter the number"))
for i in range (1,11):
    print(i*n) 


# In[19]:


# return python function:
def add(a, b):
    print(a+b)
add(10, 20)


# In[20]:


def add(a,b):
    return a+b
result=add(10, 20)
print(result)


# In[22]:


def square(n):
    return n*n
x=square(5)
print(x)


# In[48]:


def test1():
    print(10)
def test2():
        return 10
a=test1()
b=test2()
print(a)
print(b)


# In[49]:


name="sakshi"
print(len(name))


# In[51]:


numbers=[10, 20, 30, 40]
print(max(numbers))


# In[52]:


numbers=[1, 2, 3, 4, 5]
print(min(numbers))


# In[55]:


numbers=[4, 5, 6, 7]
print(sorted(numbers))


# In[67]:


def even_odd(num):
    if num % 2== 0:
        return "Even"
    else:
        return "odd"
print(even_odd(7))


# In[69]:


def square(n):
    return n*n
print(square(5))


# In[72]:


def cube(n):
    return n**3
print(cube(8))


# In[ ]:




