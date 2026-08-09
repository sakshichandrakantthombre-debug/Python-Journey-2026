#!/usr/bin/env python
# coding: utf-8

# # looping program python practice!
# 

# In[7]:


# sum of the numbers:
numbers = [10, 20, 30, 40, 50]
total=0
for num in numbers:
    total +=num
    print("Sum:", total)


# In[8]:


#2> Even numbers
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2==0:
        print(num)


# In[9]:


#3> odd numbers:
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num %2!=0:
        print(num)


# In[13]:


#4> multiplication table
num=7
for i in range(1,11):
    print(num, "x", i, "=", num*i)


# In[16]:


#5> count vowels
text="Python programing"
count=0
for char in text.lower():
    if char in "aeiou":
        count+=1
        print("vowels:",count)


# In[21]:


#6> find maximum number
numbers=[25, 10, 45, 32, 67, 15]
maximum=numbers[0]
for num in numbers:
    if num>maximum:
        maximum=num
    print("maximum:",maximum)


# In[23]:


#7> find the minimum numbers:
numbers=[25, 10, 45, 32, 67, 15]
minimum=numbers[0]
for num in numbers:
    if num>minimum:
        minimum=num
    print("minimum:",minimum)


# In[24]:


#8> factorial:
num=5
factorial=1
for i in range(1,num+1):
    factorial *=i
    print("Factorial:",factorial)


# In[26]:


#9> reverse a string:

text="Python"
reverse=""
for char in text:
    reverse=char+reverse
    print("Reverse:",reverse)


# In[28]:


#10> count positive and negative numbers:
numbers=[10, -5, 20, -8, 15, -2, 30]
positive=0
negative=0
for num in numbers:
    if num>0:
        positive +=1
    elif num<0:
        negative+=1
    print("Positive:", positive)
    print("Negative:", negative)


# In[ ]:




