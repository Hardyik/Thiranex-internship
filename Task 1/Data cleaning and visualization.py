# Task 1: Data Cleaning & Visualization Project
# Name: Hardik Prakash Kotawdekar
# Intern ID: THX-MAY226-4357

# 1. importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load the Dataset
df = pd.read_csv('sample.csv')
print(df.head())
print(df.info())

# 3: Check Dataset Information
print(df.info())
print(df.describe())

# 4. Check for missing values
print(df.isnull().sum())
# Handling the missing values form dataset
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 5. checking for duplicate rows
print(df.duplicated().sum())
# removing duplicate rows
df.drop_duplicates(inplace=True)

# 6. detect outliers
plt.figure(figsize=(6,4))
sns.boxplot(x=df['Fare'])
plt.title('Boxplot of Fare')
plt.show()

# 7 data visualize
# 1. Gender Distrubution
plt.figure(figsize=(6,4))
sns.countplot(x="Sex", data=df)
plt.title('Gender distrubution')
plt.show()
# 2 Age Distrubution
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=5, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()
# 3 Fare Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Fare'], bins=5, kde=True)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.show()
# 4 Age Vs Fare Scatter plot 
plt.figure(figsize=(6,4))
sns.scatterplot(x='Age', y='Fare', hue='Sex', data=df)
plt.title('Age vs Fare')
plt.show()

# Final cleaned dataset
print(df.head())
