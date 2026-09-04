#!/usr/bin/env python
# coding: utf-8

# # Pandas_Operation_Practices

# #  02/09/2026

# # DataFrames

# In[1]:


import pandas as pd


# In[2]:


pd.DataFrame
pd.DataFrame


# In[3]:


emp_data = {
    "ids":[101,102,103,104,105],
    "name":["Suman","Raman","Thaman","Baman","Naman"],
    "salary":[25000,35000,55000,12000,34000],
    "dept":["IT","Sales","Marketting","BPO","IT"]
}


# In[4]:


emp_data


# In[5]:


type(emp_data)


# In[6]:


emp_data.items()


# In[7]:


emp_data.keys()


# In[8]:


df=pd.DataFrame(emp_data)


# In[9]:


df


# In[10]:


stu={"stu_id":[1,2,3,4,5],
    "stu_name":["vijay","raj","raju","aanand","abhi"],
    "dept_name":["DS","CS","IT","Mech","ENTC"]}


# In[11]:


stu


# In[12]:


stu_df=pd.DataFrame(stu)
stu_df


# In[13]:


df


# In[14]:


df.shape


# In[15]:


df.shape[1]


# In[16]:


df.shape[0]


# In[17]:


stu_df.shape


# In[18]:


stu_df.shape[1]


# In[19]:


df.info()


# In[20]:


df.info()


# In[21]:


stu_df.info()


# In[22]:


df.index


# In[23]:


stu_df.index


# In[24]:


df.columns


# In[25]:


stu_df.columns


# In[26]:


df.columns=["id1","name1","salary1","dept1"]


# In[27]:


df


# In[28]:


df.index=[100,101,102,103,104]


# In[29]:


df


# In[30]:


stu_df


# # DataFrame From  a List!!

# In[31]:


ids= [101, 102, 103, 104, 105]
name= ['Suman', 'Raman', 'Thaman', 'Baman', 'Naman']
salary= [25000, 35000, 55000, 12000, 34000]
dept= ['IT', 'Sales', 'Marketting', 'BPO', 'IT']


# In[32]:


type(name)
type(salary)
type(ids)


# In[33]:


df2=pd.DataFrame([ids,name,salary,dept])


# In[34]:


df2


# In[35]:


df2=pd.DataFrame([ids,name,salary,dept]).T
df2


# In[36]:


df2.columns=["ids","name","salary","dept"]


# In[37]:


df2


# In[38]:


df2.columns=["ids","name","salary","dept"]


# In[39]:


df2


# In[40]:


stu_1=[1,2,3]
stu_name=["vj","az","abhi"]
marks=[45,46,47]


# In[41]:


stu_df2=pd.DataFrame([stu_1,stu_name,marks]).T


# In[42]:


stu_df2


# In[43]:


stu_df2.columns=["stu_id","name","marks"]


# In[44]:


stu_df2


# In[45]:


id1 = [101,"suman",35000,"IT"]
id2 = [102,"raman",56000,"Sales"]
id3 = [103,"suman",80000,"marketting"]
id4 = [104,"baman",90000,"bpo"]


# In[46]:


a=pd.DataFrame([id1,id2,id3,id4],columns=["ids","name","salary","dept"])
a


# In[47]:


a.info()


# In[ ]:





# In[48]:


st=pd.read_csv(r"C:\Users\user\Downloads\50_Startups.csv")
st


# In[49]:


st.shape


# In[50]:


st.index


# In[51]:


st.info()


# In[52]:


st.columns


# In[53]:


st.head()


# # Read of CSV file

# In[54]:


import pandas as pd


# In[55]:


pd.read_csv(r"C:\Users\user\Downloads\Cars93.csv")


# In[56]:


car=pd.read_csv(r"C:\Users\user\Downloads\Cars93.csv")


# In[57]:


car


# In[58]:


car.info()


# In[59]:


car.columns


# In[60]:


car.shape


# In[61]:


car.index


# In[62]:


from warnings import filterwarnings
filterwarnings ("ignore")


# In[63]:


st.RND


# In[64]:


st[["RND"]].head()


# In[65]:


st[["RND"]].tail()


# In[66]:


st[["RND","PROFIT"]].head()


# In[67]:


st.head(1)


# # Subsetting

# In[68]:


st[["RND","MKT"]].head()


# In[69]:


st[0:12]


# In[70]:


st[0:-12][["STATE","PROFIT"]]


# In[71]:


st[8:12][["RND","PROFIT","STATE"]]


# In[72]:


st.loc[[2,4],["STATE","PROFIT"]]


# In[73]:


st.loc[[2,4],["STATE","PROFIT"]]


# In[74]:


df.iloc[3:5,2:]


# In[75]:


car.columns


# In[76]:


car.info()


# In[77]:


car.head()


# In[78]:


car.tail()


# In[79]:


car.index


# In[80]:


car.info()


# In[81]:


car.isnull().sum()


# In[82]:


car.isnull().sum()[car.isnull().sum()>0]


# In[83]:


car.columns


# # find out cars with mileage between 10 and 25 on highway

# In[84]:


car["MPG.highway"]


# In[85]:


f1=(car["MPG.highway"]>10) & (car["MPG.highway"]>25)


# In[87]:


car[f1]


# In[88]:


car[f1][["MPG.highway","Manufacturer"]]


# In[89]:


car.head(1)


# # Find out cars whose price is greater than 40

# In[90]:


a=car["Price"]>40


# In[91]:


a


# In[92]:


car[a]


# In[93]:


car["Price"].min()


# In[94]:


car["Price"].max()


# In[95]:


car["Price"].describe()


# # Find out car details whose manufacturer is infiniti

# In[96]:


car["Manufacturer"].unique()


# In[98]:


car[car["Manufacturer"]=="Infiniti"]


# # Find out models whose type belongs to Compact Size.

# In[99]:


car["Type"].unique()


# In[100]:


car[car["Type"]=="Compact"]


# In[101]:


car["Price"].nunique()


# # Find out cars which belong to sport type and are priced more than 25

# In[102]:


car["Type"].unique()


# In[103]:


a=(car["Type"]=="Sporty") & (car["Price"]>25)


# In[106]:


car[a]


# # Finf out cars which provided aribags to driver and passanger. Display manufacture, module anad in output.

# In[107]:


car["AirBags"].unique()


# In[108]:


car[car["AirBags"]=="Driver & Passenger"]


# # Find out cars whose luggage room > 15

# In[109]:


car.columns


# In[110]:


car["Luggage.room"].unique()


# In[114]:


car[car["Luggage.room"]>15][["Luggage.room","Manufacturer","Type"]]


# In[115]:


car.sort_values(by="Price",ascending=False)[["Price","Manufacturer"]]


# In[ ]:


car.sort_values(by=["Manufacturer","Price"])[[O]]

