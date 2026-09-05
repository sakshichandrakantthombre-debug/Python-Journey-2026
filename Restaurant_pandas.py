#!/usr/bin/env python
# coding: utf-8

# # Date 05/09/2026

# # Pandas Introduction

# pandas is an open-source Python library used for data manipulation, analysis and cleaning. It provides fast and flexible tools to work with tabular data, similar to spreadsheets or SQL tables.
# 
# Pandas is used in data science and analytics due to its integration with libraries such as:

# In[1]:


import pandas as pd


# In[2]:


import numpy as np

data = np.array(['g', 'e', 'e', 'k', 's'])
s = pd.Series(data)
print("Pandas Series:")
print(s)


# In[3]:


import pandas as pd 

df = pd.DataFrame() 
print(df)
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 

df = pd.DataFrame(lst) 
print(df)


# In[4]:


type(lst)


# In[5]:


df.shape


# In[6]:


df.size


# In[7]:


df


# In[8]:


dataframe = pd.read_csv(r"C:\Users\user\Downloads\Zomato_Dataset.csv")
print(dataframe.head())


# In[9]:


dataframe


# In[10]:


dataframe.head()


# In[11]:


dataframe.tail()


# In[12]:


dataframe.info()


# ### Checking for missing or null values to identify any data gaps.

# In[13]:


import pandas as pd
import numpy as np


# # Missing Values

# In[18]:


dataframe.isnull().sum()


# In[19]:


(dataframe.isnull().sum()/len(dataframe) *100).sort_values(ascending=False)


# #  Duplicate Rows

# In[20]:


dataframe.duplicated().sum()


# In[21]:


dataframe[dataframe.duplicated()]


# In[22]:


dataframe.describe()


# In[24]:


dataframe[['Price_range','Votes','Average_Cost_for_two','Rating']].describe()


# ## Cateforical Analysis

# In[25]:


dataframe['City'].nunique()


# In[26]:


dataframe['City'].value_counts().head(10)


# In[29]:


dataframe['Cuisines'].value_counts().head(10)


# In[30]:


dataframe['City'].value_counts().head(10) ## city counts


# In[31]:


dataframe['RestaurantName'].value_counts().head(10)


# # Analysis the data from Pandas of EDA 

# In[33]:


# Missing values
dataframe.isnull().sum()


# In[35]:


dataframe.duplicated().sum()


# # Columns data types

# In[36]:


dataframe.dtypes


# In[37]:


dataframe.nunique().sort_values()


# ### Basic Statistics

# In[38]:


dataframe.describe(include='all')


# In[41]:


dataframe[['RestaurantName',
           'Rating']].sort_values(
by='Rating',ascending=False
).head(10)


# # Average votes by price Range

# In[42]:


dataframe[['Price_range',
           'Votes']].mean().sort_values(
ascending=False)


# In[ ]:




