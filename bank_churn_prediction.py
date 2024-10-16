# -*- coding: utf-8 -*-
"""Bank Churn Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/129M8EwK7c3m062b1s9Rrre8dGX5OQb24
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Load the dataset
df = pd.read_csv('/content/Churn_Modelling.csv')

# Preview the data
df.head()

# Check for missing values
df.isnull().sum()

# Summary statistics
df.describe()

# Encoding categorical variables
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Geography'] = df['Geography'].map({'France': 1, 'Spain': 2, 'Germany': 2})

# Drop unnecessary columns
df = df.drop(columns=['RowNumber', 'CustomerId', 'Surname'])

#Check correlation
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f')
plt.show()

# Define features (X) and target variable (y)
X = df.drop(columns='Exited')
y = df['Exited']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data (optional, but beneficial for models like SVM)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Logistic Regression Model
log_model = LogisticRegression()
log_model.fit(X_train, y_train)

# Predictions and Evaluation
log_pred = log_model.predict(X_test)
print("Logistic Regression Accuracy:", accuracy_score(y_test, log_pred))
print(classification_report(y_test, log_pred))

from sklearn.metrics import ConfusionMatrixDisplay

# Confusion matrix for Logistic Regression
ConfusionMatrixDisplay.from_estimator(log_model, X_test, y_test)
plt.title('Logistic Regression Confusion Matrix')
plt.show()

# Decision Tree Classifier
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)

# Predictions and Evaluation
tree_pred = tree_model.predict(X_test)
print("Decision Tree Accuracy:", accuracy_score(y_test, tree_pred))
print(classification_report(y_test, tree_pred))

# Confusion matrix for Decision Tree
ConfusionMatrixDisplay.from_estimator(tree_model, X_test, y_test)
plt.title('Decision Tree Confusion Matrix')
plt.show()

# Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# Predictions and Evaluation
rf_pred = rf_model.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, rf_pred))
print(classification_report(y_test, rf_pred))

# Confusion matrix for Random Forest
ConfusionMatrixDisplay.from_estimator(rf_model, X_test, y_test)
plt.title('Random Forest Confusion Matrix')
plt.show()

# Support Vector Classifier
svm_model = SVC()
svm_model.fit(X_train, y_train)

# Predictions and Evaluation
svm_pred = svm_model.predict(X_test)
print("SVM Accuracy:", accuracy_score(y_test, svm_pred))
print(classification_report(y_test, svm_pred))

# Confusion matrix for SVM
ConfusionMatrixDisplay.from_estimator(svm_model, X_test, y_test)
plt.title('SVM Confusion Matrix')
plt.show()

# K-Nearest Neighbors Classifier
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Predictions and Evaluation
knn_pred = knn_model.predict(X_test)
print("KNN Accuracy:", accuracy_score(y_test, knn_pred))
print(classification_report(y_test, knn_pred))

# Confusion matrix for KNN
ConfusionMatrixDisplay.from_estimator(knn_model, X_test, y_test)
plt.title('KNN Confusion Matrix')
plt.show()

from sklearn.model_selection import GridSearchCV

# Example of hyperparameter tuning for Random Forest
param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20, 30]}
grid_rf = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_rf.fit(X_train, y_train)

# Best parameters
print("Best parameters:", grid_rf.best_params_)

# Evaluate tuned model
grid_pred = grid_rf.predict(X_test)
print("Tuned Random Forest Accuracy:", accuracy_score(y_test, grid_pred))
print(classification_report(y_test, grid_pred))

#Create visualization for feature importances
feature_names = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
importances = pd.Series(rf_model.feature_importances_, index=feature_names)

#Plot
importances.plot(kind='barh')
plt.title('Feature Importances')
plt.show()

import joblib

# Save the Random Forest Classifier model
joblib.dump(rf_model, 'rf_model_bank_churn.pkl')