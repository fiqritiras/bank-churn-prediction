# Bank Churn Prediction
## Overview
This project aims to predict customer churn using unsupervised machine learning technique. Customer churn in a bank refers to when a customer stops using the company's products. By predicting which customers are likely to churn, businesses can take actions to retain them. The project includes data preprocessing, model training, evaluation, and deployment of the churn prediction model.

## Dataset
The dataset used is from public dataset published at Kaggle (https://www.kaggle.com/datasets/saurabhbadole/bank-customer-churn-prediction-dataset). The dataset contains information on customer demographics, services, and behavior. It includes the following key features:

- CustomerId: A unique identifier for each customer
- Surname: The surname of the customer
- CreditScore: The credit score of the customer
- Geography: The geographical location of the customer (e.g., country or region)
- Gender: The gender of the customer
- Age: The age of the customer
- Tenure: The number of years the customer has been with the bank
- Balance: The account balance of the customer
- NumOfProducts: The number of bank products the customer has
- HasCrCard: Indicates whether the customer has a credit card (binary: yes/no)
- IsActiveMember: Indicates whether the customer is an active member (binary: yes/no)
- EstimatedSalary: The estimated salary of the customer
- Exited: Indicates whether the customer has exited the bank (binary: yes/no)

## Methodology
1. **Data Preprocessing**: Clean and prepare the dataset, checking missing values
2. **Exploratory Data Analysis (EDA)**: Visualize data to identify trends and relationships between features and churn
3. **Feature Engineering**: Encoding categorical features using label encoding, scaling numerical features to improve model performance
4. **Modeling**: Train various classification models to predict churn, including:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - Support Vector Machine
   - K-Nearest Neighbors
5. **Model Evaluation**: Assess model performance using metrics like accuracy, precision, recall, F1-score, and also in visualization confusion matrix.

## Conclusion
The analysis successfully identified key factors influencing customer churn and built a predictive model using Random Forest Classifier with 86% accuracy. The insights gained from this analysis can help the bank implement targeted retention strategies and enhance customer satisfaction.
