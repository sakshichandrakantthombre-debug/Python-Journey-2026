#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Day1

# In[ ]:





# # Linear Regression

# In[1]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd


# In[2]:


# Linear Regression
# steps to be followed

#data import
#data cleaning-->null,replace
#Sampling-->train_test_splite
#Linreg
#Build Model-->fit
#linreg.score-->Rsquare
#AdjRsquare
#linreg.intercept_
#linreg.coef_
#pred-->train_x,test_x
#err_train
#err_mean()
#hist plot
#skew()
#kurt+3
#scatter plot
#data fram-->x=Actual y=pred
#regplot
#err_test
#mse
#rmse
#mape
#acc
# To be taken as note
# 1) data should be numeric and continuous only
# 2) hist should be normaly distributed
# 3) Data should be equaly scattered
# 4) in regplot all data should be linear pred line


# In[3]:


import pandas as pd


# # LungCapData

# In[4]:


pd.read_csv(r"C:\Users\user\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\sessions\F81493623DA4A6C582DE384F23169A366E91AA5E\transfers\2026-37\LungCapData.csv")


# In[5]:


lung=pd.read_csv(r"C:\Users\user\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\sessions\F81493623DA4A6C582DE384F23169A366E91AA5E\transfers\2026-37\LungCapData.csv")


# In[6]:


lung.isnull().sum()[lung.isnull().sum()>0]


# In[7]:


lung.shape


# In[8]:


lung.Smoke.replace({'no':0,'yes':1},inplace=True)
lung.Gender.replace({'male':1,'female':0},inplace=True)
lung.Caesarean.replace({'no':0,'yes':1},inplace=True)


# In[9]:


lung.head()


# In[10]:


from sklearn.model_selection import train_test_split
lung_train,lung_test=train_test_split(lung,test_size=.2)


# In[11]:


lung_train_x=lung_train.iloc[::,1:]
lung_train_y=lung_train.iloc[::,0]


# In[12]:


lung_test_x=lung_test.iloc[::,1:]
lung_test_y=lung_test.iloc[::,0]


# In[13]:


lung_test_x


# In[14]:


from sklearn.linear_model import LinearRegression
linreg=LinearRegression()


# In[15]:


linreg.fit(lung_train_x,lung_train_y)


# In[16]:


linreg.score(lung_train_x,lung_train_y)


# In[17]:


lung_train_x.shape[0]


# In[18]:


lung_train_x.shape[1]


# In[19]:


lung_train_x.shape


# In[20]:


Rsquare=linreg.score(lung_train_x,lung_train_y)
n=lung_train_x.shape[0]
k=lung_train_x.shape[1]

adjrsquare=1-(1-Rsquare)*(n-1)/(n-k-1)
adjrsquare


# In[21]:


print(linreg.intercept_)


# In[22]:


linreg.coef_


# In[23]:


pred_train=linreg.predict(lung_train_x)
pred_test=linreg.predict(lung_test_x)



# In[24]:


err_train=lung_train_y-pred_train


# In[25]:


err_train


# In[26]:


err_train.mean()


# In[27]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[28]:


plt.hist(err_train,edgecolor='red',bins=20);


# In[29]:


err_train.skew()


# In[30]:


err_train.kurtosis()+3


# In[31]:


plt.plot(err_train,'*')


# In[32]:


pred_act=pd.DataFrame()
pred_act['Actual']=lung_train_y
pred_act['Pred']=pred_train
pred_act


# In[33]:


sns.regplot(x='Actual',y='Pred',data=pred_act)


# In[34]:


err_test=lung_test_y-pred_test
err_test


# In[35]:


import numpy as np


# In[36]:


mse=np.mean(np.square(err_test))
mse


# In[37]:


np.sqrt(mse)


# In[38]:


mape=np.mean(np.abs(err_test*100/lung_test_y))


# In[39]:


mape


# acc=100-mape
# print(acc)

# In[ ]:





# In[ ]:





# # Data sets

# In[40]:


# 1) Property_Price_Train


# In[ ]:





# # Day2

# # Logistic Regression

# # CreditRisk59

# In[41]:


# Logistic Regression
# steps to be followed

#data import
#data cleaning-->null,replace
#Sampling-->train_test_splite

# over sampling it is used only when modal is classimblance-->after cleaning before sampling
#df1=sug_train[sug_train.complication==1]
#sug_train=pd.concat([sug_train,df1,df1])
#sug_train.shape

#logreg
#Build Model-->fit
#Pred_train,pred_test
#import confusion_matrix,accuracy_score,precision_score,f1_score,recall_score
#mat_test=confusion_matrix(sug_test_y,pred_test)--->build Confusion matrix
#accuracy_score
#recall_score
#precision_score
#FPR-->manual calculation
#f1_score

#pred_prob_test=logreg.predict_proba(sug_test_x)
#len(pred_prob_test)

#from sklearn.metrics import roc_auc_score,roc_curve
#roc_auc_score(sug_test_y,pred_prob_test[:,1])

#fpr,tpr,th=roc_curve(sug_test_y,pred_prob_test[:,1])

#plt.plot(fpr,tpr,marker='*',color='green')
#plt.xlabel('fpr')
#plt.ylabel('tpr')
#plt.title('roc curve')
#plt.grid()


# To be taken as note
# 1) data should be numeric and Binomile only
# 2) confusion matrix should be not class imblance, if than need to do over sampling
# 3) AROUC curve should be increase in TPR than increase FPR
# 4) only one parameter can not play the role it should be evaluted as per modeel performance,
#    model performance is based on requirement



# In[5]:


import pandas as pd


# In[6]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\CreditRisk59.csv")


# In[7]:


cr=pd.read_csv(r"C:\Users\user\Desktop\MLA\CreditRisk59.csv")
cr.head(3)


# In[8]:


cr.isnull().sum()[cr.isnull().sum()>0]


# In[9]:


cr.Gender.fillna('Male', inplace = True)
cr. Married. fillna('Yes', inplace = True)
cr. Dependents. fillna(0, inplace = True)
cr. LoanAmount.fillna(cr.LoanAmount.mean(), inplace = True)
cr. Loan_Amount_Term.fillna(cr.Loan_Amount_Term.mean(), inplace = True)
cr. Credit_History. fillna(0, inplace = True)
cr.Self_Employed.fillna('No', inplace= True)


# In[10]:


cr1=cr #just a back up


# In[48]:


cr=cr.drop(['Loan_ID'],axis=1)
cr


# In[ ]:





# In[49]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


# In[50]:


cr[cr.select_dtypes(include='object').columns]


# In[51]:


cr[cr.select_dtypes(include='object').columns] = cr[cr.select_dtypes(include='object').columns].apply(le.fit_transform)


# In[52]:


cr


# In[53]:


#cr1=cr # just for back up
#cr=cr.drop(['Loan_ID'],axis=1)


# In[54]:


cr1.columns


# In[55]:


cr1


# In[56]:


from sklearn.model_selection import train_test_split
cr_train,cr_test=train_test_split(cr,test_size=.2)


# In[ ]:





# In[57]:


# over sampling
df1=cr_train[cr_train.Loan_Status==0]
cr_train=pd.concat([cr_train,df1,df1])
cr_train.shape


# In[58]:


cr_train .Loan_Status.value_counts()


# In[59]:


cr_train_x=cr_train.iloc[:,0:-1]
cr_train_y=cr_train.iloc[:,-1]


cr_test_x=cr_test.iloc[:,0:-1]
cr_test_y=cr_test.iloc[:,-1]


# In[60]:


cr_test_x


# In[61]:


from sklearn.linear_model import LogisticRegression


# In[62]:


logreg=LogisticRegression()
logreg.fit(cr_train_x,cr_train_y)


# In[63]:


pred_test


# In[64]:


pred_train=logreg.predict(cr_train_x)
pred_test=logreg.predict(cr_test_x)



# In[65]:


from sklearn.metrics import confusion_matrix


# In[66]:


mat_test=confusion_matrix(cr_test_y,pred_test)
mat_test


# In[67]:


from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score


# In[68]:


16/(16+29)*100


# In[69]:


accuracy_score(cr_test_y,pred_test)


# In[70]:


recall_score(cr_test_y,pred_test)


# In[71]:


precision_score(cr_test_y,pred_test)


# In[72]:


f1_score(cr_test_y,pred_test)


# In[73]:


# recall / TPR
mat_test.diagonal().sum()/ mat_test.sum()


# In[ ]:





# In[74]:


mat_test1=pd.DataFrame(mat_test)
mat_test1.columns=['rej','app']


# In[75]:


mat_test1.index=['rej','app']


# In[76]:


mat_test1


# In[77]:


pred_prob_test=logreg.predict_proba(cr_test_x)
len(pred_prob_test)


# In[78]:


from sklearn.metrics import roc_auc_score,roc_curve


# In[79]:


#pred_prob_test[:,1]
# will select all rows and 2nd column


# In[80]:


roc_auc_score(cr_test_y,pred_prob_test[:,1]) # area under the curve the value


# In[81]:


fpr,tpr,thre  =roc_curve(cr_test_y,pred_prob_test[:,1])


# In[82]:


import matplotlib.pyplot as plt


# In[83]:


plt.plot(fpr,tpr,marker='*' , color='green')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('roc plot on fpr and tpr')
plt.grid()


# In[84]:


# it is done to see .4


# In[ ]:





# # Day3

# # Churn

# In[85]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\Churn.csv")


# In[86]:


churn=pd.read_csv(r"C:\Users\user\Desktop\MLA\Churn.csv")


# In[87]:


churn.isnull().sum()[churn.isnull().sum()>0]


# In[ ]:





# In[88]:


churn.select_dtypes(include='object').columns


# In[89]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


# In[90]:


churn.gender=le.fit_transform(churn.gender)
churn.Partner=le.fit_transform(churn.Partner)
churn.Dependents=le.fit_transform(churn.Dependents)
churn.PhoneService=le.fit_transform(churn.PhoneService)
churn.MultipleLines=le.fit_transform(churn.MultipleLines)
churn.InternetService=le.fit_transform(churn.InternetService)
churn.OnlineSecurity=le.fit_transform(churn.OnlineSecurity)
churn.OnlineBackup=le.fit_transform(churn.OnlineBackup)
churn.DeviceProtection=le.fit_transform(churn.DeviceProtection)
churn.TechSupport=le.fit_transform(churn.TechSupport)
churn.StreamingTV=le.fit_transform(churn.StreamingTV)
churn.StreamingMovies=le.fit_transform(churn.StreamingMovies)
churn.Contract=le.fit_transform(churn.Contract)
churn.PaperlessBilling=le.fit_transform(churn.PaperlessBilling)
churn.PaymentMethod=le.fit_transform(churn.PaymentMethod)
churn.TotalCharges=le.fit_transform(churn.TotalCharges)
churn.customerID=le.fit_transform(churn.customerID)
churn.Churn=le.fit_transform(churn.Churn)


# In[91]:


churn[churn.select_dtypes(include='object').columns] = churn[churn.select_dtypes(include='object').columns].apply(le.fit_transform)


# In[92]:


churn.head()


# In[93]:


from sklearn.model_selection import train_test_split
churn_train,churn_test=train_test_split(churn,test_size=.2)


# In[94]:


churn_train.Churn.value_counts()


# In[95]:


# over sampling
df1=churn_train[churn_train.Churn==1]
churn_train=pd.concat([churn_train,df1,df1])
churn_train.shape


# In[96]:


churn_train.Churn.value_counts()


# In[97]:


churn_train_x=churn_train.iloc[::,0:-1]
churn_train_y=churn_train.iloc[::,-1]

churn_test_x=churn_test.iloc[::,0:-1]
churn_test_y=churn_test.iloc[::,-1]


# In[ ]:





# In[98]:


from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()


# In[99]:


logreg.fit(churn_train_x,churn_train_y)


# In[100]:


pred_train=logreg.predict(churn_train_x)
pred_test=logreg.predict(churn_test_x)


# In[101]:


from sklearn.metrics import confusion_matrix
mat_test=confusion_matrix(churn_test_y,pred_test)


# In[102]:


mat_test


# In[103]:


from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score


# In[104]:


286/(286+745)*100


# In[105]:


accuracy_score(churn_test_y,pred_test)


# In[106]:


206-145


# In[107]:


recall_score(churn_test_y,pred_test)


# In[108]:


precision_score(churn_test_y,pred_test)


# In[109]:


f1_score(churn_test_y,pred_test)


# In[ ]:





# In[110]:


pred_prob_test=logreg.predict_proba(churn_test_x)
len(pred_prob_test)


# In[ ]:





# In[111]:


from sklearn.metrics import roc_auc_score,roc_curve


# In[112]:


roc_auc_score(churn_test_y,pred_prob_test[:,1])


# In[113]:


fpr,tpr,thre=roc_curve(churn_test_y,pred_prob_test[:,1])


# In[114]:


import matplotlib.pyplot as plt


# In[115]:


plt.plot(fpr,tpr,marker='*',color='green')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('roc plot on fpr and tpr')
plt.grid()


# # Data sets

# In[116]:


# 1) Attrition 2) diabetesLogistic 3) Surgical_deepnet


# In[ ]:





# # day4

# # Decision Tree Classification

# # CreditRisk59

# In[117]:


# Decision Tree
# steps to be followed

#data import
#data cleaning-->null,replace
#Sampling-->train_test_splite

# over sampling it is used only when modal is classimblance-->after cleaning before sampling
#df1=sug_train[sug_train.complication==1]
#sug_train=pd.concat([sug_train,df1,df1])
#sug_train.shape

#from sklearn.tree import DecisionTreeClassifier
#dt=DecisionTreeClassifier(criterion='entropy',min_samples_split=50)
# --> Hyperparametres -->by defolt it is gini,min_samples_split,max_depth,etc

#Build Model-->fit
#Pred_train,pred_test
#import confusion_matrix,accuracy_score,precision_score,f1_score,recall_score
#mat_test=confusion_matrix(sug_test_y,pred_test)--->build Confusion matrix
#accuracy_score
#recall_score
#precision_score
#FPR-->manual calculation
#f1_score

#pred_prob_test=dt.predict_proba(sug_test_x)
#len(pred_prob_test)

#from sklearn.metrics import roc_auc_score,roc_curve
#roc_auc_score(sug_test_y,pred_prob_test[:,1])

#fpr,tpr,th=roc_curve(sug_test_y,pred_prob_test[:,1])

#import matplotlib.pyplot as plt
#import seaborn as sns
#plt.plot(fpr,tpr,marker='*',color='green')
#plt.xlabel('fpr')
#plt.ylabel('tpr')
#plt.title('roc curve')
#plt.grid()

# feature importances, feature selection --> to send to call dept

# Read the Decision Tree----------------------------------------------------------->
#from IPython.display import Image
#from sklearn.tree import export_graphviz
#import pydotplus
#import pydot
#from six import StringIO

#dot_data = StringIO()
#import matplotlib.pyplot as plt
#fig= plt.figure(figsize=(12,12))

#export_graphviz(dt_mp  , out_file=dot_data,
#                filled=True, rounded=True,
#                special_characters=True , feature_names=mp_train_x.columns  )
#graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

#(graph,) = pydot.graph_from_dot_data(dot_data.getvalue())
#Image(graph.create_png())
#---------------------------------------------------------------------------------->

# To be taken as note
# 1) data should be numeric and Binomile only
# 2) confusion matrix should be not class imblance, if than need to do over sampling
# 3) AROUC curve should be increase in TPR than increase FPR
# 4) only one parameter can not play the role it should be evaluted as per modeel performance,
#    model performance is based on requirement
#5) to make best model use entropy,min_samples_split,max_depth,etc-->Hyperparameters



# In[118]:


import pandas as pd


# In[119]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\CreditRisk59.csv")


# In[ ]:





# In[120]:


cr=pd.read_csv(r"C:\Users\user\Desktop\MLA\CreditRisk59.csv")


# In[121]:


cr.isnull().sum()[cr.isnull().sum()>0]


# In[122]:


cr.Gender.fillna('Male', inplace = True)
cr. Married. fillna('Yes', inplace = True)
cr. Dependents. fillna(0, inplace = True)
cr. LoanAmount.fillna(cr.LoanAmount.mean(), inplace = True)
cr. Loan_Amount_Term.fillna(cr.Loan_Amount_Term.mean(), inplace = True)
cr. Credit_History. fillna(0, inplace = True)
cr.Self_Employed.fillna('No', inplace= True)


# In[123]:


cr.select_dtypes(include='object').columns


# In[124]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


# In[125]:


cr[cr.select_dtypes(include='object').columns] = cr[cr.select_dtypes(include='object').columns].apply(le.fit_transform)


# In[126]:


cr1=cr # just for back up
cr=cr.drop(['Loan_ID'],axis=1)


# In[127]:


cr


# In[13]:


from sklearn.model_selection import train_test_split
cr_train,cr_test=train_test_split(cr,test_size=.2)


# In[14]:


cr.Loan_Status.value_counts()


# In[15]:


# over sampling
df1=cr_train[cr_train.Loan_Status==0]
cr_train=pd.concat([cr_train,df1,df1,df1,df1])
cr_train.shape


# In[16]:


cr_train_x=cr_train.iloc[:,0:-1]
cr_train_y=cr_train.iloc[:,-1]

cr_test_x=cr_test.iloc[:,0:-1]
cr_test_y=cr_test.iloc[:,-1]


# In[17]:


cr_test_y


# In[19]:


from sklearn.tree import


# In[12]:


from sklearn.tree import
dt=DecisionTreeClassifier()


# In[ ]:


dt.fit(cr_train_x,cr_train_y)


# In[ ]:


pred_train=dt.predict(cr_train_x)
pred_test=dt.predict(cr_test_x)


# In[ ]:


from sklearn.metrics import confusion_matrix
mat_test=confusion_matrix(cr_test_y,pred_test)
mat_test


# In[ ]:


18/(18+32)*100


# In[ ]:


from sklearn.metrics import accuracy_score,recall_score,f1_score,precision_score


# In[ ]:


accuracy_score(cr_test_y,pred_test)


# In[ ]:


recall_score(cr_test_y,pred_test)


# In[ ]:


precision_score(cr_test_y,pred_test)


# In[ ]:


f1_score(cr_test_y,pred_test)


# In[ ]:


#fpr
31/(31+26)*100


# In[ ]:





# In[ ]:


pred_prob_test=dt.predict_proba(cr_test_x)
len(pred_prob_test)


# In[ ]:





# In[ ]:


from sklearn.metrics import roc_auc_score,roc_curve


# In[ ]:


roc_auc_score(cr_test_y,pred_prob_test[:,1])


# In[ ]:


fpr,tpr,thre=roc_curve(cr_test_y,pred_prob_test[:,1])


# In[ ]:


roc_auc_score(cr_test_y,pred_prob_test[:,1])


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


plt.plot(fpr,tpr,marker='*' , color='green')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('roc plot on fpr and tpr')
plt.grid()


# In[ ]:





# # Day5

# In[ ]:


##------------------------CTG DESCRIPTION
#LB : beats per second
#AC : acceleration per second
#FM : fetal movement per second
#NSP (Normal , suspect, pathalogical)


# # CTG

# In[21]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\CTG.csv")


# In[22]:


ctg=pd.read_csv(r"C:\Users\user\Desktop\MLA\CTG.csv")


# In[23]:


ctg.isnull().sum()[ctg.isnull().sum()>0]


# In[24]:


#ctg.info()


# In[ ]:





# In[25]:


from sklearn.model_selection import train_test_split
ctg_train,ctg_test=train_test_split(ctg,test_size=.2)


# In[26]:


# over sampling
#df3=ctg_train[ctg_train.NSP==3]
#df2=ctg_train[ctg_train.NSP==2]

#ctg_train=pd.concat([ctg_train,df3,df3,df2,df2])
#ctg_train.shape


# In[27]:


ctg.NSP.value_counts()


# In[28]:


ctg_train_x=ctg_train.iloc[:,0:-1]
ctg_train_y=ctg_train.iloc[:,-1]

ctg_test_x=ctg_test.iloc[:,0:-1]
ctg_test_y=ctg_test.iloc[:,-1]


# In[ ]:





# In[29]:


from sklearn.tree import DecisionTreeClassifier
dt_ctg=DecisionTreeClassifier(class_weight='balanced')


# In[ ]:





# In[30]:


dt_ctg.fit(ctg_train_x,ctg_train_y)


# In[31]:


pred_test_ctg=dt_ctg.predict(ctg_test_x)


# In[32]:


from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,f1_score


# In[33]:


tab_ctg= confusion_matrix(ctg_test_y,pred_test_ctg)


# In[34]:


tab_ctg


# In[35]:


accuracy_score(ctg_test_y,pred_test_ctg) # accuracy score model how much predicted right or corrected.


# In[38]:


precision_score(ctg_test_y,pred_test_ctg,average='macro')


# In[39]:


recall_score(ctg_test_y,pred_test_ctg,average='macro')


# In[40]:


f1_score(ctg_test_y,pred_test_ctg,average='macro')


# In[ ]:





# # Grid Search

# In[41]:


from sklearn.model_selection import GridSearchCV


# In[55]:


search_dict = {'criterion':['gini','entropy'],
              'max_depth':range(4,9),
              'min_samples_split':[50,75,100]}


# In[56]:


dt_ctg=DecisionTreeClassifier()
grid=GridSearchCV(dt_ctg,param_grid=search_dict)


# In[57]:


grid.fit(ctg_train_x,ctg_train_y)


# In[59]:


grid.best_params_


# # Random Search

# In[60]:


from sklearn.model_selection import RandomizedSearchCV


# In[61]:


search_dict1 = {'criterion':['gini','entropy'],
              'max_depth':range(4,9),
              'min_samples_split':[50,75,100]}


# In[62]:


dt_ctg=DecisionTreeClassifier()


# In[63]:


random_search=RandomizedSearchCV(
        estimator=dt_ctg,
        param_distributions=search_dict1,
        n_iter=10,
        random_state=42,
        cv=5
)



# In[64]:


random_search.fit(ctg_train_x,ctg_train_y)


# In[65]:


random_search.best_params_


# In[ ]:





# In[66]:


tab_ctg_df=pd.DataFrame(tab_ctg)
tab_ctg_df.columns=['Normal','suspect','pathalogical']
tab_ctg_df.index=['Normal','suspect','pathalogical']


# In[67]:


tab_ctg_df


# In[ ]:





# In[68]:


get_ipython().run_line_magic('pip', 'install pydotplus')


# In[69]:


get_ipython().run_line_magic('pip', 'install pydot')


# In[70]:


get_ipython().run_line_magic('pip', 'install dot')


# In[ ]:


#conda install graphviz


# In[71]:


from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
import pydot
from six import StringIO


# In[72]:


dt_ctg.fit(ctg_train_x,ctg_train_y)


# In[73]:


dot_data = StringIO()

import matplotlib.pyplot as plt
fig= plt.figure(figsize=(12,12))

export_graphviz(dt_ctg  , out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True , feature_names=ctg_train_x.columns  )
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

(graph,) = pydot.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())


# # Data sets

# In[ ]:


# 1) Surgical_deepnet 2)Churn 3) Attrition 4) trainRF 5)original_data


# In[ ]:





# # Day6

# # Random Forest

# In[ ]:


# Random Forest
# steps to be followed

#data import
#data cleaning-->null,replace
#Sampling-->train_test_splite

# over sampling it is used only when modal is classimblance-->after cleaning before sampling
#df1=sug_train[sug_train.complication==1]
#sug_train=pd.concat([sug_train,df1,df1])
#sug_train.shape

#from sklearn.ensemble import RandomForestClassifier
#rfc=RandomForestClassifier(n_estimators=250)
# --> Hyperparametres -->n_estimators=250-->numbers of trees

#Build Model-->fit
#Pred_train,pred_test
#import confusion_matrix,accuracy_score,precision_score,f1_score,recall_score
#mat_test=confusion_matrix(sug_test_y,pred_test)--->build Confusion matrix
#accuracy_score
#recall_score
#precision_score
#FPR-->manual calculation
#f1_score

#pred_prob_test=dt.predict_proba(sug_test_x)
#len(pred_prob_test)

#from sklearn.metrics import roc_auc_score,roc_curve
#roc_auc_score(sug_test_y,pred_prob_test[:,1])

#fpr,tpr,th=roc_curve(sug_test_y,pred_prob_test[:,1])

#import matplotlib.pyplot as plt
#import seaborn as sns
#plt.plot(fpr,tpr,marker='*',color='green')
#plt.xlabel('fpr')
#plt.ylabel('tpr')
#plt.title('roc curve')
#plt.grid()

# feature importances, feature selection --> to send to call dept

#---------------------------------------------------------------------------------->

# To be taken as note
# 1) data should be numeric and Binomile only
# 2) confusion matrix should be not class imblance, if than need to do over sampling
# 3) AROUC curve should be increase in TPR than increase FPR
# 4) only one parameter can not play the role it should be evaluted as per modeel performance,
#    model performance is based on requirement
#5) to make best model use n_estimators=250-->Hyperparameters



# In[74]:


pd.read_csv(r"C:\Users\user\MLA\Attrition.csv")


# In[77]:


at=pd.read_csv(r"C:\Users\user\MLA\Attrition.csv")


# In[78]:


at.isnull().sum()[at.isnull().sum()>0]


# In[79]:


at.info()


# In[80]:


at.Attrition.value_counts()


# In[81]:


at.Attrition.replace({'No':0,'Yes':1},inplace=True)


# In[ ]:


at.select_dtypes(include='object').columns


# In[82]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


# In[83]:


at[at.select_dtypes(include='object').columns]=at[at.select_dtypes(include='object').columns].apply(le.fit_transform)


# In[84]:


at.head()


# In[85]:


from sklearn.model_selection import train_test_split
at_train,at_test=train_test_split(at,test_size=.2)


# In[86]:


# over sampling
df1=at_train[at_train.Attrition==1]
at_train=pd.concat([at_train,df1])
at_train.shape


# In[87]:


at_train_x=at_train.iloc[::,at.columns!='Attrition']
at_train_y=at_train.Attrition


# In[88]:


at_test_x=at_test.iloc[::,at.columns!='Attrition']
at_test_y=at_test.Attrition


# In[89]:


at_test_y


# In[90]:


from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=250,criterion="entropy",)


# In[ ]:





# In[91]:


rfc.fit(at_train_x,at_train_y)


# In[92]:


#pred_train=rfc.predict(at_train_x)
pred_test=rfc.predict(at_test_x)
pred_test


# In[93]:


from sklearn.metrics import confusion_matrix,accuracy_score,recall_score,precision_score,f1_score


# In[94]:


mat=confusion_matrix(at_test_y,pred_test)


# In[95]:


mat


# In[96]:


accuracy_score(at_test_y,pred_test)


# In[97]:


recall_score(at_test_y,pred_test)


# In[98]:


precision_score(at_test_y,pred_test)


# In[99]:


f1_score(at_test_y,pred_test)


# In[100]:


pred_prob_test=rfc.predict_proba(at_test_x)


# In[101]:


from sklearn.metrics import roc_auc_score,roc_curve


# In[102]:


roc_auc_score(at_test_y,pred_prob_test[:,1])


# In[103]:


fpr,tpr,thr=roc_curve(at_test_y,pred_prob_test[:,1])


# In[104]:


import matplotlib.pyplot as plt


# In[105]:


plt.plot(fpr,tpr,marker='*',color='green')
plt.xlabel(fpr)
plt.ylabel(tpr)
plt.grid()
plt.title('arouc curve')


# In[ ]:


at.Attrition.value_counts()


# # GridSearchCV

# In[ ]:


from sklearn.model_selection import GridSearchCV


# In[ ]:


search_dict = {"n_estimators":[2,5,10,15,20,25],
    'criterion':['gini','entropy'],
              'max_depth':range(4,9),
              'min_samples_split':[50,75,100]}


# In[ ]:


dt_at=RandomForestClassifier()
grid=GridSearchCV(dt_at,param_grid=search_dict,cv=5,scoring="f1_macro")


# In[ ]:


grid.fit(at_train_x,at_train_y)


# In[ ]:


grid.best_params_


# In[ ]:


grid.best_score_


# In[ ]:





# In[ ]:


import sklearn
sklearn.metrics.get_scorer_names()


# # Data sets

# In[ ]:


# 1) CreditRisk59 2) Surgical_deepnet 3) Churn 4) trainRF 5) CTG 6) original_data


# In[ ]:





# # Day7

# # Cross Validation k-fold/CV

# In[ ]:


# Cross Validaion
# steps to be followed

#data import
#data cleaning-->null,replace
#Sampling-->train_test_splite

#from sklearn.model_selection import cross_val_score
#from sklearn.tree import DecisionTreeClassifier
#dt_mp=DecisionTreeClassifier()
#score_dt_mp=cross_val_score(dt_mp,mp_train_x,mp_train_y,cv=5)-------> cv means make a 5 group of data
#score_dt_mp.mean().-----> should be use

# model is build of decision tree


# To be taken as note
# 1) its not an Algorithm its a consept , it can be use on any algo.
# 2) CV--> cross validation --> it make a 5 group of data---->cv=5
# 3) mean is used
# 4) cross validation is type of testing on train data (train 8000,cv=2000) itration after every record


# In[ ]:


import pandas as pd


# In[ ]:


pd.read_csv(r'C:\Users\sudha\OneDrive\Desktop\files\Files\trainRF.csv')


# In[ ]:


mp=pd.read_csv(r'C:\Users\sudha\OneDrive\Desktop\files\Files\trainRF.csv')


# In[ ]:


mp.isnull().sum()[mp.isnull().sum()>0]


# In[ ]:


from sklearn.model_selection import train_test_split
mp_train,mp_test=train_test_split(mp,train_size=.2)


# In[ ]:


mp_train_x=mp_train.iloc[::,:-1]
mp_train_y=mp_train.iloc[::,-1]


# In[ ]:


mp_test_x=mp_test.iloc[::,:-1]
mp_test_y=mp_test.iloc[::,-1]


# In[ ]:


from sklearn.model_selection import cross_val_score


# In[ ]:


from sklearn.tree import DecisionTreeClassifier
dt_mp=DecisionTreeClassifier()


# In[ ]:


dt_mp.fit(mp_train_x,mp_train_y)


# In[ ]:


score_dt_mp=cross_val_score(dt_mp,mp_train_x,mp_train_y,cv=5)


# In[ ]:


score_dt_mp


# In[ ]:


score_dt_mp.min()


# In[ ]:


score_dt_mp.max()


# In[ ]:


score_dt_mp.mean()


# # Data sets

# In[ ]:


# all CAT data-->1) CreditRisk59 2) Surgical_deepnet 3) Churn 4) trainRF 5) CTG 6) original_data


# In[ ]:





# # Ridge and Lasso

# In[ ]:


import pandas as pd


# In[ ]:


# over Fitting ---------->Its a problem
# Ridge and Lasso-------> solution for over fitting
# steps to be followed

#data import
#data cleaning-->null,replace
#Sampling-->train_test_splite
#Ridge---/Lasso
#Rsquare=ridge.score(tr_train_x,tr_train_y)-->Rsquare
#AdjRsquare
#pred-->train_x,test_x
#err_train
#mse
#mape
#acc
# To be taken as note
# 1) data should be numeric and continuous only
# 2) its not a model but it is use to solve problem of over fitting models


# # Ridge

# In[ ]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\train123.csv")


# In[ ]:


tr=pd.read_csv(r"C:\Users\user\Desktop\MLA\train123.csv")


# In[ ]:


tr.isnull().sum()[tr.isnull().sum()>0]


# In[ ]:


tr.select_dtypes(include='object').columns


# In[ ]:


tr=tr.drop(['ID'],axis=1)


# In[ ]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


# In[ ]:


tr[tr.select_dtypes(include='object').columns]=tr[tr.select_dtypes(include='object').columns].apply(le.fit_transform)


# In[ ]:


from sklearn.model_selection import train_test_split
tr_train,tr_test=train_test_split(tr,test_size=.2)


# In[ ]:


tr_train_x=tr_train.iloc[::,1::]
tr_train_y=tr_train.iloc[::,0]


# In[ ]:


tr_test_x=tr_test.iloc[::,1:]
tr_test_y=tr_test.iloc[::,0]


# In[ ]:


tr_test_x


# In[ ]:


from sklearn.linear_model import Ridge


# In[ ]:


ridge=Ridge()


# In[ ]:


ridge.fit(tr_train_x,tr_train_y)


# In[ ]:


Rsquare=ridge.score(tr_train_x,tr_train_y)
Rsquare


# In[ ]:


Rsquare=ridge.score(tr_train_x,tr_train_y)
N=tr_train_x.shape[0]
K=tr_train_x.shape[1]

AdjRsquare=1-(1-Rsquare)*(N-1)/(N-K-1)
AdjRsquare


# In[ ]:


pred_train=ridge.predict(tr_train_x)
pred_test=ridge.predict(tr_test_x)


# In[ ]:


err_train=tr_train_y-pred_train
err_test=tr_test_y-pred_test


# In[ ]:


import numpy as np


# In[ ]:


mse_train=np.mean(np.square(err_train))
mse_test=np.mean(np.square(err_test))


# In[ ]:


mse_test


# In[ ]:


mse_train


# In[ ]:


mape_train=np.mean(np.abs(err_train*100/tr_train_y))


# In[ ]:


mape_train


# In[ ]:


mape_test=np.mean(np.abs(err_test*100/tr_test_y))


# In[ ]:


mape_test


# In[ ]:


acc=100-mape_train
acc


# In[ ]:


acc1=100-mape_test
acc1


# In[ ]:


#import matplotlib.pyplot as plt


# In[ ]:


ridge.coef_.max()


# In[ ]:


ridge.coef_


# In[ ]:


tr_ridge=pd.DataFrame()
tr_ridge['feat']=tr_train_x.columns
tr_ridge['coef']=ridge.coef_
tr_ridge


# In[ ]:


tr_ridge[tr_ridge.coef!=0]


# In[ ]:


375-355


# # Lasso

# In[ ]:


from sklearn.linear_model import Lasso
lasso=Lasso()


# In[ ]:


lasso.fit(tr_train_x,tr_train_y)


# In[ ]:


Rsquare=lasso.score(tr_train_x,tr_train_y)
Rsquare


# In[ ]:


Rsquare=lasso.score(tr_train_x,tr_train_y)
N=tr_train_x.shape[0]
k=tr_train_x.shape[1]

AdjRsquare=1-(1-Rsquare)*(N-1)/(N-K-1)
AdjRsquare


# In[ ]:


pred_train=lasso.predict(tr_train_x)
pred_test=lasso.predict(tr_test_x)


# In[ ]:


err_train=tr_train_y-pred_train
err_test=tr_test_y-pred_test


# In[ ]:


mse_train=np.mean(np.square(err_train))
mse_test=np.mean(np.square(err_test))


# In[ ]:


print(mse_train)
print(mse_test)


# In[ ]:


mape_train=np.mean(np.abs(err_train*100/tr_train_y))
mape_test=np.mean(np.abs(err_test*100/tr_test_y))


# In[ ]:


mape_test


# In[ ]:


mape_train


# In[ ]:


acc=100-mape_train
acc


# In[ ]:


acc=100-mape_test
acc


# In[ ]:


lasso.coef_


# In[ ]:


tr_lasso=pd.DataFrame()
tr_lasso['feat']=tr_train_x.columns
tr_lasso['coef']=lasso.coef_


# In[ ]:


tr_lasso[tr_lasso.coef!=0]


# In[ ]:


375-7


# # Data sets

# In[ ]:


# 1) LungCapData


# In[ ]:





# # Day8

# # SVM

# In[261]:


import pandas as pd


# In[262]:


# SVM
# steps to be followed

#data import
#data cleaning-->null,replace
#Sampling-->train_test_splite

# over sampling it is used only when modal is classimblance-->after cleaning before sampling
#df1=sug_train[sug_train.complication==1]
#sug_train=pd.concat([sug_train,df1,df1])
#sug_train.shape

#from sklearn.svm import SVC
#svc=SVC(kernel='linear')
# --> Hyperparametres -->linear,poly,rbf,sigmoid

#Build Model-->fit
#Pred_train,pred_test
#import confusion_matrix,accuracy_score,precision_score,f1_score,recall_score
#mat_test=confusion_matrix(sug_test_y,pred_test)--->build Confusion matrix
#accuracy_score
#recall_score
#precision_score
#FPR-->manual calculation
#f1_score

#pred_prob_test=dt.predict_proba(sug_test_x)
#len(pred_prob_test)

#from sklearn.metrics import roc_auc_score,roc_curve
#roc_auc_score(sug_test_y,pred_prob_test[:,1])

#fpr,tpr,th=roc_curve(sug_test_y,pred_prob_test[:,1])

#import matplotlib.pyplot as plt
#import seaborn as sns
#plt.plot(fpr,tpr,marker='*',color='green')
#plt.xlabel('fpr')
#plt.ylabel('tpr')
#plt.title('roc curve')
#plt.grid()

# feature importances, feature selection --> to send to call dept

#---------------------------------------------------------------------------------->

# To be taken as note
# 1) data should be numeric and Binomile only
# 2) confusion matrix should be not class imblance, if than need to do over sampling
# 3) only one parameter can not play the role it should be evaluted as per modeel performance,
#    model performance is based on requirement
#5) to make best model use sigmoid,linear,rbf,poly-->Hyperparameters



# In[263]:


import pandas as pd


# In[264]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\CTG.csv")


# In[265]:


sv=pd.read_csv(r"C:\Users\user\Desktop\MLA\CTG.csv")


# In[266]:


sv.isnull().sum()[sv.isnull().sum()>0]


# In[267]:


sv.select_dtypes(include='object').columns


# In[268]:


sv.education.replace({'basic.4y':1, 'high.school':4, 'basic.6y':2, 'basic.9y':3,
       'professional.course':6, 'unknown':0, 'university.degree':5,
       'illiterate':0},inplace= True)
sv.default.replace({'no':0, 'unknown':1, 'yes':2},inplace= True)
sv.housing.replace({'no':0, 'unknown':1, 'yes':2},inplace= True)
sv.month.replace({'may':5, 'jun':6, 'jul':7, 'aug':8, 'oct':10, 'nov':11, 'dec':12, 'mar':3, 'apr':4,
       'sep':9},inplace= True)
sv.day_of_week.replace({'mon':1, 'tue':2, 'wed':3, 'thu':4, 'fri':5},inplace= True)
sv.poutcome.replace({'nonexistent':0, 'failure':1, 'success':2},inplace= True)


# In[269]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


# In[270]:


sv[sv.select_dtypes(include='object').columns]=sv[sv.select_dtypes(include='object').columns].apply(le.fit_transform)


# In[271]:


sv.y.value_counts()


# In[272]:


from sklearn.model_selection import train_test_split
sv_train,sv_test=train_test_split(sv,test_size=.2)


# In[275]:


# oversampling
df1=sv_train[sv_train.y==1]
sv_train=pd.concat([sv_train,df1,df1])


# In[274]:


sv_train_x=sv_train.iloc[::,:-1]
sv_train_y=sv_train.iloc[::,-1]


# In[ ]:


sv_test_x=sv_test.iloc[::,:-1]
sv_test_y=sv_test.iloc[::,-1]


# In[ ]:


from sklearn.svm import SVC
svc=SVC(kernel='linear',)


# In[ ]:


svc.fit(sv_train_x,sv_train_y)


# In[ ]:


pred_sv=svc.predict(sv_test_x)


# In[ ]:


from sklearn.metrics import confusion_matrix,accuracy_score,recall_score,precision_score,f1_score


# In[ ]:


tab=confusion_matrix(sv_test_y,pred_sv)


# In[ ]:


tab


# In[ ]:


accuracy_score(sv_test_y,pred_sv)


# In[ ]:


precision_score(sv_test_y,pred_sv)


# In[ ]:


recall_score(sv_test_y,pred_sv)


# In[ ]:


f1_score(sv_test_y,pred_sv)


# In[ ]:


from sklearn.metrics import classification_report


# In[ ]:


print(classification_report(sv_test_y,pred_sv))


# In[ ]:


import sklearn
sklearn.metrics.get_scorer_names()


# In[ ]:


# Hyperparameter
#linear--> acc=90,tpr=32,pre=64,
#poly-->acc=89,tpr=22,pre=62
#rbf-->acc=90,tpr=22,pre=64
#sigmoid--> 90,21,65


# # Data sets

# In[ ]:


# 1) CreditRisk59 2) Surgical_deepnet 3) Churn 4) trainRF 5) CTG 6) original_data


# In[ ]:





# In[ ]:





# # Day9

# # KNN

# In[ ]:


# K-nearest neighbors -----> nearest neighbor should be select eg-->n_neighbors=25
# steps to be followed

#data import
#data cleaning-->null,replace
#Sampling-->train_test_splite

# over sampling it is used only when modal is classimblance-->after cleaning before sampling
#df1=sug_train[sug_train.complication==1]
#sug_train=pd.concat([sug_train,df1,df1])
#sug_train.shape

#from sklearn.neighbors import KNeighborsClassifier
#knn=KNeighborsClassifier(n_neighbors=25)
# --> Hyperparametres -->n_neighbors=25

#Build Model-->fit
#Pred_train,pred_test
#import confusion_matrix,accuracy_score
#mat_test=confusion_matrix(sug_test_y,pred_test)--->build Confusion matrix
#accuracy_score

#l1=[]
#for k in range(1,51):
#    knn=KNeighborsClassifier(n_neighbors=k)
#    knn.fit(ctg_train_x,ctg_train_y)
#    pred_knn=knn.predict(ctg_test_x)
#    tab_knn=confusion_matrix(ctg_test_y,pred_knn)
#    acc=accuracy_score(ctg_test_y,pred_knn)
#    l1.append(acc)

#import matplotlib.pyplot as plt
#import seaborn as sns

#plt.figure(figsize=(15,6))
#plt.plot(list(range(1,51)),l1,marker='*')
#plt.grid()

# To be taken as note
# 1) data should be numeric and Binomile only
# 2) confusion matrix should be not class imblance, if than need to do over sampling
#3) to make best model use n_neighbors=25 -->Hyperparameters
#4) plot should be decrease conteniously -----> good acc. as well as stabel model


# In[ ]:


import pandas as pd


# In[106]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\CTG.csv")


# In[107]:


ctg=pd.read_csv(r"C:\Users\user\Desktop\MLA\CTG.csv")


# In[108]:


ctg.isnull().sum()[ctg.isnull().sum()>0]


# In[109]:


from sklearn.model_selection import train_test_split
ctg_train,ctg_test=train_test_split(ctg,test_size=.2)


# In[110]:


ctg.NSP.value_counts()


# In[111]:


#over sampling
df2=ctg_train[ctg_train.NSP==2]
df3=ctg_train[ctg_train.NSP==3]
ctg_train=pd.concat([ctg_train,df3,df3,df3,df3,df2])


# In[ ]:





# In[112]:


ctg_train_x=ctg_train.iloc[:,0:-1]
ctg_train_y=ctg_train.iloc[:,-1]

ctg_test_x=ctg_test.iloc[:,0:-1]
ctg_test_y=ctg_test.iloc[:,-1]


# In[113]:


ctg_test_y


# In[114]:


from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=37)


# In[115]:


knn.fit(ctg_train_x,ctg_train_y)


# In[116]:


pred_knn=knn.predict(ctg_test_x)


# In[117]:


from sklearn.metrics import confusion_matrix,classification_report,accuracy_score


# In[118]:


tab_knn=confusion_matrix(ctg_test_y,pred_knn)


# In[119]:


tab_knn


# In[120]:


#tab_knn.diagonal().sum()/tab_knn.sum()
accuracy_score(ctg_test_y,pred_knn)


# In[121]:


print(classification_report(ctg_test_y,pred_knn))


# In[122]:


l1=[]
for k in range(1,100):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(ctg_train_x,ctg_train_y)
    pred_knn=knn.predict(ctg_test_x)
    tab_knn=confusion_matrix(ctg_test_y,pred_knn)
    acc=accuracy_score(ctg_test_y,pred_knn)
    l1.append(acc)


# In[189]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:





# In[190]:


plt.figure(figsize=(15,6))
plt.plot(list(range(1, 51)), l1[:50], marker='*')
plt.grid()


# In[191]:


plt.figure(figsize=(15,6))
plt.plot(list(range(1,100)), l1, marker='*')
plt.grid()


# # Data Sets

# In[ ]:


# 1) CreditRisk59 2) Surgical_deepnet 3) Churn 4) trainRF 5) CTG 6) original_data


# In[ ]:





# # Day10

# # Feature Selection / Festure Importance

# In[ ]:


# feature selection ---> festure importance--># bulid the modle with less x varibles ----> remove insignificant varibles
# steps to be followed

#data import
#data cleaning-->null,replace
#split
#cr_x=cr.iloc[::,0:-1]
#cr_x1=cr.iloc[::,0:-1]
#cr_y=cr.iloc[::,-1]
# convert into array
#cr_x=np.array(cr_x)
#cr_y=np.array(cr_y)

#--------------------------------------->Boruta feature selection
#from sklearn.ensemble import RandomForestClassifier---> take any alog.
#rf=RandomForestClassifier()
#from boruta import BorutaPy

#boruta_Feature_selector = BorutaPy(rf, max_iter = 25, verbose = 2)-----> 25=max ittration,2= best significant varibale
#boruta_Feature_selector.fit(cr_x,cr_y)

#boruta_Feature_selector.support_

#fet=pd.DataFrame()
#fet['fetu']=cr_x1.columns
#fet['imp']=boruta_Feature_selector.support_
#fet=fet.sort_values('imp',ascending=False)
#fet

#------------------------------------------------>RFE feature selection

#from sklearn.tree import DecisionTreeClassifier-----> take any alog.
#dt=DecisionTreeClassifier(criterion='entropy')
#from sklearn.feature_selection import RFE
#rfe=RFE(dt,n_features_to_select=2)--->2= best two
#rfe.fit(cr_x,cr_y)
#rfe.support_
#feat=pd.DataFrame()
#feat['col']=cr_x1.columns
#feat['imp']=rfe.support_
#feat=feat.sort_values('imp',ascending=False)
#feat

#------------------------------------------------->VarianceThreshold feature selection
# no split use named as data
#from sklearn.feature_selection import VarianceThreshold
#var=VarianceThreshold(threshold=.1)
#var.fit(tr)
#var.get_support()
#l4=[]
#for i in range (0,len(var.get_support())):
#    if var.get_support()[i]==False:
#        l4.append(tr.columns[i])
#l4
#tr=tr.loc[:,l4]
#tr------------> it convert into 0 and 1   out of 378-->284 signification varible


# To be taken as note
# 1) its not an Algorithm its a consept , it can be use on any algo.
# 2) Boruta---->we dont do predection it is only for feature selection,is a iterative alogrthim
# 3) boruta gives us ans in T and F which are signification varible but we done know which one is more significant
#    amoge True so we go to RFE
# 3) RFE--> recurrcive feature elimination
#   it gives us ans in T and F but which is more signification varible is at top
# 4)VarianceThreshold--> it gives us which x varibles are not signification at last

#parametric testing for feature selection
# co-relation
#->chi- square
# DT,RF,Ada boost
# lasso


# In[ ]:


import pandas as pd


# # Boruta

# In[137]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\CreditRisk59.csv")


# In[138]:


cr=pd.read_csv(r"C:\Users\user\Desktop\MLA\CreditRisk59.csv")


# In[139]:


cr.isnull().sum()[cr.isnull().sum()>0]


# In[140]:


cr.Gender.fillna('Male', inplace = True)
cr. Married. fillna('Yes', inplace = True)
cr. Dependents. fillna(0, inplace = True)
cr. LoanAmount.fillna(cr.LoanAmount.mean(), inplace = True)
cr. Loan_Amount_Term.fillna(cr.Loan_Amount_Term.mean(), inplace = True)
cr. Credit_History. fillna(0, inplace = True)
cr.Self_Employed.fillna('No', inplace= True)


# In[141]:


cr.select_dtypes(include='object').columns


# In[142]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


# In[143]:


cr[cr.select_dtypes(include='object').columns] = cr[cr.select_dtypes(include='object').columns].apply(le.fit_transform)


# In[144]:


cr=cr.drop(['Loan_ID'],axis=1)


# In[145]:


from sklearn.ensemble import RandomForestClassifier
from boruta import BorutaPy
import numpy as np


# In[146]:


get_ipython().run_line_magic('pip', 'install boruta')


# In[ ]:





# In[147]:


cr_x = cr.iloc[:, 0:11]
cr_x1 = cr.iloc[:, 0:11] # just a back up
cr_y = cr.iloc[:, -1]


# In[148]:


cr_x = np.array(cr_x)
cr_y = np.array(cr_y)
cr_y


# In[125]:


rf = RandomForestClassifier()
boruta_Feature_selector = BorutaPy(rf, max_iter = 25, verbose = 2)
boruta_Feature_selector.fit(cr_x, cr_y)



# In[127]:


get_ipython().run_line_magic('pip', 'install --upgrade numpy==1.23.5')


# In[128]:


boruta_Feature_selector.support_


# In[ ]:


cr_x1.columns


# In[ ]:


feat_imp = pd.DataFrame()
feat_imp['Features'] = cr_x1.columns
feat_imp['imp'] = boruta_Feature_selector.support_


# In[ ]:


feat_imp = feat_imp.sort_values('imp', ascending = False)


# In[ ]:


feat_imp


# In[ ]:


#droback of baruta it required more time , in work on cloud more money


# In[ ]:


#which one more signeficant among 3 cant say due to true and false


# In[ ]:





# # RFE

# In[ ]:


from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(  criterion='entropy')


# In[ ]:


from sklearn.feature_selection import RFE
rfe=RFE(dt,n_features_to_select=3)


# In[ ]:


rfe.fit(cr_x, cr_y)


# In[ ]:


rfe.support_


# In[ ]:


import numpy as  np


# In[156]:


feat_imp_dt = pd.DataFrame()
feat_imp_dt['col'] = cr_x1.columns
feat_imp_dt['imp'] =rfe.support_
feat_imp_dt


# In[ ]:


feat_imp_dt = feat_imp_dt.sort_values('imp', ascending = False)


# In[ ]:


feat_imp_dt


# In[ ]:





# # VarianceThreshold

# In[ ]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\Property_Price_Train (1).csv")


# In[ ]:


ppt=pd.read_csv(r"C:\Users\user\Desktop\MLA\Property_Price_Train (1).csv")


# In[161]:


ppt.select_dtypes(include='object').columns


# In[162]:


ppt.isnull().sum()[ppt.isnull().sum()>0]


# In[163]:


ppt.Lot_Extent.fillna(ppt.Lot_Extent .mean().round(2), inplace=True)
ppt.Lane_Type.fillna('Gravl', inplace=True)
ppt.Brick_Veneer_Type.fillna('BrkFace', inplace=True)
ppt.Brick_Veneer_Area.fillna(ppt.Brick_Veneer_Area .mean().round(2), inplace=True)
ppt.Basement_Height.fillna('TA', inplace=True)
ppt.Basement_Condition.fillna('TA', inplace=True)
ppt.Exposure_Level.fillna('No', inplace=True)
ppt.BsmtFinType1.fillna('Unf', inplace=True)
ppt.BsmtFinType2.fillna('Unf', inplace=True)
ppt.Electrical_System.fillna('SBrkr', inplace=True)
ppt.Fireplace_Quality.fillna('Gd', inplace=True)
ppt.Garage.fillna('Attchd', inplace=True)
ppt.Garage_Built_Year.fillna(ppt.Garage_Built_Year .mean().round(2), inplace=True)
ppt.Garage_Finish_Year.fillna('Unf', inplace=True)
ppt.Garage_Quality.fillna('TA', inplace=True)
ppt.Garage_Condition.fillna('TA', inplace=True)
ppt.Pool_Quality.fillna('TA', inplace=True)
ppt.Fence_Quality.fillna('MnPrv', inplace=True)
ppt.Miscellaneous_Feature.fillna('Shed', inplace=True)


# In[164]:


ppt.Zoning_Class.replace({'RLD':0, 'RMD':1, 'Commer':2, 'FVR':3, 'RHD':4},inplace=True)
ppt.Road_Type.replace({'Paved':0, 'Gravel':1},inplace=True)
ppt.Lane_Type.replace({'Gravl':0, 'Paved':1,'Grvl':2},inplace=True)
ppt.Property_Shape.replace({'Reg':0, 'IR1':1, 'IR2':2, 'IR3':3},inplace=True)
ppt.Land_Outline.replace({'Lvl':0, 'Bnk':1, 'Low':2, 'HLS':3},inplace=True)
ppt.Utility_Type.replace({'AllPub':0, 'NoSeWa':1},inplace=True)
ppt.Lot_Configuration.replace({'I':0, 'FR2P':1, 'C':2, 'CulDSac':3, 'FR3P':4},inplace=True)
ppt.Property_Slope.replace({'GS':0, 'MS':1, 'SS':2},inplace=True)
ppt.Neighborhood.replace({'CollgCr':0, 'Veenker':1, 'Crawfor':2, 'NoRidge':3, 'Mitchel':4, 'Somerst':5,
       'NWAmes':6, 'OldTown':7, 'BrkSide':8, 'Sawyer':9, 'NridgHt':10, 'NAmes':11,
       'SawyerW':12, 'IDOTRR':13, 'MeadowV':14, 'Edwards':15, 'Timber':16, 'Gilbert':17,
       'StoneBr':18, 'ClearCr':19, 'NPkVill':20, 'Blmngtn':21, 'BrDale':22, 'SWISU':23,
       'Blueste':24},inplace=True)
ppt.Condition1.replace({'Norm':0, 'Feedr':1, 'PosN':2, 'Artery':3, 'RRAe':4, 'RRNn':5, 'RRAn':5, 'PosA':6,
       'RRNe':7},inplace=True)

ppt.Condition2.replace({'Norm':0, 'Artery':1, 'RRNn':2, 'Feedr':3, 'PosN':4, 'PosA':5, 'RRAn':6, 'RRAe':7},inplace=True)
ppt.House_Type.replace({'1Fam':0, '2fmCon':1, 'Duplex':2, 'TwnhsE':3, 'Twnhs':4},inplace=True)
ppt. House_Design.replace({'2Story':0, '1Story':1, '1.5Fin':2, '1.5Unf':3, 'SFoyer':4, 'SLvl':5, '2.5Unf':6,
       '2.5Fin':7},inplace=True)
ppt. Roof_Design.replace({'Gable':0, 'Hip':1, 'Gambrel':2, 'Mansard':3, 'Flat':4, 'Shed':5},inplace=True)
ppt.Roof_Quality .replace({'SS':0, 'WSh':1, 'ME':2, 'WS':3, 'M':4, 'TG':4, 'R':5, 'CT':6},inplace=True)
ppt.Exterior1st.replace({'VinylSd':0, 'MetalSd':1, 'Wd Sdng':2, 'HdBoard':3, 'BrkFace':4, 'WdShing':5,
       'CemntBd':5, 'Plywood':6, 'AsbShng':7, 'Stucco':8, 'BrkComm':9, 'AsphShn':10,
       'Stone':11, 'ImStucc':12, 'CBlock':13},inplace=True)
ppt.Exterior2nd .replace({'VinylSd':0, 'MetalSd':1, 'Wd Shng':2, 'HdBoard':3, 'Plywood':4, 'Wd Sdng':5,
       'CmentBd':6, 'BrkFace':7, 'Stucco':7, 'AsbShng':8, 'Brk Cmn':9, 'ImStucc':10,
       'AsphShn':11, 'Stone':12, 'Other':13, 'CBlock':14},inplace=True)
ppt.Exterior2nd .replace({'VinylSd':0, 'MetalSd':1, 'Wd Shng':2, 'HdBoard':3, 'Plywood':4, 'Wd Sdng':5,
       'CmentBd':6, 'BrkFace':7, 'Stucco':7, 'AsbShng':8, 'Brk Cmn':9, 'ImStucc':10,
       'AsphShn':11, 'Stone':12, 'Other':13, 'CBlock':14},inplace=True)
ppt.Brick_Veneer_Type.replace({'BrkFace':0, 'None':1, 'Stone':2, 'BrkCmn':3},inplace=True)
ppt.Exterior_Material.replace({'Gd':0, 'TA':1, 'Ex':2, 'Fa':3},inplace=True)
ppt.  Exterior_Condition.replace({'TA':0, 'Gd':1, 'Fa':2, 'Po':3, 'Ex':4},inplace=True)
ppt.Foundation_Type .replace({'PC':0, 'CB':1, 'BT':2, 'W':3, 'SL':4, 'S':5},inplace=True)
ppt. Basement_Height.replace({'Gd':0, 'TA':1, 'Ex':2,  'Fa':3},inplace=True)
ppt.Basement_Condition.replace({'TA':0, 'Gd':1,  'Fa':2, 'Po':3},inplace=True)
ppt. Exposure_Level.replace({'No':0, 'Gd':1, 'Mn':2, 'Av':3,'Av ':4},inplace=True)
ppt.BsmtFinType1.replace({'GLQ':0, 'ALQ':1, 'Unf':2, 'Rec':3, 'BLQ':4, 'LwQ':5},inplace=True)
ppt.BsmtFinType2.replace({'Unf':0, 'BLQ':1,  'ALQ':2, 'Rec':3, 'LwQ':4, 'GLQ':5},inplace=True)
ppt.Heating_Type  .replace({'GasA':0, 'GasW':1, 'Grav':2, 'Wall':3, 'OthW':4, 'Floor':5},inplace=True)
ppt.Heating_Quality.replace({'Ex':0 ,'Gd':1, 'TA':2, 'Fa':3, 'Po':4},inplace=True)
ppt.Air_Conditioning.replace({'Y':1, 'N':0},inplace=True)
ppt.Electrical_System.replace({'SBrkr':5, 'FuseF':1, 'FuseA':2, 'FuseP':3, 'Mix':4,'SBrkr':6},inplace=True)
ppt. Kitchen_Quality.replace({'Gd':0, 'TA':1, 'Ex':2, 'Fa':3},inplace=True)
ppt.Functional_Rate .replace({'TF':0, 'MD1':1, 'MajD1':2, 'MD2':3, 'MD':4, 'MajD2':5, 'SD':6, 'MS':7},inplace=True)
ppt. Fireplace_Quality .replace({'TA':0, 'Gd':1, 'Fa':2, 'Ex':3, 'Po':4,'Gd ':5},inplace=True)
ppt. Garage.replace({'Attchd':0, 'Detchd':1, 'BuiltIn':2, 'CarPort':3,'Basment':4, '2TFes':5,
       '2Types':6},inplace=True)
ppt. Garage_Finish_Year.replace({'RFn':0, 'Unf':1, 'Fin':2,'Unf ':3},inplace=True)
ppt.Garage_Quality.replace({'TA':0, 'Fa':1, 'Gd':2, 'Ex':3, 'Po':4,'TA ':5},inplace=True)
ppt. Garage_Condition.replace({'TA':0, 'Fa':1, 'Gd':2, 'Po':3, 'Ex':4},inplace=True)
ppt.Pavedd_Drive.replace({'Y':1, 'N':0, 'P':2},inplace=True)
ppt.Fence_Quality.replace({'MnPrv':0, 'GdWo':1, 'GdPrv':2, 'MnWw':3},inplace=True)
ppt.Miscellaneous_Feature = ppt.Miscellaneous_Feature.replace ({'Shed':0, 'Gar2':1, 'Othr':2, 'TenC':3})
ppt.Sale_Type.replace({'WD':0, 'New':1, 'COD':2, 'ConLD':3, 'ConLI':4, 'CWD':5, 'ConLw':6, 'Con':7, 'Oth':8},inplace=True)
ppt.Sale_Condition.replace({'Normal':0, 'Abnorml':1, 'Partial':2, 'AdjLand':3, 'Alloca':4, 'Family':5},inplace=True)
ppt.Pool_Quality.replace({'Gd':1, 'Ex':2, 'Fa':3, 'Gd':4, 'TA':0},inplace=True)

ppt = ppt.drop(['Id','Lane_Type','Fence_Quality','Miscellaneous_Feature','Pool_Quality', ], axis = 1)

ppt = ppt.drop (['Fireplace_Quality'], axis = 1)


# In[165]:


from sklearn.feature_selection import VarianceThreshold
var=VarianceThreshold(threshold=.1)


# In[166]:


var.fit(ppt)


# In[167]:


var.get_support()


# In[168]:


l3=[]
for i in range (0,len(var.get_support())):
    if var.get_support()[i]==False:
        l3.append(ppt.columns[i])


# In[169]:


l3


# In[170]:


ppt=ppt.loc[:,l3]


# In[171]:


ppt


# In[ ]:





# In[ ]:





# # Day11

# # Ada Boost

# In[ ]:


# Ada Boost
# steps to be followed

#data import
#data cleaning-->null,replace
#Sampling-->train_test_splite

#build model on any Decision tree ,random forest
#check accuracy

#from sklearn.ensemble import AdaBoostClassifier
#add=AdaBoostClassifier(dt_mp,n_estimators=10)-->10 it will boost
#build the model of ada boost
#check accuracy


# To be taken as note
# 1) its not an Algorithm its a consept , it can be use on any algo.
# 2) n_estimators=10--> its Hyper parameter---> 10 times boost the model
# 3) it gives the more importance to week learners
#4)1000 records are passed to 1st boost and then 600 gives correct pred and wrong pred for 400 then that 400 records
# r taken in 2nd boost 300 gives me correct pred and 100 wrong pred so in 3rd boost only 100 records are taken and so on


# In[ ]:


import pandas as pd


# In[192]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\trainRF.csv")


# In[193]:


mp=pd.read_csv(r"C:\Users\user\Desktop\MLA\trainRF.csv")


# In[194]:


mp.isnull().sum()[mp.isnull().sum()>0]


# In[195]:


from sklearn.model_selection import train_test_split
mp_train,mp_test=train_test_split(mp,test_size=.2)


# In[196]:


mp_train_x=mp_train.iloc[::,:-1]
mp_train_y=mp_train.iloc[::,-1]


# In[197]:


mp_test_x=mp_test.iloc[::,:-1]
mp_test_y=mp_test.iloc[::,-1]


# # Decision tree

# In[198]:


from sklearn.tree import DecisionTreeClassifier
dt_mp=DecisionTreeClassifier(criterion='entropy')


# In[199]:


dt_mp.fit(mp_train_x,mp_train_y)


# In[200]:


pred=dt_mp.predict(mp_test_x)


# In[201]:


from sklearn.metrics import confusion_matrix,accuracy_score


# In[202]:


tab=confusion_matrix(mp_test_y,pred)


# In[203]:


tab


# In[204]:


accuracy_score(mp_test_y,pred)


# # Decision tree Ada boost

# In[205]:


from sklearn.ensemble import AdaBoostClassifier
add=AdaBoostClassifier(dt_mp)


# In[206]:


add.fit(mp_train_x,mp_train_y)


# In[207]:


pred_add=add.predict(mp_test_x)


# In[208]:


tab_add=confusion_matrix(mp_test_y,pred_add)


# In[209]:


tab_add


# In[210]:


accuracy_score(mp_test_y,pred_add)


# In[211]:


add.feature_importances_


# In[212]:


fet=pd.DataFrame()
fet['features']=mp_train_x.columns
fet['imp']=add.feature_importances_
fet


# In[213]:


fet=fet.sort_values('imp',ascending=False)
fet


# # random forest

# In[214]:


from sklearn.ensemble import RandomForestClassifier
rfc_mp=RandomForestClassifier(n_estimators=50)


# In[215]:


rfc_mp.fit(mp_train_x,mp_train_y)


# In[216]:


pred_rfc=rfc_mp.predict(mp_test_x)


# In[217]:


tab_rfc=confusion_matrix(mp_test_y,pred_rfc)


# In[218]:


tab_rfc


# In[219]:


accuracy_score(mp_test_y,pred_rfc)


# # random forest Ada boost

# In[220]:


from sklearn.ensemble import AdaBoostClassifier
add_rfc=AdaBoostClassifier(rfc_mp,n_estimators=20)


# In[221]:


add_rfc.fit(mp_train_x,mp_train_y)


# In[222]:


pred_add_rfc=add_rfc.predict(mp_test_x)


# In[223]:


tab_add_rfc=confusion_matrix(mp_test_y,pred_add_rfc)


# In[224]:


tab_add_rfc


# In[225]:


accuracy_score(mp_test_y,pred_add_rfc)


# In[ ]:





# # Day 12

# # Naive Bayes

# In[ ]:


# Naive Bayes
# steps to be followed

#data import
#data cleaning-->null,replace
#Sampling-->train_test_splite

#from sklearn.naive_bayes import MultinomialNB
#nb=MultinomialNB()

#Build Model-->fit
#Pred_train,pred_test
#import confusion_matrix,accuracy_score
#mat_test=confusion_matrix(sug_test_y,pred_test)--->build Confusion matrix
#accuracy_score


# To be taken as note
# 1) data should be numeric and Binomile only
# 2) confusion matrix should be not class imblance, if than need to do over sampling
# 3) to make best model use hyperparameter
# 4) model perfrom poor due to check all x varible with y target varible which are dependent on each other so chances
# of getting error is high


# In[ ]:


import pandas as pd


# In[ ]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\trainRF.csv")


# In[ ]:


mp=pd.read_csv(r"C:\Users\user\Desktop\MLA\trainRF.csv")


# In[ ]:


mp.isnull().sum()[mp.isnull().sum()>0]


# In[ ]:


from sklearn.model_selection import train_test_split
mp_train,mp_test=train_test_split(mp,test_size=.2)


# In[ ]:


mp_train_x=mp_train.iloc[::,:-1]
mp_train_y=mp_train.iloc[::,-1]


# In[ ]:


mp_test_x=mp_test.iloc[::,:-1]
mp_test_y=mp_test.iloc[::,-1]


# In[ ]:


from sklearn.naive_bayes import MultinomialNB
nb=MultinomialNB()


# In[ ]:


nb.fit(mp_train_x,mp_train_y)


# In[ ]:


pred=nb.predict(mp_train_x)


# In[ ]:


from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,f1_score


# In[ ]:


tab=confusion_matrix(mp_train_y,pred)


# In[ ]:


tab


# In[ ]:


accuracy_score(mp_train_y,pred)


# In[ ]:


precision_score(mp_train_y,pred,average='macro')


# In[ ]:


recall_score(mp_train_y,pred,average='macro')


# In[ ]:


f1_score(mp_train_y,pred,average='macro')


# In[ ]:





# # Unsupervised

# # Day 13

# # Kmeans

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



# In[ ]:


import pandas as pd


# In[ ]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\mall_kmeans.csv")


# In[ ]:


mall=pd.read_csv(r"C:\Users\user\Desktop\MLA\mall_kmeans.csv")


# In[ ]:


mall=mall.drop(['CustomerID'],axis=1)


# In[ ]:


mall.rename(columns={'Annual Income (k$)':'Anuincome','Spending Score (1-100)':'spendingscore'},inplace=True)


# In[ ]:


mall.isnull().sum()[mall.isnull().sum()>0]


# In[ ]:


mall.Genre.value_counts()


# In[ ]:


mall.Genre.replace({'Female':0,'Male':1},inplace=True)


# In[ ]:


mall.head()


# In[ ]:


from sklearn.cluster import KMeans
kmean_mall=KMeans(n_clusters=4)


# In[ ]:


kmean_mall.fit(mall)


# In[ ]:


kmean_mall.labels_


# In[ ]:


len(kmean_mall.labels_)


# In[ ]:


pd.DataFrame(kmean_mall.labels_).value_counts()


# In[ ]:


cluster_center=pd.DataFrame(kmean_mall.cluster_centers_)


# In[ ]:


cluster_center


# In[ ]:


cluster_center.columns=mall.columns


# In[ ]:


cluster_center


# In[ ]:


kmean_mall.score(mall)


# In[ ]:


# negative score not good cluster


# In[ ]:


#Inertia measures the sum of squared distances between each data
#point and its assigned cluster center, quantifying how well the data points fit their respective clusters.


# In[ ]:


ssd=[]
for k in range(1,12):
    kmean_mall=KMeans(n_clusters=k)
    kmean_mall.fit(mall)
    score=kmean_mall.score(mall)
    ssd.append(score)
    print("Value of k is: ",k)


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


import numpy as np
ssd=np.abs(ssd)


# In[ ]:


plt.figure(figsize=(10,6))
plt.plot(list(range(1,12)),ssd,marker='*')
plt.grid()
plt.title("Elbow plot on mall data")
plt.xlabel("No of clusters")
plt.ylabel("SSD")


# In[ ]:


#ssd=np.round(ssd)
#ssd


# In[ ]:


#l1=ssd


# In[ ]:


#l2 = []
#for i in range(len(l1)-1):
#    res = ((l1[i] - l1[i + 1] )/ l1[i]*100)
#    l2.append(np.abs(res))


# In[ ]:


#l2


# In[ ]:


# l1[i]: The current value in the list.

# l1[i + 1]: The next value in the list.

# (l1[i] - l1[i + 1]) / l1[i] * 100: Computes the percentage change between the current and next value.

# np.abs(res): Ensures that the percentage change is always positive, regardless of the direction of change


# In[ ]:


from sklearn.cluster import KMeans
kmean_mall1=KMeans(n_clusters=6)
kmean_mall1.fit(mall)


# In[ ]:


kmean_mall1.score(mall)


# In[ ]:


# Lower SSD: Indicates better clustering, as data points are closer to their centroids.

# Higher SSD: Suggests poorer clustering, with data points more spread out from their centroids.


# In[ ]:


# Since a lower inertia indicates better clustering, the second model (kmean_mall1)
#with a score closer to zero is performing
#better in terms of how well the data points fit their assigned clusters.


# In[ ]:


pd.Series(kmean_mall1.labels_).value_counts()


# In[ ]:


mall['Cluster_number']=kmean_mall1.labels_


# In[ ]:


mall.head(20)


# In[ ]:


colormap=np.array(['red','green','blue','black','yellow','purple'])


# In[ ]:


plt.figure(figsize=(10,6))
plt.scatter(mall.Age,mall.spendingscore,c=colormap[kmean_mall1.labels_])
plt.show()


# In[ ]:


plt.figure(figsize=(8,8))
plt.scatter(mall.Age,mall.Cluster_number,c=colormap[kmean_mall1.labels_])
plt.show()


# In[ ]:





# # Data Sets

# In[ ]:


# snsdata


# In[ ]:





# In[ ]:





# # Day 14

# # Hierarchical Clustering

# In[226]:


import pandas as pd


# In[129]:


mall = pd.read_csv(r'C:\Users\user\Desktop\MLA\mall_kmeans.csv')


# In[130]:


mall.head()


# In[131]:


mall.drop('CustomerID', axis=1, inplace=True)


# In[132]:


mall.rename(columns={'Annual Income (k$)': 'Income', 'Spending Score (1-100)': 'Score'}, inplace=True)


# In[133]:


mall['Genre'].replace({'Female': 0, 'Male': 1}, inplace=True)


# In[232]:


mall.head()


# In[233]:


from sklearn.cluster import AgglomerativeClustering


# In[234]:


agg_mall = AgglomerativeClustering(n_clusters=5, linkage='ward', metric='euclidean')
#mall['Cluster'] = agg_mall.fit_predict(mall)


# In[235]:


agg_mall.fit(mall)


# In[236]:


agg_mall.labels_


# In[237]:


len(agg_mall.labels_)


# In[238]:


from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score



# In[239]:


mall['Cluster'] = agg_mall.fit_predict(mall)


# In[240]:


mall['Cluster'].value_counts()


# In[241]:


# Features only (excluding cluster labels)
X = mall.drop('Cluster', axis=1)
labels = mall['Cluster']


# In[242]:


# Evaluation metrics
sil_score = silhouette_score(X, labels)
sil_score


# In[ ]:





# In[243]:


mall.head()


# In[244]:


import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np


# In[245]:


# single, complete,ward


# In[246]:


# Dendrogram to help choose number of clusters (optional but useful)
plt.figure(figsize=(12, 6))
link_result = linkage(mall.drop('Cluster', axis=1), method='single')
dendrogram(link_result)
plt.title("Dendrogram - Hierarchical Clustering")
plt.xlabel("Customers")
plt.ylabel("Distance")
plt.grid()
plt.show()


# In[247]:


# Scatter plot: Age vs Spending Score colored by cluster
colors = np.array(['red', 'green', 'blue', 'black', 'purple'])

plt.figure(figsize=(8, 8))
plt.scatter(mall['Age'], mall['Score'], c=colors[mall['Cluster']])
plt.title("Clusters (Age vs Spending Score)")
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.grid()
plt.show()


# # Data Sets
# 

# In[ ]:


# snsdata


# In[ ]:





# # Day 15

# # PCA

# In[ ]:


import pandas as pd


# In[ ]:


#  PCA----> It is a dimensition Reduction Tech,-->reduce col. or row
# steps to be followed --> unsupervised model

#data import
#data cleaning-->null,replace
#no Sampling

#drop he col. which are not in need

#pp1=pp
#pp=pp.drop(['Sale_Price'],axis=1)

#from sklearn.preprocessing import StandardScaler
#scaler=StandardScaler()
#scaler_pp=scaler.fit_transform(pp)

#from sklearn.decomposition import PCA
#from sklearn import decomposition
#pca=PCA()
#x_pca1=pca.fit_transform(scaler_pp)-------------PCA has been performed


#pca.explained_variance_ratio_

#l1=list(pca.explained_variance_ratio_)

#pca.explained_variance_ratio_.sum()

#np.sum(l1[0:55])

#df1=pd.DataFrame(x_pca1[:,0:55])

#from sklearn.linear_model import LinearRegression
#linreg=LinearRegression()
#linreg.fit(df1,pp1.Sale_Price)

#df2=pd.DataFrame(x_pca1)
#df2.corr().round()----------------> since there is no co-relation between cols




# To be taken as note
# 1) data should be numerical variables only
# 2) PCA is dimensition reduction tech.--> reduce col. and row
# 3) it is not a feature selection we can get which col. is more siginficant
# 4)  1st principle component would be the most importanat follwed by 2nd and 3rd and so on....
# 5) pca is also use to solve problem of multi colinearity



# In[ ]:


pd.read_csv(r'C:\Users\sudha\OneDrive\Desktop\files\Files\Property_Price_Train.csv')


# In[ ]:


pp=pd.read_csv(r'C:\Users\sudha\OneDrive\Desktop\files\Files\Property_Price_Train.csv')


# In[ ]:


pp.select_dtypes(include='object').columns


# In[ ]:


pp.isnull().sum()[pp.isnull().sum()>0]  #these are the cols which contain nulls


# In[ ]:


pp=pp.drop(['Id','Fireplace_Quality','Pool_Quality','Fence_Quality','Miscellaneous_Feature','Lane_Type'],axis=1)


# In[ ]:


pp.Lot_Extent.fillna(pp.Lot_Extent.mean(),inplace=True)
#pp.Lane_Type.fillna('Grvl',inplace=True)
pp.Brick_Veneer_Type.fillna('None',inplace=True)
pp.Brick_Veneer_Area.fillna(pp.Brick_Veneer_Area.mean(),inplace=True)
pp.Basement_Height.fillna('TA',inplace=True)
pp.Basement_Condition.fillna('TA',inplace=True)
pp.Exposure_Level.fillna('NO',inplace=True)
pp.BsmtFinType1.fillna('Unf',inplace=True)
pp.BsmtFinType2.fillna('Unf',inplace=True)
pp.Electrical_System.fillna('SBrkr',inplace=True)
#pp.Fireplace_Quality.fillna('Gd',inplace=True)
pp.Garage.fillna('Attchd',inplace=True)
pp.Garage_Built_Year.fillna(pp.Garage_Built_Year.mean(),inplace=True)
pp.Garage_Finish_Year.fillna('Unf',inplace=True)
pp.Garage_Quality.fillna('TA',inplace=True)
pp.Garage_Condition.fillna('TA',inplace=True)
#pp.Pool_Quality.fillna('Gd',inplace=True)
#pp.Fence_Quality.fillna('MnPrv',inplace=True)
#pp.Miscellaneous_Feature.fillna('Shed ',inplace=True)


# In[ ]:


pp.isnull().sum()[pp.isnull().sum()>0]


# In[ ]:


from sklearn.preprocessing import LabelEncoder


# In[ ]:


le=LabelEncoder()

pp[pp.select_dtypes(include='object').columns] = pp[pp.select_dtypes(include='object').columns].apply(le.fit_transform)


# In[ ]:


pp.head()


# In[ ]:


pp.columns


# In[ ]:


pp1=pp


# In[ ]:


pp=pp.drop(['Sale_Price'],axis=1)


# In[ ]:


pp.shape


# In[ ]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


# In[ ]:


scaled_pp =scaler.fit_transform(pp)
scaled_pp


# In[ ]:


from sklearn import decomposition
from sklearn.decomposition import PCA


# In[ ]:


pca =PCA(n_components=55)  # create an instance


# In[ ]:


x_pca1=pca.fit_transform(scaled_pp)
#PCA has been performed


# In[ ]:


pca.explained_variance_ratio_


# In[ ]:


l1=list(pca.explained_variance_ratio_)


# In[ ]:


len(l1)


# In[ ]:


pca.explained_variance_ratio_.sum()


# In[ ]:


# explained_variance_ratio_: how much variance each principal component explains.

# np.sum(l1[0:55]): total variance explained by the first 55 components.


# In[ ]:


import numpy as np


# In[ ]:


np.sum(l1[0:55])


# In[ ]:


df=pd.DataFrame(x_pca1[:,0:55])


# In[ ]:


from sklearn.linear_model import LinearRegression
linreg =LinearRegression()


# In[ ]:


linreg.fit(df,pp1.Sale_Price)


# In[ ]:


linreg.score(df,pp1.Sale_Price)


# In[ ]:


# Trains a Linear Regression model using top 55 components.

# score() returns the R² value — proportion of variance in Sale_Price explained by the model.


# In[ ]:


#1st principle component would be the most importanat follwed by 2nd and 3rd and so on....


# In[ ]:


df1=pd.DataFrame(x_pca1)


# In[ ]:


df1.corr().round(3) # since there is no co-relation between cols


# In[ ]:


# Shows correlation between all PCA components. Since PCA creates orthogonal (uncorrelated)
# components, you should see near-zero correlations.


# In[ ]:


# PCA cannot be used for feature selection bcause there is not one on one mapping your
# original column and the columns after transformation


# In[ ]:


#PCA is not feature selection; it's dimensionality reduction.

#First few components explain the most variance.

#PCA reduces multicollinearity since components are uncorrelated.


# In[ ]:


# So the result is a 74×74 correlation matrix.


# In[ ]:


pp.shape


# In[ ]:


pp1.shape


# In[ ]:




