#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('python --version')


# In[4]:


import warnings
warnings.filterwarnings("ignore")


# In[5]:


import pandas as pd


# # series

# In[6]:


t=(10,11,12)
d=pd.Series(t)
d


# In[7]:


type(t)


# In[8]:


type(d)


# In[9]:


l1=[45,78,56,445,78]
d=pd.Series(l1)
d


# In[10]:


type(l1)


# In[11]:


type(d)


# In[12]:


d={'a':1, 'b':2, 'c':3, 'd':4}
d


# In[13]:


d.keys()


# In[14]:


d['c']


# In[15]:


b=pd.Series(d)
b


# In[16]:


import numpy as np


# In[17]:


l1=list(range(12))
l1


# In[18]:


a=np.arange(10)
a


# In[20]:


d=pd.Series(np.arange(20))
d[5:15:2]


# In[23]:


a=pd.Series(list(range(20+1)))
a[2:5]


# # DataFrame

# In[24]:


data=[['abc',1],['def',2],[3,3],['hij'],['klm',5],[6,"vj"]]
type(data)


# In[25]:


a=pd.DataFrame(data)
a


# In[26]:


d=pd.DataFrame(data,columns=['name','marks'],index=['A','B','c','D','E','F'])
d


# In[28]:


d1={"name":["vijay","raju","raj"],"age":[25,26,27]}
d1.keys()


# In[29]:


d1.values()


# In[30]:


d2=pd.DataFrame(d1)
d2


# In[31]:


data={'name':['a','b','c','d','e','f'],'age':[45,12,48,56,45,36]}
data.keys()


# In[32]:


d=pd.DataFrame(data)
d


# In[33]:


d.columns=['Candidate','Age_in_years']
d


# In[34]:


d.rename({2:"num1"},axis=0,inplace=True)
d


# In[35]:


d.rename({'Age_in_years':"Age"},axis=1,inplace=True)
d


# In[1]:


get_ipython().system('python --version')


# In[2]:


import warnings
warnings.filterwarnings("ignore")


# In[3]:


pwd


# In[6]:


train=pd.read_csv(r"C:\Users\user\Desktop\MLA\4train.csv")
train


# In[7]:


data=pd.read_csv('4train.csv')
data


# In[8]:


type(data)


# In[9]:


data.head()


# In[10]:


data.head(1)


# In[11]:


data.tail()


# In[13]:


data.tail(2)


# In[14]:


data.columns


# In[15]:


data['Pclass'].unique()


# In[18]:


data['Pclass'].nunique()


# In[19]:


data['Name'].unique()


# In[20]:


data['Name'].nunique()


# In[21]:


data.shape


# In[22]:


data.shape[0]


# In[23]:


data.info()


# In[24]:


data.columns


# In[25]:


data[['Age']]


# In[26]:


data[['Age','Name']]


# In[27]:


data.describe()


# In[28]:


## describe with 'O' statisatics of categorical variables.
data.describe(include='O')


# In[29]:


data.describe(include=["object"])


# In[30]:


data.loc[data['Age']==80]


# In[32]:


data.loc[(data['Sex']=='male') & (data['Age']>40)]                    


# In[33]:


data.columns


# In[34]:


data.Sex.unique()


# In[35]:


data.loc[(data['Sex']=='female') & (data['Pclass']==1)] [["Sex","Pclass"]]


# In[39]:


data.loc[(data['Sex']=='female') & (data['Pclass']==1) & (data['Survived']==0)][["Sex","Pclass","Survived"]]


# In[40]:


import numpy as np


# In[41]:


data.iloc[np.where(data['Age']==80)]


# In[42]:


data.iloc[np.where( (data['Sex']=='male') & (data['Survived']==1) )][["Sex","Survived"]].head()


# In[43]:


data.Pclass.value_counts()


# In[44]:


data.Embarked.value_counts()


# In[45]:


data['Age'].isnull().sum()


# In[46]:


data.isnull().sum()


# In[51]:


data.isnull().sum()[data.isnull().sum()>0]


# In[52]:


pd.set_option('display.max_rows',None) ## displaying all rows


# In[53]:


data


# In[54]:


pd.reset_option('display.max_rows',None)


# In[55]:


data


# In[56]:


pd.set_option('display.max_columns',None)


# In[57]:


data


# In[58]:


d1=data[['Survived','Age','Sex']]


# In[59]:


d1


# In[60]:


d1[15:30]


# In[61]:


data.iloc[15:30,2:7]


# In[62]:


data.loc[15:30,[("Name")]]


# In[ ]:




