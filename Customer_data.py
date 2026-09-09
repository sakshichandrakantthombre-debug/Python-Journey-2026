#!/usr/bin/env python
# coding: utf-8

# # Date: 08/09/2026

# # EDA

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r"C:\Users\user\Downloads\customer_shopping_data.csv")


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.describe(include="object")


# In[10]:


df.describe(include="object")


# # check missing values

# In[11]:


df.isnull().sum()


# # Percentage

# In[12]:


(df.isnull().sum()/len(df)) *100


# # Check duplicates

# In[13]:


df.duplicated().sum()


# # Check unique values

# df.nunique()

# ### for individual categorical columns

# In[14]:


df["gender"].unique()


# In[15]:


df["customer_id" ].unique()


# In[16]:


df["payment_method"].unique()


# ## Create Revenue columns

# #### This is very important for custokmer shopping analysis.

# In[17]:


df["revenue"]=df["quantity"]*df["price"]


# In[18]:


df


# In[19]:


df[["quantity","price","revenue"]].head()


# In[20]:


df[["quantity","price","revenue"]].tail()


# # Univariant Analysis

# ## Gender

# In[21]:


df["gender"].value_counts()


# In[22]:


sns.countplot(data=df, x="gender")
plt.title("Customer Distribution by Gender")
plt.show()


# # Category

# In[23]:


df["category"].value_counts()
plt.figure(figsize=(10,5))
sns.countplot(data=df,
x="category")
plt.xticks(rotation=45)
plt.title("Sales by Category")
plt.show()


# In[ ]:





# # Payment method

# In[24]:


sns.countplot(data=df,
x="payment_method")
plt.title("Payment Method Distribution")
plt.show()


# # Shopping mall

# In[25]:


plt.figure(figsize=(10,5))
sns.countplot(data=df,
x="shopping_mall")
plt.xticks(rotation=45)
plt.title("Customer by Shopping Mall")
plt.show()


# # Numerical Analysis

# ### Age distribution

# In[26]:


sns.histplot(data=df, x='age',
bins=20, kde=True)
plt.title("Age Distribution")
plt.show()


# ## Quantity

# In[27]:


sns.histplot(data=df,
x="quantity",bins=10, kde=True)
plt.title("Quantity Distribution")
plt.show()


# In[28]:


sns.histplot(data=df, x='price',
bins=30, kde=True)
plt.title("Price Distribution")
plt.show()


# ## Revenue

# In[29]:


sns.histplot(data=df, x='revenue',
bins=30, kde=True)
plt.title("revenue Distribution")
plt.show()


# In[30]:


sns.histplot(data=df, x='age',
bins=20, kde=True)
plt.title("Age Distribution")
plt.show()


# # Central Tendancy

# # mean

# In[31]:


df["age"].mean()


# # median

# In[32]:


df["age"].median()


# # mode

# In[33]:


df["age"].mode()


# In[34]:


print("Mean:", df["age"].mean())
print("median:",
df["age"].median())
print("Mode:", df["age"].mode()
[0])


# In[35]:


df["price"].mean()
df["quantity"].mean()
df["revenue"].mean()


# ## category_wise Revenue

# In[54]:


category_revenue =df.groupby("category")["revenue"].sum()
category_revenue


# # visualizations

# In[59]:


category_revenue.plot(kind="bar",figsize=(10,5)),plt.title("Revenue by Category"),plt.xlabel("Category"),plt.ylabel("Revenue"),plt.xticks(rotation=45)
plt.show()


# # Gender vs revenue

# In[63]:


gender_revenue =df.groupby("gender")["revenue"].sum()

gender_revenue


# In[64]:


df.columns


# In[65]:


print(df.columns.tolist())


# In[66]:


gender_revenue.plot(kind="bar")
plt.title("Revenue by Gender")
plt.ylabel("Revenue")
plt.show()


# # Gender x category

# In[67]:


gender_category=pd.pivot_table(
    df,
    values="revenue",
    index="category",
    columns="gender",
    aggfunc="sum"

)
gender_category


# In[69]:


plt.figure(figsize=(10,6))
sns.heatmap(gender_category,
annot=True, fmt=".0f")
plt.title("Revenue by Category and Gender")
plt.show()


# # Shopping Mall Analysis

# In[71]:


mall_revenue=df.groupby("shopping_mall")["revenue"].sum().sort_values(ascending=False)
mall_revenue


# mall_revenue.plot(kind="bar",figsize=(12,5))
# plt.title("Revenue by Shopping Mall")
# plt.ylabel("Revenue")
# plt.xticks(rotation=45)
# plt.show()

# ## Payment method vs revenue

# In[80]:


payment_revenue=df.groupby("payment_method")["revenue"].sum()
payment_revenue


# # Age Group Analysis

# In[82]:


bins=[0,18,25,35,45,55,100]
labels=[
    "Below 18",
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "55+"
]
df["age_group"]=pd.cut(
    df["age"],
    bins=bins,
    labels=labels
)



# In[83]:


bins


# In[84]:


df["age_group"].value_counts().sort_index()


#  ## Correlation Analysis

# In[85]:


numeric_df=df[["age","quantity","price","revenue"]]
numeric_df.corr()


# In[86]:


plt.figure(figsize=(8,6))
sns.heatmap(
     numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Matrix")
plt.show()


# # outliner Analysis

# In[87]:


sns.boxplot(data=df, x="price")
plt.title("Price Outliers")
plt.show()


# In[89]:


sns.boxplot(data=df, x="revenue")
plt.title("Revenue Outliers")
plt.show()


# # Top Customers

# In[94]:


top_customer=(
df.groupby("customer_id")
["revenue"]
.sum()
.sort_values(ascending=False)
.head(10)
)
top_customer


# # Top 10 invoices

# In[95]:


top_invoice =(
    df.groupby("invoice_no")
    ["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
top_invoice


# In[ ]:




