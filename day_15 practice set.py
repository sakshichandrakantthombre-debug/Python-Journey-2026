#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = 'sakshi'
age = 21
print(name)
print(age)


# In[2]:


name=input("enter the name: ")
print("hello", name)


# In[4]:


num=int(input("Enter the number"))
if num>100:
    print("positive")
else:
    print("Negative")


# In[6]:


for i in range(1,11):
    print(i*2)


# In[10]:


i=1
while i<=5:
    print(i)
    i +=1


# In[14]:


def sqaure(n):
    return n*n
print(sqaure(5))


# In[17]:


def sum(x,y=8):
    return x+y
print(sum(x=5,))


# In[21]:


numbers=[10, 20, 30, 40]
for num in numbers:
    print(num)


# In[22]:


student = {
    "name": "sakshi", "age": 22
}
print(student["name"])


# In[29]:


totle= 0
for i in range(1, 11):
    totle+=i
print(i)


# In[31]:


num=input("Enter the number:")


# In[33]:


list=[1, 2, 3, 4, 5]
print(list)


# In[34]:


print(max(list))


# In[35]:


print(min(list))


# In[37]:


print(len(list))


# In[41]:


list.append(6)
print(list)


# In[42]:


list.pop()
print(list)


# In[43]:


list.remove(4)
print(list)


# In[45]:


list.insert(0, "mango")
print(list)


# In[46]:


list.reverse()
print(list)


# In[ ]:




