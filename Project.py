from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
import numpy as np
df = pd.read_csv('/content/drive/MyDrive/ColorectalCancerGEData.csv')
df = df.drop(columns=["Unnamed: 0"]) # drops unncessary columns
df = df.set_index("ID_REF") # sets Gene IDs as index 
df = df.T # Transpose dataset
print(df.shape)
df.head()
ds = pd.read_csv('/content/drive/MyDrive/ColorectalCancerPatientData.csv')
ds.head()

# current program to transpose gene expression dataset, and output both datasets 