#!/usr/bin/env python
# coding: utf-8

# ## Starting with Logistic Regression
# # Goal: Customer company churn yes or with company No, so that predict .

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


import warnings
warnings.filterwarnings("ignore")


# In[3]:


df=pd.read_csv(r"C:\Users\user\Desktop\MLA\Churn.csv")
df


# In[4]:


import pandas as pd


# In[9]:


print(df.shape)
print(df.head)
print(df.tail)
print(df.info)


# In[11]:


df["Churn"].value_counts()


# In[12]:


x=df.drop("Churn",axis=1)
y=df["Churn"]


# In[13]:


x.head()


# In[14]:


y.head()


# In[15]:


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


# In[16]:


x_train.dtypes


# In[17]:


x=x.drop("customerID",axis=1)
x


# In[18]:


x


# In[19]:


X = df.drop("Churn", axis=1)
X = X.drop("customerID", axis=1)

y = df["Churn"]


# In[20]:


y


# In[21]:


x


# In[22]:


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# In[23]:


x


# In[24]:


X_train = pd.get_dummies(X_train, drop_first=True)
X_test = pd.get_dummies(X_test, drop_first=True)


# In[25]:


x


# In[26]:


x_train


# In[27]:


x_test


# In[29]:


x_train.dtypes


# In[28]:


x=df.drop("Churn",axis=1)


# In[29]:


x


# In[32]:


x=df.drop("customerID",axis=1)


# In[33]:


x


# In[34]:


y=df["Churn"]


# In[35]:


y


# In[36]:


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# In[37]:


X_train.columns


# In[38]:


X_train = pd.get_dummies(X_train, drop_first=True)
X_test = pd.get_dummies(X_test, drop_first=True)


# In[39]:


X_train, X_test = X_train.align(
    X_test,
    join="left",
    axis=1,
    fill_value=0
)


# In[40]:


y_train = y_train.map({"No": 0, "Yes": 1})
y_test = y_test.map({"No": 0, "Yes": 1})


# In[41]:


y_train.head()


# In[42]:


from sklearn.linear_model import LogisticRegression


# In[43]:


model = LogisticRegression(max_iter=1000)


# In[44]:


model.fit(X_train, y_train)


# In[45]:


print(X_train.shape)
print(X_test.shape)
print(X_train.columns.equals(X_test.columns))


# In[46]:


df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)


# In[47]:


sns.countplot(data=df, x='Churn')
plt.title('Customer Churn Distribution')
plt.show()


# In[48]:


y_pred = model.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))


# In[49]:


from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Logistic Regression Confusion Matrix')
plt.show()


# ### Decision Tree algorithum 

# ####  Decision tree algorithum using for the build the model features depend on data  to take decision tree like  structure.

# In[50]:


from sklearn.tree import DecisionTreeClassifier

dt_model = DecisionTreeClassifier(
    random_state=42
)


# # fit the model

# In[51]:


dt_model.fit(X_train, y_train)


# ## Make Predictionn

# In[52]:


dt_pred = dt_model.predict(X_test)


# # Evalute the model

# In[53]:


from sklearn.metrics import accuracy_score, classification_report

print("Accuracy:",
      accuracy_score(y_test, dt_pred))

print(classification_report(y_test, dt_pred))


# In[54]:


from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, dt_pred)

sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Decision Tree Confusion Matrix')
plt.show()


# ## Logistic Regression in probability based predictionn do, and the decision tree in feature based values depend rule prediction do.

# ## Raandom Forest

# In[55]:


from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)


# In[56]:


# evalution


# In[57]:


from sklearn.metrics import classification_report

print(classification_report(y_test, rf_pred))


# ### comaparision the three models  results:

# In[58]:


from sklearn.metrics import accuracy_score, recall_score, f1_score
import pandas as pd

results = pd.DataFrame({
    'Model': ['Logistic Regression',
              'Decision Tree',
              'Random Forest'],
    'Accuracy': [
        accuracy_score(y_test, y_pred),
        accuracy_score(y_test, dt_pred),
        accuracy_score(y_test, rf_pred)
    ],
    'Churn Recall': [
        recall_score(y_test, y_pred),
        recall_score(y_test, dt_pred),
        recall_score(y_test, rf_pred)
    ],
    'Churn F1-score': [
        f1_score(y_test, y_pred),
        f1_score(y_test, dt_pred),
        f1_score(y_test, rf_pred)
    ]
})

print(results.round(2))


# ## SVM algorithum 

# In[59]:


from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


# # create the fit model

# In[68]:


svm_model = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='rbf'))
])

svm_model.fit(X_train, y_train)


# # make predictions

# In[61]:


svm_pred = svm_model.predict(X_test)


# # Evaluate the model

# In[62]:


from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

print("Accuracy:",
      accuracy_score(y_test, svm_pred))

print(classification_report(y_test, svm_pred))


# ## KNN algorithum

# # import  created a model

# In[63]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
knn_model = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])


# # fit the model

# In[64]:


knn_model.fit(X_train, y_train)


# # Prediction

# In[65]:


knn_pred = knn_model.predict(X_test)


# # Evalution

# In[74]:


from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

print("Accuracy:",
      accuracy_score(y_test, knn_pred))

print(classification_report(y_test, knn_pred))


# In[77]:


from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[78]:


knn_model = KNeighborsClassifier(n_neighbors=5)

knn_model.fit(X_train_scaled, y_train)


# # prediction

# In[79]:


knn_pred = knn_model.predict(X_test_scaled)


# In[82]:


# accuracy


# In[80]:


print("KNN Accuracy:", accuracy_score(y_test, knn_pred))


# In[81]:


print(classification_report(y_test, knn_pred))


# In[83]:


# model comparaision


# In[84]:


from sklearn.metrics import accuracy_score, recall_score, f1_score

results = pd.DataFrame({
    'Model': [
        'Logistic Regression',
        'Decision Tree',
        'Random Forest',
        'SVM',
        'KNN'
    ],
    'Accuracy': [
        accuracy_score(y_test, y_pred),
        accuracy_score(y_test, dt_pred),
        accuracy_score(y_test, rf_pred),
        accuracy_score(y_test, svm_pred),
        accuracy_score(y_test, knn_pred)
    ],
    'Churn Recall': [
        recall_score(y_test, y_pred),
        recall_score(y_test, dt_pred),
        recall_score(y_test, rf_pred),
        recall_score(y_test, svm_pred),
        recall_score(y_test, knn_pred)
    ],
    'Churn F1-score': [
        f1_score(y_test, y_pred),
        f1_score(y_test, dt_pred),
        f1_score(y_test, rf_pred),
        f1_score(y_test, svm_pred),
        f1_score(y_test, knn_pred)
    ]
})

print(results.round(2))


# In[85]:


# hyperparameter tunning


# In[86]:


from sklearn.metrics import accuracy_score

k_values = range(1, 16)
accuracy = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    pred = knn.predict(X_test_scaled)
    accuracy.append(accuracy_score(y_test, pred))

for k, acc in zip(k_values, accuracy):
    print(k, round(acc, 3))


# In[87]:


best_k = k_values[accuracy.index(max(accuracy))]

print("Best K:", best_k)
print("Best Accuracy:", max(accuracy))


# In[92]:


best_knn = KNeighborsClassifier(n_neighbors=1)

best_knn.fit(X_train_scaled, y_train)

knn_final_pred = best_knn.predict(X_test_scaled)


# In[93]:


print("KNN Accuracy:", accuracy_score(y_test, knn_final_pred))
print(classification_report(y_test, knn_final_pred))


# In[94]:


# confusion matrix


# In[95]:


from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, knn_final_pred)

sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("KNN Confusion Matrix")
plt.show()


# In[ ]:




