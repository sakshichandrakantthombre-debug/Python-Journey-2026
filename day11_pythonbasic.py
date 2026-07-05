#!/usr/bin/env python
# coding: utf-8

# In[21]:


#1) Write a recursive function to calculate the sum of numbers from 0 to 10
sum=0
for i  in range(0,11):
        sum=sum+i
        print(sum, end="  ")


# In[25]:


#2)Return the largest item from the given list
lst1=[2, 3, 5, 6, 7,9, 20, 50]
print(max(lst1))


# In[18]:


#3)Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both,
#and if the salary is missing in function call it should show it as 9000
def showEmployee(name, salary=9000):
    print("Employee Name:", name)
    print("Salary:", salary)

showEmployee("Sakshi")


# In[24]:


#4) Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print("First color:",color_list[0])
print("last color:", color_list[-1])


# In[32]:


#5)Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a
#tuple with those numbers
numbers=input("Enter the commo_separated numbers:")
list_data = numbers.split(", ")
tuple_data = tuple(list_data)
print("List:", list_data)
print("Tuple:", tuple_data)




# In[37]:


#6)Display the numbers in reverse from 100 to 1
for i in range(100, 0, -1):
    print(i, end=" ")


# In[4]:


#7)print the fruits append method:
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)


# In[13]:


#8)From the below nested dictionary, pick the word "Bangalore".
d = {'1':'One','2':[1,{'Two':['Ch','Cbe','Salem',{'Place':[5,6,7,'Bangalore']}]}]}
print(d['2'] [1]['Two'][3]['Place'][3])


# In[14]:


#9)calling the function:
def fun():
    print("Welcome to  new city")
fun()


# In[22]:


# 10) functions:
def evenOdd(x):
    if(x%2 == 0):
        return "Even"
    else:
        return "Odd"
print(evenOdd(16))
print(evenOdd(7))


# In[ ]:




