#!/usr/bin/env python
# coding: utf-8

# In[30]:


num=int(input("Enter number:"))
if num % 2 == 0:
    print("Even")
else:
    print("odd")


# In[31]:


a = int(input("A:"))
b = int(input("B:"))
if a < b:
    print("B is largest")
else:
    print("A is largest")


# In[9]:


age = int(input("Age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# In[33]:


a = int(input("A: "))
b = int(input("B: "))

if a < b:
    print("B is largest")

else:
    print("A is largest")


# In[12]:


if 5 > 2:
    print("Five is greater than two!")


# In[13]:


x = 5
y ="john"
print(x)
print(y)


# In[14]:


x = 4
x = "Sally"
print(x)


# In[16]:


x = str(3)
y = int(3)
z = float(3)
print(type(x))


# In[7]:


x = "awesome"
def myfunc(a):
    x = "fantastic"
    print("Python is" + x)
    myfunc(5)
    print("Python is " + x)


# In[34]:


for i in range(100, 0, -1):
    print(i, end=" ")


# In[36]:


for i in reversed(range(1,101)):
    print(i,end=" ")


# In[1]:


i=5
for i in range(1, 11):
    print(i*5)


# In[2]:


for i in range(1, 20):
    if i%2==0:
        print("even", i, end=" ")
    else:
        print("odd", i, end=" ")


# In[21]:


a=9
b=10
if a<b:
    print(" b is greater than a")


# In[27]:


number=12
if number<100:
    print("it is true")


# In[28]:


score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")


# In[29]:


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# In[33]:


i=1
while i<8:
    print(i)
    if i == 7:
        break
    i += 1


# In[34]:


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# In[36]:


i=1
while i < 9:
    print(i)
    i += 1
else:
    print("i is no longer less than 9")


# In[41]:


i=2
for i in range(1, 9):
    print(i+1)


# In[ ]:




