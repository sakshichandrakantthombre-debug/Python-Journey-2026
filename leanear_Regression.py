#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import warnings
warnings.filterwarnings("ignore")


# In[4]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\Property_Price_Train.csv")


# In[5]:


lr=pd.read_csv(r"C:\Users\user\Desktop\MLA\Property_Price_Train.csv")
lr


# In[6]:


import pandas as pd


# In[7]:


print(lr.shape)
print(lr.head)
print(lr.tail)
print(lr.info)


# # Define X and Y

# In[8]:


x=lr.drop("Sale_Price",axis=1)
y=lr["Sale_Price"]
x


# In[9]:


y


# In[10]:


lr.isna().sum()


# ## Numerical columns fill with the medium

# In[11]:


lr["Lot_Extent"]=lr["Lot_Extent"].fillna(lr["Lot_Extent"].median())
lr


# ## Categorical  columns - fill with the mode

# In[12]:


lr.columns


# In[13]:


lr.isna().sum()


# In[14]:


x=lr.drop("Sale_Price",axis=1)
y=lr["Sale_Price"]


# In[15]:


x


# In[16]:


y


# In[17]:


print(lr.dtypes)


# In[18]:


print(type(lr))


# In[19]:


categorical_cols=lr.select_dtypes(include="object").columns
numerical_cols=lr.select_dtypes(exclude="object").columns

print("Categorical columns:")
print(categorical_cols)

print("\nNumerical columns:")
print(numerical_cols)


# In[20]:


lr


# In[21]:


print(x.shape)
print(x.dtypes.value_counts())


# In[22]:


print(y.shape)


# In[23]:


lr.duplicated().sum()


# In[24]:


df=lr.drop_duplicates()
df


# In[25]:


df.nunique()


# In[26]:


x=df.drop(["Sale_Price", "Id"],axis=1)
y=df["Sale_Price"]


# In[27]:


x


# In[28]:


y


# In[29]:


lr.isna().sum()


# In[30]:


df.isna().sum()[df.isna().sum()>0]


# # Categorical columns find out the missing values.

# In[31]:


cat_nan=x.select_dtypes(include="object").isna().sum()
print(cat_nan[cat_nan>0].sort_values(ascending=False))


# # find out the value of numerical only.

# In[34]:


num_nan=x.select_dtypes(exclude="object").isna().sum()
print(num_nan[num_nan>0].sort_values(ascending=False))


# In[36]:


x[categorical_cols]=x[categorical_cols].fillna("None")


# In[37]:


x[categorical_cols].isna().sum().sum()


# In[44]:


categorical_cols=x.select_dtypes(include="object").columns
numerical_cols=x.select_dtypes(exclude="object").columns


# In[45]:


x[categorical_cols]=x[categorical_cols].fillna("None")


# In[46]:


x[numerical_cols]=x[numerical_cols].fillna(x[numerical_cols].median())


# In[47]:


print(x.isna().sum().sum())


# In[53]:


print(x.columns.tolist())


# In[54]:


print([col for col in x.columns if "Sale" in col])


# In[55]:


print(x.shape)
print(y.shape)


# In[56]:


y=lr["Sale_Price"]
x=x.copy()
print(x.shape)
print(y.shape)


# In[57]:


categorical_cols=x.select_dtypes(include="object").columns
print(categorical_cols)
print(len(categorical_cols))


# # Encoding

# In[58]:


x=pd.get_dummies(x,columns=categorical_cols,drop_first=True) ## using getdummies for the categorical data o & 1 convert into numeircal.
print(x.shape)


# In[61]:


print(x.dtypes.value_counts())


# In[62]:


print(x.isna().sum().sum())


# # Flow of the  data segragation and Data cleanings.
# ### Missing values
# ### Cleaned
# ### Target
# ### Encoding
# ### Train/Test Split
# ### Linear Regression Model

# In[67]:


print(x.shape)


# In[ ]:




