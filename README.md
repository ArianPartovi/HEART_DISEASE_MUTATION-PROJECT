# Colon Cancer Classification Using Gene Expression Data

## Objective
This project aims to predict colorectal cancer progression using gene expression features and supervised machine learning.

## Dataset
We use:
- Colorectal Cancer Gene Expression Data (features)
- Patient Data (clinical labels)
- [Colorectal Cancer Dataset (Kaggle)](https://www.kaggle.com/datasets/amandam1/colorectal-cancer-patients)

The dataset includes:
- ~63 patient samples
- ~2000 gene expression features per sample

## Features
The dataset contains gene expression measurements represented by microarray probe IDs (e.g., 117_at, 1007_s_at).
Each feature corresponds to the expression level of a gene or transcript for a given patient sample.

## Target Variable
- Dukes Stage (A–D), representing cancer progression

## Data Preprocessing
- Transposed gene expression dataset
- Merged datasets using ID_REF
- Handled missing values
- Selected relevant features

## Approach
- Supervised machine learning (classification)
- Model comparison (Logistic Regression, Random Forest, etc.)
