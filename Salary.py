#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings


warnings.filterwarnings("ignore")


# In[2]:


get_ipython().system('pip show tensorflow')


# In[3]:


# Data Manipulation
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

# ANN
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Evaluation
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# In[4]:


# Load dataset
df = pd.read_csv(r"C:\Users\user\Documents\Desktop\AI\Salary_prediction.csv")

# First 5 rows
df.head()


# In[5]:


print(df.shape)

df.info()

df.describe()

df.isnull().sum()


# In[6]:


# Remove duplicate rows
df = df.drop_duplicates()

# Select the target column
# Change "Salary" if your actual salary column has a different name
target = "AnnualSalary"

# Remove rows with missing values
df = df.dropna()

# Separate input and output
X = df.drop(columns=[target])
y = df[target]

# Convert categorical input columns into numeric columns
X = pd.get_dummies(X, drop_first=True, dtype=int)

print("Input shape:", X.shape)
print("Target shape:", y.shape)


# In[7]:


# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale input features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)


# In[8]:


model = Sequential([
    # input+hidden layer 1
    Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
    Dropout(0.30),

    Dense(32, activation="relu"),
    Dropout(0.30),

    Dense(16, activation="relu"),

    Dense(8, activation="relu"),

    Dense(4, activation="relu"),

    Dense(2, activation="relu"),

    Dense(1, activation="linear")
])


# Display model architecture
model.summary()


# In[9]:


# Compile model

from tenserflow.keras.optimizers import Adam
model.compile(
    optimizer=adam(learning_rate=0.001),
    loss="mse",
    metrics=["mae"]
)


# In[ ]:


history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=64,
    validation_split=0.2,
    verbose=1
)


# In[11]:


#fig data
plt.figure(figsize=(8,5))

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")

plt.legend()

plt.show()


# In[15]:


from tensorflow.keras.callbacks import EarlyStopping


# In[16]:


#Train the model
early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=64,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)


# In[17]:


print(model)


# In[18]:


#Evaluate the model
y_pred = model.predict(X_test).flatten()

print("MAE:", mean_absolute_error(y_test, y_pred))

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:", rmse)

print("R2 Score:", r2_score(y_test, y_pred))


# In[19]:


#Compare actual and predicted salary
result = pd.DataFrame({
    "Actual Salary": y_test.values,
    "Predicted Salary": y_pred
})

print(result.head(10))


# In[20]:


#run the model and succesfully run
model.save("salary_ann_model.keras")

print("ANN model saved successfully!")


# In[ ]:




