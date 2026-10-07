#!/usr/bin/env python
# coding: utf-8

# ## Trip Advisor reviews using the dataset to decide the positive or negative predict the review.

# #### Pipeline:
# ### Review Data → Cleaning → Text Preprocessing → TF-IDF → Train/Test Split → Naive Bayes → Prediction → Evaluation

# In[1]:


import warnings
warnings.filterwarnings("ignore")


# In[2]:


import pandas as pd


# In[3]:


pd.read_csv(r"C:\Users\user\Desktop\MLA\Trip_advisor_review.csv")


# In[4]:


df=pd.read_csv(r"C:\Users\user\Desktop\MLA\Trip_advisor_review.csv")
df


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df['Rating'].value_counts()


# In[9]:


df.info()


# In[10]:


df.isnull().sum()


# # sentiment columns

# In[11]:


df['Sentiment']=df['Rating'].apply(
    lambda x: 'Positive' if x >=4 else 'Negative')


# In[12]:


df[['Review','Rating','Sentiment']].head()


# In[13]:


df['Sentiment'].value_counts()


# In[16]:


x=df["Review"]
y=df["Sentiment"]


# # train test split

# In[ ]:





# In[18]:


X = df["Review"].astype(str)
y = df["Sentiment"]

# Check
print("X created:", X.shape)
print("y created:", y.shape)
print(X.head())
print(y.head())


# # train test  split

# In[20]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)


# In[21]:


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words='english'
)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

print("X_train_tfidf:", X_train_tfidf.shape)
print("X_test_tfidf:", X_test_tfidf.shape)


# In[22]:


from sklearn.naive_bayes import MultinomialNB

nb_model = MultinomialNB()

nb_model.fit(X_train_tfidf, y_train)

print("Model training completed successfully!")


# In[23]:


y_pred = nb_model.predict(X_test_tfidf)

print(y_pred[:10])


# In[24]:


review = ["The hotel was excellent and I really enjoyed my stay"]

review_tfidf = tfidf.transform(review)

prediction = nb_model.predict(review_tfidf)

print("Sentiment:", prediction[0])


# In[30]:


review = ["The hotel room was dirty and the service was very bad"]

review_tfidf = tfidf.transform(review)

prediction = nb_model.predict(review_tfidf)

print("Sentiment:", prediction[0])


# In[32]:


from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# In[ ]:





# In[33]:


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Negative", "Positive"]
)

disp.plot()
plt.title("Naive Bayes - Confusion Matrix")
plt.show()


# # hyperparamaneter tunings

# In[35]:


from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

alphas = [0.01, 0.1, 0.5, 1, 2, 5]

for alpha in alphas:
    model = MultinomialNB(alpha=alpha)
    model.fit(X_train_tfidf, y_train)

    pred = model.predict(X_test_tfidf)
    acc = accuracy_score(y_test, pred)

    print("Alpha:", alpha, "Accuracy:", round(acc, 4))


# In[39]:


best_alpha = 0.5   
final_nb = MultinomialNB(alpha=best_alpha)

final_nb.fit(X_train_tfidf, y_train)

final_pred = final_nb.predict(X_test_tfidf)

print("Final Naive Bayes model trained successfully!")


# In[40]:


from sklearn.metrics import accuracy_score, classification_report

print("Final Accuracy:", accuracy_score(y_test, final_pred))

print("\nFinal Classification Report:")
print(classification_report(y_test, final_pred))


# In[41]:


review = ["The hotel was excellent and I really enjoyed my stay"]

review_tfidf = tfidf.transform(review)

prediction = final_nb.predict(review_tfidf)

print("Review:", review[0])
print("Predicted Sentiment:", prediction[0])


# In[42]:


review = ["The hotel was dirty and the service was very bad"]

review_tfidf = tfidf.transform(review)

prediction = final_nb.predict(review_tfidf)

print("Review:", review[0])
print("Predicted Sentiment:", prediction[0])


# In[ ]:




