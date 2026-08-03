#!/usr/bin/env python
# coding: utf-8

# In[28]:


#1>check whether the number is even or 

num =(12)
if num % 2 == 0:
    print("even")
else:
    print("odd")


# In[32]:


#2>largest of theree numbers;

a=10
b=20
c=50
print(max(a,b,c))


# In[33]:


#3> factorial:

num=5
fact=1
for i in range (1,num+1):
    fact *= i
    print(fact)


# In[34]:


#4>reverse a string:

text="Python"
print(text[::-1])


# In[45]:


text="python"
print(text[1:])


# In[47]:


#5> count vowels

text="Programming"
count=0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print(count)


# In[46]:


name="sakshi"
count=0
for ch in name.lower():
    if ch in "aeiou":
        count +=1
print(count)


# In[50]:


#6> remove duplicates from list:

numbers=[1, 2, 2, 3, 4, 4, 5]
unique=list(set(numbers))
print(unique)


# In[51]:


height=5.2
print(height)


# In[52]:


name = input("Enter the number:")
print("Your name is:",name)


# In[53]:


age=int(input("Enter  your age: "))
print("Age=", age)


# In[54]:


a=4
b=8
print("Mul=", a*b)


# In[ ]:





# In[56]:


#6> calculate the area of tringle;
length=int(input("Enter the length: "))
width=int(input("Enter the breadth: "))
area=length*width
print("Area of triangle=", area)


# In[57]:


#7> swap two variable:

a=20
b=30
a,b=b,a
print(a)
print(b)


# In[59]:


#8> calculate the average of given data:

a=int(input("Enter first marks:"))
b=int(input("Enter second marks:"))
c=int(input("Enter third marks:"))
average=(a+b+c)/3
print("Average=", average)


# In[60]:


#9> convert celsius to fahrenheit

c=float(input("Enter Celsius:"))
f=(c*9/5) +32
print("Fahrenheit=", f)


# In[61]:


#10> simple interest:

p=float(input("Principle: "))
r=float(input("Rate:"))
t=float(input("Time:"))

si=(p*r*t)/100
print("Simple interest =", si)


# In[ ]:




