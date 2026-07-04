#!/usr/bin/env python
# coding: utf-8

# # functool
# functool is built in python module that provided tools to make
# working with functions easier and more powerful.
# 
# -reuse function
# -optimize performance
# -simplify code
# - write cleaner programs

# In[2]:


import functools


# In[4]:


from functools import reduce
number=[1, 2, 3, 4, 5]
result=reduce(lambda x,y: x+y, number)
print(result)


# In[9]:


from functools import reduce
number=[1, 2, 3, 4, 5]
result=reduce(lambda x,y: x*y, number)
print(result)


# In[12]:


from functools import reduce
number=[1, 2, 3, 4, 5]
result=reduce(lambda x,y: x%y, number)
print(result)


# In[13]:


from functools import reduce
number=[1, 2, 3, 4, 5]
result=reduce(lambda x,y: x/y, number)
print(result)


# In[17]:


from functools import reduce
number=[1, 2, 3, 4, 5]
reciprocal=reduce(lambda x,y: 1/x, number)
print(reciprocal)


# In[18]:


from functools import reduce
number=[1, 2, 3, 4, 5]
result=reduce(lambda x, y: x if x<y else y, number)
print(result)


# In[19]:


from functools import reduce
number=[1, 2, 3, 4, 5]
result=reduce(lambda x, y: x if x>y else y, number)
print(result)


# In[23]:


from functools import reduce
words=["pyhon", " ", "us", " ", "easy"]
result=reduce(lambda x,y: x+y, words)
print(result)


# In[24]:


from functools import reduce
words=["My", " ", "is", " ", "easy"]
result=reduce(lambda x,y: x+y, words)
print(result)


# In[27]:


from functools import reduce
number=[1, 2, 3, 4, 5]
result=reduce(lambda x,y: x-y, number)
print(result)


# In[ ]:




