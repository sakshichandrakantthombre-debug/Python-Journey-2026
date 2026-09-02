#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('python --version')


# In[7]:


import warnings
warnings.filterwarnings("ignore")


# In[8]:


import pandas as pd


# # series

# In[9]:


t=(10,11,12)
d=pd.Series(t)
d


# In[10]:


type(t)


# In[11]:


type(d)


# In[12]:


l1=[45,78,56,445,78]
d=pd.Series(l1)
d


# In[13]:


type(l1)


# In[14]:


type(d)


# In[15]:


d={'a':1, 'b':2, 'c':3, 'd':4}
d


# In[16]:


d.keys()


# In[17]:


d['c']


# In[18]:


b=pd.Series(d)
b


# In[19]:


import numpy as np


# In[20]:


l1=list(range(12))
l1


# In[21]:


a=np.arange(10)
a


# In[22]:


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


# In[27]:


d1={"name":["vijay","raju","raj"],"age":[25,26,27]}
d1.keys()


# In[28]:


d1.values()


# In[29]:


d2=pd.DataFrame(d1)
d2


# In[30]:


data={'name':['a','b','c','d','e','f'],'age':[45,12,48,56,45,36]}
data.keys()


# In[31]:


d=pd.DataFrame(data)
d


# In[32]:


d.columns=['Candidate','Age_in_years']
d


# In[33]:


d.rename({2:"num1"},axis=0,inplace=True)
d


# In[34]:


d.rename({'Age_in_years':"Age"},axis=1,inplace=True)
d


# In[35]:


get_ipython().system('python --version')


# In[36]:


import warnings
warnings.filterwarnings("ignore")


# In[37]:


pwd


# In[38]:


train=pd.read_csv(r"C:\Users\user\Desktop\MLA\4train.csv")
train


# In[39]:


data=pd.read_csv('4train.csv')
data


# In[40]:


type(data)


# In[41]:


data.head()


# In[42]:


data.head(1)


# In[43]:


data.tail()


# In[44]:


data.tail(2)


# In[45]:


data.columns


# In[46]:


data['Pclass'].unique()


# In[47]:


data['Pclass'].nunique()


# In[48]:


data['Name'].unique()


# In[49]:


data['Name'].nunique()


# In[50]:


data.shape


# In[51]:


data.shape[0]


# In[52]:


data.info()


# In[53]:


data.columns


# In[54]:


data[['Age']]


# In[55]:


data[['Age','Name']]


# In[56]:


data.describe()


# In[57]:


## describe with 'O' statisatics of categorical variables.
data.describe(include='O')


# In[58]:


data.describe(include=["object"])


# In[59]:


data.loc[data['Age']==80]


# In[60]:


data.loc[(data['Sex']=='male') & (data['Age']>40)]                    


# In[61]:


data.columns


# In[62]:


data.Sex.unique()


# In[63]:


data.loc[(data['Sex']=='female') & (data['Pclass']==1)] [["Sex","Pclass"]]


# In[64]:


data.loc[(data['Sex']=='female') & (data['Pclass']==1) & (data['Survived']==0)][["Sex","Pclass","Survived"]]


# In[65]:


import numpy as np


# In[66]:


data.iloc[np.where(data['Age']==80)]


# In[67]:


data.iloc[np.where( (data['Sex']=='male') & (data['Survived']==1) )][["Sex","Survived"]].head()


# In[68]:


data.Pclass.value_counts()


# In[69]:


data.Embarked.value_counts()


# In[70]:


data['Age'].isnull().sum()


# In[71]:


data.isnull().sum()


# In[72]:


data.isnull().sum()[data.isnull().sum()>0]


# In[73]:


pd.set_option('display.max_rows',None) ## displaying all rows


# In[74]:


data


# In[75]:


pd.reset_option('display.max_rows',None)


# In[76]:


data


# In[77]:


pd.set_option('display.max_columns',None)


# In[78]:


data


# In[79]:


d1=data[['Survived','Age','Sex']]


# In[80]:


d1


# In[81]:


d1[15:30]


# In[82]:


data.iloc[15:30,2:7]


# In[83]:


data.loc[15:30,[("Name")]]


# In[84]:


dff=data.loc[data['Sex']=='female']
dff


# In[85]:


dff.shape


# In[86]:


dff.Survived.value_counts()


# In[87]:


dff.Age.mean()


# In[88]:


df1=data.loc[(data['Age']>65)]


# In[89]:


df1


# In[90]:


data.loc[(data['Sex']=='female') | (data['Age']<38)]


# In[91]:


d1


# In[92]:


data["Salary"]=35000
data


# In[93]:


data['DS']='Data Science'
data.head()


# In[94]:


data.drop(['Salary'],axis=1,inplace=True) ## drop the column.


# In[95]:


data.drop(['DS'],axis=1,inplace=True)


# In[96]:


data.head(3)


# In[97]:


data.drop(4,axis=0,inplace=True)
data.head(5)


# In[98]:


new_data=data.copy()


# In[99]:


new_data


# In[100]:


data.columns


# In[101]:


data.drop([5,6],axis=0,inplace=True)


# In[102]:


data.head()


# In[107]:


data["Pclass"].value_counts()


# In[108]:


data.sort_values('Pclass')


# In[109]:


data.sort_values('Pclass',ascending=False)


# In[110]:


data.sort_values('Pclass',ascending=False,ignore_index=True)


# In[112]:


data.sort_values(by=['Age','Pclass'],ascending=[1,0])


# In[113]:


cat=data.select_dtypes(include="object")
cat.head(1)


# In[114]:


con=data.select_dtypes(exclude="object")
con.head(1)


# In[115]:


data.Pclass.value_counts()


# In[116]:


data.groupby(data['Pclass']).count()


# In[117]:


data.groupby(['Sex','Pclass']).max("Fare")


# In[ ]:





# In[118]:


data.groupby(['Pclass','Sex']).max("Fare")


# In[ ]:


#data.groupby(data['Sex']).mean()


# In[119]:


data.groupby('Sex').mean(numeric_only=True)[["Pclass","Age"]]


# In[120]:


data.groupby(data["Pclass"]).agg({"Fare":["min","max","sum","count","mean"]})


# In[122]:


data.groupby(data["Pclass"]).agg({"Fare":["max","min"],"Age":["min"]})


# In[123]:


data['Age']=data.Age.astype('float16')


# In[124]:


data.info()


# In[126]:


data['Fare']=pd.to_numeric(data.Fare,downcast='float')


# In[127]:


data.info()


# In[ ]:




