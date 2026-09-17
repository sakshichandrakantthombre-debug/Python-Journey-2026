#!/usr/bin/env python
# coding: utf-8

# # Unsupervised Learning 

# # K-Means

# In[ ]:


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


# In[16]:


import pandas as pd


# In[17]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd


# In[18]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\mall_kmeans.csv")


# In[19]:


mall=pd.read_csv(r"C:\Users\user\Desktop\MLA\mall_kmeans.csv")


# In[20]:


mall


# In[21]:


mall=mall.drop(['CustomerID'],axis=1)


# In[22]:


mall


# In[23]:


mall.rename(columns={'Annual Income (k$)':'Anuincome','Spending Score (1-100)':'spendingscore'},inplace=True)


# In[24]:


mall



# In[31]:


mall.isnull().sum()[mall.isnull().sum()>0]


# In[32]:


mall.Genre.value_counts()


# In[33]:


mall.Genre.value_counts()


# In[34]:


mall.head()


# In[38]:


from sklearn.cluster import KMeans
kmean_mall=KMeans(n_clusters=4)


# In[41]:


mall.Genre.replace({'Female':0,'Male':1},inplace=True)


# In[42]:


mall.head()


# In[43]:


from sklearn.cluster import KMeans
kmean_mall=KMeans(n_clusters=4)


# In[44]:


kmean_mall.fit(mall)


# In[45]:


kmean_mall.labels_


# In[46]:


len(kmean_mall.labels_)


# In[47]:


pd.DataFrame(kmean_mall.labels_).value_counts()


# In[48]:


cluster_center=pd.DataFrame(kmean_mall.cluster_centers_)


# In[49]:


cluster_center


# In[ ]:




