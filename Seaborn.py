#!/usr/bin/env python
# coding: utf-8

# # Date: 07/09/2026

# In[8]:


import warnings
warnings.filterwarnings("ignore")


# In[9]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[10]:


# getting the built-in datasets of seanorn.
sns.get_dataset_names()


# In[13]:


# loading datasets
df= sns.load_dataset("iris")


# In[14]:


df


# In[17]:


df.species.unique()


# In[18]:


df.species.value_counts()


# In[19]:


df.head(1)


# In[26]:


sns.lineplot(x='sepal_length', y='sepal_width', data=df, ci=65)
plt.show()


# In[29]:


sns.lineplot(x='sepal_length', y='sepal_width', data=df,hue='species', ci=None)
plt.show()


# In[30]:


sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue='species')
plt.title("Scatter plot")
plt.show()


# In[33]:


sns.barplot(x='species', y='sepal_length', data=df)
plt.show()


# In[34]:


sns.countplot(x='species', data=df)
plt.show()


# In[35]:


df


# In[36]:


sns.boxplot(x='sepal_width',data=df)
plt.show()


# In[37]:


sns.boxplot(x='species', y='sepal_width', data=df)
plt.show()


# In[38]:


# visualized the density of the data 
sns.violinplot(x='species', y='sepal_width', data=df)
plt.show()


# In[39]:


#It is used for striplot:
sns.stripplot(x='species', y='petal_width', data=df)
plt.show()


# In[40]:


# distributed data observation.
sns.histplot(x='petal_width', data=df)
plt.show()


# In[42]:


sns.histplot(x='petal_width', data=df,hue='species',kde=True)## hue for the subcategory
plt.show()


# In[45]:


sns.distplot(df['petal_width'],color="g") # ,hist=False, kde=False
plt.show()


# In[47]:


sns.pairplot(data=df, hue='species')
plt.show()


# In[48]:


sns.catplot(x='sepal_length', data=df, kind='violin')## categorical plot
plt.show()


# In[49]:


sns.catplot(x='species', y='sepal_length', data=df, kind='swarm')
plt.show()


# In[50]:


sns.catplot(x='petal_length',y='species',data=df)
plt.show()


# In[51]:


tc=df.select_dtypes(include=['number']).corr()
print(tc)


# In[52]:


plt.figure(figsize=(7,8))
sns.heatmap(tc,annot=True,cmap='coolwarm') # annot denote the numbers
plt.title('Correlation Heatmap')
plt.show()


# In[56]:


sns.heatmap(tc, annot =True)
plt.show()


# In[ ]:




