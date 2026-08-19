#!/usr/bin/env python
# coding: utf-8

# In[1]:


# create a list:
n= ["apple", "grapes", "pineapple"]
n[1] ="blueberry"
print(n)


# In[2]:


#replace element of 1:
n=[1, 3, 5]
n[2]=0
print(n)


# In[3]:


#add element in list
n.append(9)
print(n)


# In[4]:


# remove element list
n.remove(0)
print(n)


# In[6]:


# list method
#1 append
fruits=["mango", "banana", "papaya"]
fruits.append("cherry")
print(fruits)


# In[8]:


#2 extend
fruits=["mango", "banana"]
more_fruits = ["cherry", "mango"]
fruits.extend(more_fruits)
print(fruits)


# In[50]:


#2 insert
fruits=["mango", "mango", "pineapple"]
fruits.insert(3, "banana")
print(fruits)


# In[22]:


#3 remove
fruits=["mango", "banana", "pineapple"]
fruits.remove("banana")
print(fruits)


# In[25]:


#4 clear
fruits=["mango", "banana", "pineapple"]
fruits.clear()
print(fruits)


# In[28]:


#4 finding index
fruits=["mango", "banana", "pineapple"]
fruits.index("mango")
print(index)


# In[37]:


# finding index within a range:
fruits=["mango", "banana", "pineapple", "banana"]
index=fruits.index("banana", 2)
print(index)


# In[42]:


#  count element:
fruits=["mango", "banana", "pineapple", "banana"]
count=fruits.count("banana")
print(count)


# In[41]:


# revese a string
fruits=["mango", "banana", "pineapple", "banana"]
reverse=fruits.reverse()
print(fruits)


# In[44]:


#sortinng list in reverse order:
numbers= [40, 50, 30, 7, 10]
numbers.sort()
print(numbers)


# In[45]:


numbers.sort(reverse=True)
print(numbers)


# In[46]:


list=["apple", "blackberry", "papaya", "watermalon"]
list.sort(reverse=True)
print(list)


# In[53]:


list=["apple", "papaya", "Blackberry", "watermalon"]
list.sort(key=len, reverse=True)
print(list)


# In[57]:


# pop with index value:
numbers=[10, 20, 30, 40]
popped=numbers.pop(1)
print(popped)


# In[62]:


numbers=[10, 20, 30, 40]
last = numbers.pop
print(last)
print(numbers)


# In[63]:


# copy in method list:
fruits=["mango", "banana", "pineapple", "banana"]
copy_fruits=fruits.copy()
print(copy_fruits)


# In[4]:


#list comprehension means means in python
#create a new list for a fast  or small steps:
numbers= [1, 2, 3, 4, 5]
cube = [x**3 for x in numbers]
print(cube)


# In[6]:


numbers= [1, 2, 3, 4, 5]
square= [x**2 for x in numbers]
print(square)


# In[8]:


# even numbers:
numbers =[1, 2, 3, 4, 5, 6, 7, 8]
even_num=[x for x in numbers if x%2==0]
print(even_num)


# In[9]:


numbers =[1, 2, 3, 4, 5, 6, 7, 8]
odd_num=[x for x in numbers if x%2!=0]
print(odd_num)


# In[10]:


#convert to uppercase
names = ["sakshi", "python", "ai"]
upper = [name.upper() for name in names]
print(upper)


# In[4]:


names = ["sakshi", "python", "ai"]
upper=[name.upper()for name in names]
print(upper)


# In[14]:


names = ["SAKSHI", "PYTHON", "AI"]
lower=[name.lower() for name in names]
print(lower)


# In[16]:


# negative numbers
numbers = [-10, 5, -3, 2, -6, 7]
negative = [x for x in numbers if x < 0]
print(negative)


# In[17]:


# negative numbers:
numbers = [-10, 5, -3, 2, -6, 7]
positive = [x for x in numbers if x > 0]
print(positive)


# In[21]:


# print the positive as well as negative numbers square in list:
numbers = [12, -5, 8, -9, 15, -2, 0]
negative= [x for x in numbers if x < 0]
print("Negative numbers", negative)
positive= [x for x in numbers if x > 0]
print("Positive numbers", positive)


# In[23]:


# even numbers squares:
numbers=[10, 20, 5, 7, 9]
even_num=[x**2 for x in numbers if x%2==0]
print(even_num)


# In[25]:


# print even numbers list:
numbers=[10, 20, 5, 7, 9]
even_num=[x for x in numbers if x%2==0]
print(even_num)


# In[26]:


# 1 to 20 divisible by 3 create list
numbers=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
div_num=[x for x in numbers if x%3==0]
print(div_num)


# In[27]:


# print the range 1, 21 to divisible by 5 list:
numbers=range(1,21)
div_num=[x for x in numbers if x%3==0]
print(div_num)


# In[31]:


print the big numbers given list from greater than 5:
numbers=[1, 2, 4, 9, 8, 20, 5, 60]
big_num=[x for x in numbers if x>5]
print(big_num)


# In[36]:


print odd or even square in list:
numbers=[1, 2, 4, 9, 8, 20, 5, 60]
big_num=[x**2 for x in numbers if x%2==0] 
print("Even numbers square", big_num)
big_num=[x**2 for x in numbers if x%2!=0] 
print("Odd numbers square", big_num)


# In[37]:


#print the vowels list from given text:
text="python programming"
vowels =[ch for ch in text if ch in "aeiou"]
print(vowels)


# In[54]:


# print the vowels list from given text:
text="My name is sakshi"
vowels=[ch for ch in text if ch in "aeiou"]
print(vowels)


# In[1]:


#wap to generate list of random numbers and make two 
#different list as odd numbers list and even num list from original list:
num=[2, 4, 6, 9, 8,5]
Odd_num=[x for x in num if x%2==0]
print("odd num", Odd_num)
even_num=[x for x in num if x%2!=0]
print("Even num", even_num)


# In[2]:


l1=[1, 2, 3, 4, 8, 10, 50]
OL=[]
EL=[]
for i in l1:
    if i%2==0:
        EL.append(i)
    else:
        OL.append(i)
        print(f"Original list: {l1}\nEven number list : {EL}\nodd number list: {OL}") 


# In[3]:


s1= {}
print(type(s1))


# In[11]:


s2=set()
print(type(s2))


# In[4]:


s3= {1, 2, 2, 1, 3, 4, 3, 5, }
print(s3)


# In[5]:


s4={1, "ram", 78.86}
print(s4)


# In[55]:


s3[2]


# In[7]:


s3.add(20)
print(s3)


# In[8]:


s3.update("abc")
print(s3)



# In[9]:


s3.update(100)
print(s3)


# In[21]:


s3.add("pune")
print(s3)


# In[30]:


s3.remove("pune")
print(s3)


# In[24]:


s3.remove(100)
print(s3)


# In[10]:


print(s3.discard(100))


# In[11]:


s3={1, 6, 9, 'j', 'a'}
s3.discard('a')
print(s3)


# In[12]:


s3.remove("b")
print(s3)


# In[13]:


#Intersection
A ={1, 2, 3, 4, 5}
B ={4, 5, 6, 7, 8}
A.intersection(B)


# In[14]:


#union
A.union(B)


# In[15]:


# Difference
A.difference(B)


# In[36]:


B.difference(A)


# In[16]:


A = {1, 2, 3, 4, 5}
B=  {4, 5, 6, 7, 8}
A.union(B)-A.intersection(B)


# In[17]:


A.difference(B)


# In[48]:


A.intersection(B)


# In[19]:


# dictionary
#key & value pair,separated by:

d1 ={}
print(type(d1))


# In[20]:


d2=dict()
print(type(d2))


# In[55]:


d3 ={1:'Ram', 2:'Sham', 3:'jay', 4:'vijay'}
d3[2]


# In[57]:


d3[4]='om'
print(d3)


# In[46]:


d3[5]= 'Ajay'
print[d3]


# In[60]:


d3.update({6:'sachin'})
print(d3)


# In[61]:


d3.popitem()
print(d3)


# In[13]:


d3={1, 'a', 'b', 6, 9}
d3.pop()
print(d3)


# In[66]:


d3.keys()


# In[65]:


d3.values()


# In[67]:


d3.items()


# In[70]:


del d3[2]
print(d3)


# In[22]:


d3.clear()
print(d3)


# In[29]:


# string
l1=["ajay", "hello", "kiran", "sakshi"]
print(l1)


# In[24]:


l1[1]


# In[25]:


l1[-2]


# In[30]:


l1[3]


# In[31]:


l1[-3]


# In[38]:


l1.append(2)
print(l1)


# In[40]:


l1.insert(4, "durga")
print(l1)


# In[44]:


reverse=l1.reverse
print(l1)


# In[56]:


print(s3)


# In[58]:


print(type(l1))


# In[59]:


print(l1)


# #oops 

# In[61]:


class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks >= 40:
            return "Pass"
        return "Fail"
Student1= Student("Sakshi", 85)
print(Student1.name)
print(Student1.result())



# # decorators

# In[84]:


def login_required(func):
    def wrapper():
        print("Checking login...")
        func()
    return wrapper

@login_required
def dashboard():
        print("Welcome to Dashboard")


dashboard()


# In[ ]:




