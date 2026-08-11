#!/usr/bin/env python
# coding: utf-8

# # profit and loss python program 

# In[3]:


'''cp=750
sp=900
profit %=20% ?'''
cp=750
sp=900
profit=sp-cp
profit_percent=(profit/cp)*100
print(profit)
print(profit_percent)



# In[4]:


''' cp=1500, Loss=18%
sp=1230'''
cp=1500
loss=18
sp=cp*(1-loss/100)
print(sp)


# In[5]:


'''sp=1840, profit=15%
cp=1600'''
sp=1840
profit=15
cp=sp/(1+profit/100)
print(cp)


# In[6]:


''' sp=1530
loss=15
cp=1800'''
sp=1530
loss=15
cp=sp/(1-loss/100)
print(cp)


# In[7]:


''' Take CP and Profit % as input from the user and calculate the Selling Price.'''

cp=float(input("Enter the cost Price: "))
profit_percent=float(input("Enter profit %:"))
sp=cp*(1+profit_percent /100)
print("Selling Price:", sp)


# In[8]:


cp=500
sp=650
profit=sp-cp
profit_percent=(profit/cp)*100
print("Profit:", profit)
print("Profit %:", profit_percent)


# In[9]:


cp=2000
profit_percent=25
sp=cp*(1+profit_percent/100)
print("Selling Price:",sp)


# In[10]:


# target profit

cp=5000
profit_percent=25
sp=cp*(1+profit_percent/100)
print("Selling Price:", sp)


# In[11]:


# loss to profit
sp_loss=1600
loss=20
profit=25
cp=sp_loss/(1-loss/100)
new_sp=cp*(1+profit/100)
print("Cost Price", cp)
print("Selling Price for 25% Profit:", new_sp)


# In[12]:


# profit + Discount
cp=4000
profit=25
discount=10
sp=cp*(1+profit/100)
mp=sp/(1-discount/100)
print("Selling Price:", sp)
print("Marked Price:", mp)


# In[ ]:




