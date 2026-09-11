#!/usr/bin/env python
# coding: utf-8

# # Date 05/09/2026

# # Pandas Introduction

# pandas is an open-source Python library used for data manipulation, analysis and cleaning. It provides fast and flexible tools to work with tabular data, similar to spreadsheets or SQL tables.
# 
# Pandas is used in data science and analytics due to its integration with libraries such as:

# In[35]:


import pandas as pd


# In[36]:


import numpy as np

data = np.array(['g', 'e', 'e', 'k', 's'])
s = pd.Series(data)
print("Pandas Series:")
print(s)


# In[37]:


import pandas as pd 

df = pd.DataFrame() 
print(df)
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 

df = pd.DataFrame(lst) 
print(df)


# In[38]:


type(lst)


# In[39]:


df.shape


# In[40]:


df.size


# In[41]:


df


# In[42]:


dataframe = pd.read_csv(r"C:\Users\user\Downloads\Zomato_Dataset.csv")
print(dataframe.head())


# In[43]:


dataframe


# In[44]:


dataframe.head()


# In[45]:


dataframe.tail()


# In[46]:


dataframe.info()


# ### Checking for missing or null values to identify any data gaps.

# In[47]:


import pandas as pd
import numpy as np


# # Missing Values

# In[48]:


dataframe.isnull().sum()


# In[49]:


(dataframe.isnull().sum()/len(dataframe) *100).sort_values(ascending=False)


# #  Duplicate Rows

# In[50]:


dataframe.duplicated().sum()


# In[51]:


dataframe[dataframe.duplicated()]


# In[52]:


dataframe.describe()


# In[53]:


dataframe[['Price_range','Votes','Average_Cost_for_two','Rating']].describe()


# ## Cateforical Analysis

# In[54]:


dataframe['City'].nunique()


# In[55]:


dataframe['City'].value_counts().head(10)


# In[56]:


dataframe['Cuisines'].value_counts().head(10)


# In[57]:


dataframe['City'].value_counts().head(10) ## city counts


# In[58]:


dataframe['RestaurantName'].value_counts().head(10)


# # Analysis the data from Pandas of EDA 

# In[59]:


# Missing values
dataframe.isnull().sum()


# In[60]:


dataframe.duplicated().sum()


# # Columns data types

# In[61]:


dataframe.dtypes


# In[62]:


dataframe.nunique().sort_values()


# ### Basic Statistics

# In[63]:


dataframe.describe(include='all')


# In[64]:


dataframe[['RestaurantName',
           'Rating']].sort_values(
by='Rating',ascending=False
).head(10)


# # Average votes by price Range

# In[65]:


dataframe[['Price_range',
           'Votes']].mean().sort_values(
ascending=False)


# In[67]:


dataframe.duplicated().sum()


# In[69]:


dataframe.isnull().sum()


# In[71]:


dataframe.shape


# In[72]:


dataframe['Rating'].mean()


# In[73]:


dataframe['Rating'].describe()


# In[77]:


City_rating=(
dataframe.groupby('City')['Rating']
.mean()
.sort_values(ascending=False)
)
City_rating.head(10)


# 
# 
# # VISUALIZATION DATA ANALYSIS FOR THE FIND THE INSIGHTS

# In[1]:


import matplotlib.pyplot as plt


# In[ ]:




