from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
# from sklearn.svm import
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder 

# define and read both datasets used in project

df = pd.read_csv('/content/drive/MyDrive/ColorectalCancerGEData.csv')
ds = pd.read_csv('/content/drive/MyDrive/ColorectalCancerPatientData.csv')

df = df.drop(columns=["Unnamed: 0"]) # drops unncessary columns
df = df.set_index("ID_REF") # sets Gene IDs as index
df = df.T # Transpose dataset
print(df.shape)

# inspection of both datasets prior to merging, checks for ID Matching
# Ensuring data formatting, mainly for the IDs
print(df.index[:5])
print(ds.columns)
print(ds.head())

# Fix ID Format
df['SampleID'] = df.index.str.replace('GSM', '')
# Create SampleID in ds from its ID_REF column to match df's SampleID
ds['SampleID'] = ds['ID_REF'].str.replace('GSM', '').astype(str)
# Merge two datasets
merged = df.merge(ds, on='SampleID')
# Get Rid of Missing Labels
merged = merged.dropna(subset=['Dukes Stage'])

# Split X and y
y = merged['Dukes Stage']
x = merged.drop(columns=['Dukes Stage', 'SampleID'])

#Encode Label Information from A,B,C,D to 1,2,3,4
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Check Results
print(merged.shape)
print(y.value_counts())

# current program to transpose gene expression dataset, and output both datasets 