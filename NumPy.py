#!/usr/bin/env python
# coding: utf-8

# # NumPy_Array_and_Operation_1

# In[13]:


import numpy as np


# In[14]:


arr1=np.array([])
arr1


# In[15]:


type(arr1)


# In[16]:


l1=[]
l1


# In[17]:


my_list=[1,2,3,4,5]
print(my_list)
print(type(my_list))


# In[18]:


a=np.array(my_list)
a


# In[19]:


type(a)


# In[20]:


my_list+[2,3]


# In[21]:


a.ndim


# In[22]:


a.size


# In[23]:


a.shape


# # Arrays

# In[24]:


my_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # list of lists
my_matrix


# In[25]:


my_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # list of lists
type(my_matrix)


# In[26]:


b=np.array(my_matrix)
b


# In[27]:


type(b)


# In[28]:


b.ndim


# In[29]:


b.size


# In[30]:


b.shape


# In[31]:


b.dtype


# In[32]:


type(b)


# In[33]:


arr1=np.array([[[1,2,3],[4,5,6]],   [[7,8,9],[10,11,12]]])
arr1


# In[34]:


arr1.shape


# In[35]:


arr1.ndim


# In[36]:


arr1


# In[37]:


arr1[1][1][1]


# In[38]:


np.mean([1,2,3,45])


# In[39]:


l1=[1,2,3,4,45]


# In[40]:


import pandas as pd
l1=[1,2,3,4,45]
d1=pd.DataFrame(l1)
d1.mean()


# # Built-in Methods

# In[41]:


arr2=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
arr2


# In[42]:


arr2.shape


# In[43]:


arr2.reshape(-1)


# In[44]:


desc_arr=np.sort(arr2.reshape(-1))[::-1]
desc_arr


# # arange

# # Return evenly spaced values within a given innteval.

# In[45]:


list(range(10+1))


# In[46]:


np.arange(15)


# In[47]:


np.arange(5,15)


# In[48]:


np.arange(0,100,2)


#  Zeros and ones

# In[49]:


np.zeros(3)


# In[50]:


np.zeros((5,5))


# In[51]:


np.ones(3)


# In[52]:


np.ones((2,5,5)) # Genarates arry of 3 dimensions where all elements are 1


# # linespace

# In[53]:


np.linspace(1,15)


# In[54]:


np.linspace(5,25,10,retstep=True)


# In[55]:


np.linspace(0,200,10)


# In[56]:


np.linspace(0,25, retstep=True)


# # eye

# # creates an identity matrix

# In[57]:


np.eye(7)


# In[58]:


# Create an eye from a zeroes array


# #Broadcasting in an array

# In[59]:


big_one=np.ones((3,4))
print(big_one)


# In[60]:


big_one.dtype


# In[61]:


type(big_one)


# In[62]:


big_one*3


# In[63]:


bigger_one=big_one*6-2
bigger_one


# In[64]:


big_one


# In[65]:


bigger=np.array(big_one*5-3,dtype='int')
print(bigger)


# In[66]:


bigger.dtype


# In[67]:


type(bigger)


# In[68]:


bigger.shape


# In[69]:


bigger.size


# In[70]:


bigger//bigger


# In[71]:


bigger


# In[72]:


arr1


# In[73]:


1/arr1[1:]


# In[74]:


1/arr1[0:]


# In[1]:


arr1=np.arange(20)
1/arr1


# In[76]:


import warnings
warnings.filterwarnings("ignore")


# In[77]:


arr=np.arange(4)
arr


# In[78]:


arr+arr


# In[79]:


arr


# In[80]:


arr**arr


# # Use of Copy function

# In[81]:


arr1=np.arange(0,19)
arr1


# In[82]:


arr1[7]=100
arr1


# In[83]:


arr1


# In[84]:


arr2


# In[85]:


arr2=arr1 # not recommended
arr2


# In[86]:


array=([  0,   1,   2,   3,   4,   5,   6, 100,   8,   9,  10,  11,  12,
        13,  14,  15,  16,  17,  18])
array










# In[87]:


arr3=arr1.copy()


# In[88]:


arr3


# In[89]:


print(arr3)
print(arr1)


# In[90]:


arr3[10:]=100
arr3


# In[91]:


arr1 # copy function retains the original. copy creates a backup array.


# # Random number generation
# Numpy also hasa lots of ways the

# In[92]:


np.random.rand()


# In[93]:


np.random.rand(10)


# In[94]:


np.random.rand(5,2)


# In[95]:


arr1=np.random.randn(50)
arr1


# In[96]:


np.mean(arr1)


# In[97]:


np.median(arr1)


# In[98]:


np.std(arr1)


# # randint

# In[99]:


np.random.randint(1,100)


# In[100]:


np.random.randint(1,7)


# In[101]:


arr2=np.random.randint(1,100,20)


# In[102]:


arr2


# In[103]:


arr2.max()


# In[104]:


arr2.min()


# In[105]:


arr2.argmax() # find the index position argmax


# In[106]:


arr2.argmin()


# In[107]:


ranarr=np.random.randint(0,100,10)
ranarr


# In[108]:


ranarr.argmax()


# In[109]:


ranarr.argmin()


# In[110]:


ranarr.min()


# In[111]:


arr=np.arange(10,100,5)
arr


# In[112]:


len(arr)


# In[113]:


arr[-1]


# In[114]:


arr[9]


# In[115]:


arr[1:11:2]


# # Filtering

# In[116]:


arr=np.array([1,2,1010,4,108,71,610])
arr


# In[119]:


arr[5]


# In[120]:


arr[2]


# In[121]:


arr[np.where(arr>100)]


# In[123]:


arr


# In[124]:


np.where(arr==100)


# In[125]:


arr_2d=np.array(([1,2,3],[12,15,18],[64,96,128]))
arr_2d


# In[126]:


arr_2d[2,1]


# In[127]:


l1=[1,2,3,4,5]


# In[128]:


l1[:3]

arr_2d
# In[ ]:




