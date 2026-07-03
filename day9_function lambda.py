#!/usr/bin/env python
# coding: utf-8

# # Anonymus functions(lambda):-

# In[1]:


add = lambda a, b: a+b
print(add(5,3))


# In[3]:


square = lambda x: x*x
print(square(4))


# In[4]:


even = lambda x: x%2==0
print(even(10))
print(even(7))


# In[1]:


x= lambda a: a+10
print(x(5))


# In[4]:


x=lambda a, b, c: a+b+c+60
print(x(3, 5, 6))


# In[10]:


num=[2, 4, 6, 8, 10]
doubled=list(map(lambda x: x*2, num))
print(doubled)


# In[12]:


num=[2, 4, 6, 8, 10]
doubled=list(map(lambda x: x+2, num))
print(doubled)


# In[16]:


num=[2, 4, 6, 8, 10]
res=list(map(lambda x: x*2, num))
print(res)


# In[17]:


student=[("email", 25), ("Tobies", 22), ("Linus", 28)]
sorted_students=sorted(student,key=lambda x: x[1])
print(sorted_students)


# In[19]:


area_rec=lambda h,b:0.5*h*b
area_rec(2,5)

area_circle=lambda r,r: 3.14*r*r
area_circle(5)
# In[7]:


area_circle=lambda r,d: 3.14*r*d
area_circle(5,5)


# In[10]:


CA=lambda r: 3.14*r**2
CA(5)


# In[11]:


AT=lambda h,b: 0.5*h*b
AT(5,4)


# In[12]:


l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


# In[13]:


# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


# In[16]:


# Return double of n
def addition(n):
    return n + n
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# In[22]:


num1=[1, 2, 3, 4]
result=map(lambda x: x, num1)
print(list(result))


# In[23]:


# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# In[27]:


numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


# In[ ]:




