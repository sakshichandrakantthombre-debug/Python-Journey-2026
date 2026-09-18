#!/usr/bin/env python
# coding: utf-8

# # Unsupervised Learning 

# # K-Means

# In[1]:


#  Kmeans----> Determines the best value for K center point or centroids by an iterative process
# steps to be followed --> unsupervised model

#data import
#data cleaning-->null,replace
#no Sampling

#from sklearn.cluster import KMeans
#kmeans_mall=KMeans( n_clusters=4)----> 4= random cluster

#kmeans_mall.fit(mall)
#kmeans_mall.labels_ ------------------------------------------>this gives the lables for each records
#len(kmeans_mall.labels_)
#pd.DataFrame(kmeans_mall.labels_).value_counts()----------------->count in each cluster
#cluster_center=pd.DataFrame(kmeans_mall.cluster_centers_)
#cluster_center------------------------------------------------> center of each cluster
#kmeans_mall.score(mall)

#ssd=[]
#for k in range(1,12):
#    kmeans_mall=KMeans( n_clusters=k)
#    kmeans_mall.fit(mall)
#    score=kmeans_mall.score(mall)
#    ssd.append(score)
#    print('value of k is ',k)---------------------------------> calculated cluster

#ssd=np.abs(ssd)
#ssd

#plt.figure(figsize=(12,10))
#plt.plot(list(range(1,12)),ssd,marker='*')
#plt.grid()
#plt.xlabel('no of cluster')
#plt.ylabel('ssd')
#plt.title('elbow plot of mall')---------------> elbow plot

#ssd=np.round(ssd)
#l1=ssd
#l1

#l2=[]
#for i in range(len(l1)-1):
#    res = ((l1[i] - l1[i + 1] )/ l1[i]*100)
#    l2.append(np.abs(res))
#l2

#from sklearn.cluster import KMeans
#kmeans_mall=KMeans(   n_clusters=6)------------------> taken calculated cluster
#kmeans_mall.fit(mall)
#kmeans_mall.labels_
#len(kmeans_mall.labels_)
#pd.DataFrame(kmeans_mall.labels_).value_counts()----------->count in each cluster
#mall['cluster_name']=kmeans_mall.labels_
#mall

#colormap=np.array(['red','green','blue','black','yellow','purple'])
#plt.figure(figsize=(12,10))
#plt.scatter(mall.Age,mall.Spendingscore ,c=colormap[kmeans_mall.labels_])
#plt.show()



# To be taken as note
# 1) data should be numerical variables only
# 2) first take randam cluster -->4
# 3) then take calculated cluster -->6
# 4) elbow plot --> siddenly decrise and remain stable chose that cluster
# 5) size of cluster should be in between 1 to 10


# In[2]:


import pandas as pd


# In[3]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd


# In[4]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\mall_kmeans.csv")


# In[5]:


mall=pd.read_csv(r"C:\Users\user\Desktop\MLA\mall_kmeans.csv")


# In[6]:


mall


# In[7]:


mall=mall.drop(['CustomerID'],axis=1)


# In[8]:


mall


# In[9]:


mall.rename(columns={'Annual Income (k$)':'Anuincome','Spending Score (1-100)':'spendingscore'},inplace=True)


# In[10]:


mall



# In[11]:


mall.isnull().sum()[mall.isnull().sum()>0]


# In[12]:


mall.Genre.value_counts()


# In[13]:


mall.Genre.value_counts()


# In[14]:


mall.head()


# In[15]:


from sklearn.cluster import KMeans
kmean_mall=KMeans(n_clusters=4)


# In[16]:


mall.Genre.replace({'Female':0,'Male':1},inplace=True)


# In[17]:


mall.head()


# In[18]:


from sklearn.cluster import KMeans
kmean_mall=KMeans(n_clusters=4)


# In[19]:


kmean_mall.fit(mall)


# In[20]:


kmean_mall.labels_


# In[21]:


len(kmean_mall.labels_)


# In[22]:


pd.DataFrame(kmean_mall.labels_).value_counts()


# In[23]:


cluster_center=pd.DataFrame(kmean_mall.cluster_centers_)


# In[24]:


cluster_center


# In[26]:


cluster_center.columns=mall.columns


# In[27]:


cluster_center


# In[28]:


kmean_mall.score(mall)


# In[29]:


ssd=[]
for k in range(1,12):
    kmean_mall=KMeans(n_clusters=k)
    kmean_mall.fit(mall)
    score=kmean_mall.score(mall)
    ssd.append(score)
    print("Value of k is: ",k)


# In[30]:


import matplotlib.pyplot as plt


# In[31]:


import numpy as np
ssd=np.abs(ssd)


# In[32]:


plt.figure(figsize=(10,6))
plt.plot(list(range(1,12)),ssd,marker='*')
plt.grid()
plt.title("Elbow plot on mall data")
plt.xlabel("No of clusters")
plt.ylabel("SSD")


# In[33]:


# l1[i]: The current value in the list.


# In[34]:


#l1=ssd


# In[35]:


#l2 = []
#for i in range(len(l1)-1):
#    res = ((l1[i] - l1[i + 1] )/ l1[i]*100)
#    l2.append(np.abs(res))


# In[36]:


#l2


# In[37]:


from sklearn.cluster import KMeans
kmean_mall1=KMeans(n_clusters=6)
kmean_mall1.fit(mall)


# In[38]:


kmean_mall1.score(mall)


# In[39]:


pd.Series(kmean_mall1.labels_).value_counts()


# In[40]:


mall['Cluster_number']=kmean_mall1.labels_


# In[41]:


mall.head(20)


# In[42]:


plt.figure(figsize=(10,6))


# In[ ]:





# In[ ]:




