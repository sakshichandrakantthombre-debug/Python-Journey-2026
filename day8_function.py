#!/usr/bin/env python
# coding: utf-8

# In[4]:


# greet()
def greet():
    print("Hello, welcome to Python!")
greet()


# In[6]:


# funtion with parameters:
def add(a,b):
    return a+b
result = add(10, 20)
print(result)


# In[8]:


# parts of a user-defined function
def add(a,b):
    return a+b
print(add(5,3))


# In[12]:


#sum
def sum(n1,n2):
    res=n1-n2
    return res
totle=sum(6, 4)
print(sum)


# In[17]:


#mul:
def mul(n1, n2):
    res1=n1*n2
    return res1
totle=mul(6, 7)
print(totle)


# In[22]:


#check the given number  even number :
def EV(x,a):
    if x%2==0:
        return True
    else:
        return False


# In[25]:


y=EV(10, 12)
print(y)


# In[37]:


#check the given number  odd number :
def OD(x,a):
    if x%2!=0:
        return True
    else:
        return False


# In[38]:


y=OD(20, 40)
print(y)


# In[40]:


#Area of circle
def AC(r):
    Area_circle= 2*3.14*r
    return Area_circle

result=AC(7)
print(AC)



# In[41]:


# calculate the area of rectangle given data:
def area(l,b):
    res=l*b
    return res 

totle_area=area(7,5)
print( "area of recangle", totle_area)


# In[44]:


# calculate the area of triangle:
def area(h,b):
    res=0.5*h*b
    return res
totle_area=area(7,8)
print("area of triangle" ,totle_area)


# In[47]:


# square of the given number:
def square(b):
    res=b**2
    return res
sq=square(8)
print("square of number", sq)


# In[48]:


# cube of the given number:
def cube(b):
    res=b**3
    return res
CB=cube(8)
print("square of number", CB)


# In[ ]:




