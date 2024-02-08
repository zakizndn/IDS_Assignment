# -*- coding: utf-8 -*-
"""assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16vl4mdCcC_R658tViFUG4MVk6z5mZbQr

# Assignment

[Disease Symptom Prediction](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset?select=dataset.csv)

(1) RapidMiner - EDA

(2) Python - EDA and Machine Learning
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import streamlit as st
import plotly.express as px

df1 = pd.read_csv("dataset.csv")
df2 = pd.read_csv("disease_description.csv")
df3 = pd.read_csv("symptom_precaution.csv")
df4 = pd.read_csv("symptom_severity.csv")

"""## Exploratory Data Analysis"""

"""#### 1.0 Primary Dataset"""

"""###### 1.1 df1.shape"""
st.write('Row =', df1.shape[0])
st.write('Column =', df1.shape[1])
"""The dataset has 4920 rows and 18 columns."""

"""###### 1.2 df1.dtypes"""
st.write(df1.dtypes)
"""This method returns a series with the data type of each column. All of the attributes are categorical data."""

"""###### 1.3 df1.isnull().sum()"""
st.write(df1.isnull().sum())
"""This method gives the total count of null for each column (attribute)."""

"""###### 1.4 df1"""
st.write(df1)

"""###### 1.5 df1.sample(n = 10)"""
st.write(df1.sample(n=10))
"""This method returns a random sample of 10 rows (n = 10) from the dataset."""

"""###### 1.6 df1.describe()"""
st.write(df1.describe())



"""#### 2.0 Disease Description Dataset"""

"""###### 2.1 df2.shape"""
st.write('Row =', df2.shape[0])
st.write('Column =', df2.shape[1])
"""The dataset has 41 rows and 2 columns."""

"""###### 2.2 df2.types"""
st.write(df2.dtypes)
"""This method returns a series with the data type of each column. All of the attributes are categorical data."""

"""###### 2.3 df2"""
st.write(df2)


"""#### 3.0 Disease Precaution Dataset"""

"""###### 3.1 df3.shape"""
st.write('Row =', df3.shape[0])
st.write('Column =', df3.shape[1])
"""The dataset has 41 rows and 5 columns."""

"""###### 3.2 df3.types"""
st.write(df3.dtypes)
"""This method returns a series with the data type of each column. All of the attributes are categorical data."""

"""###### 3.3 df3"""
st.write(df3)

"""###### 3.4 df3.describe()"""
st.write(df3.describe())

st.markdown("---") 

"""## The Question"""

"""#### 1. What is the most common symptom reported?"""

# Extract symptom columns from the DataFrame
symptom_columns = df1.iloc[:, 1:]

# Get the frequency of each symptom
symptom_counts = symptom_columns.stack().value_counts().reset_index()
symptom_counts.columns = ['Symptom', 'Frequency']

# Total number of symptoms
total_symptoms = len(symptom_columns.stack())

# Create an interactive bar chart with plotly
fig = px.bar(symptom_counts, x='Symptom', y='Frequency', title='Distribution of Symptoms',
             labels={'Frequency': 'Frequency', 'Symptom': 'Symptoms'},
             width=3000, height=700)

# Enable scroll bar for the x-axis
fig.update_xaxes(type='category', tickangle=45)

# Streamlit app
st.title('Symptom Distribution Dashboard')
st.plotly_chart(fig)

# Display the total number of symptoms
st.write(f'Total number of symptoms: {total_symptoms}')

# Display all symptoms and their occurrence percentages
st.write('All Symptoms:')
all_symptoms = symptom_counts.copy()
all_symptoms['Percentage of Occurrence (%)'] = (all_symptoms['Frequency'] / total_symptoms) * 100
all_symptoms.columns = ['Symptom', 'Occurrence', 'Percentage of Occurrence (%)']
st.write(all_symptoms)

"""#### 2. What is the most common precaution across the dataset for preventing the transmission of diseases?"""

# Extract precaution columns from the DataFrame
precaution_columns = df4.iloc[:, 1:]

# Get the frequency of each precaution
precaution_counts = precaution_columns.stack().value_counts().reset_index()
precaution_counts.columns = ['Precautions', 'Frequency']

# Total number of precautions
total_symptoms = len(precaution_columns.stack())

# Create an interactive bar chart with plotly
fig = px.bar(precaution_counts, x='Precautions', y='Frequency', title='Distribution of Precautions',
             labels={'Frequency': 'Frequency', 'Precaution': 'Precaution'},
             width=3000, height=700)

# Enable scroll bar for the x-axis
fig.update_xaxes(type='category', tickangle=45)

# Show the plot
fig.show()

# Extract precaution columns from the DataFrame
precaution_columns = df4.iloc[:, 1:]

# Get the frequency of each sympprecautiontom
precaution_counts = precaution_columns.stack().value_counts()

# Total number of precautions
total_precautions = len(precaution_columns.stack())

# Get all precautions
all_precautions = precaution_counts.reset_index()
all_precautions.columns = ['Precaution', 'Occurrence']

# Convert 'Occurrence' column to numeric and handle errors
all_precautions['Occurrence'] = pd.to_numeric(all_precautions['Occurrence'], errors='coerce')

# Remove rows with NaN values
all_precautions = all_precautions.dropna()

# Calculate the percentage
all_precautions['Percentage of Occurrence (%)'] = (all_precautions['Occurrence'] / total_precautions) * 100

# Set display options for pandas to show 2 decimal places
pd.set_option('display.float_format', '{:.2f}'.format)

# Display all precautions
all_precautions[['Precaution', 'Occurrence', 'Percentage of Occurrence (%)']]

"""#### 3. Is there a correlation between specific symptoms and the occurrence of a particular disease in the dataset?"""

# Extract symptom columns from the DataFrame
symptom_columns = df1.iloc[:, 1:]

# Reshape the DataFrame using melt
melted_df = pd.melt(df1, id_vars=['Disease'], value_vars=df1.columns[1:])

# Drop rows with NaN values
melted_df = melted_df.dropna()

# Rename the 'value' column to 'Symptom'
melted_df = melted_df.rename(columns={'value': 'Symptom'})

# Count the frequency of each symptom for each disease
symptom_counts = melted_df.groupby(['Disease', 'Symptom']).size().reset_index(name='Frequency')

# Display
symptom_counts

# Reshape the DataFrame using melt
melted_df = pd.melt(df1, id_vars=['Disease'], value_vars=df1.columns[1:])

# Drop rows with NaN values
melted_df = melted_df.dropna()

# Count the frequency of each symptom for each disease
symptom_counts = melted_df.groupby(['Disease', 'value']).size().reset_index(name='Frequency')

# Calculate the total occurrences of each symptom
total_occurrences = symptom_counts.groupby('value')['Frequency'].sum().reset_index(name='Total')

# Merge the total occurrences with the symptom_counts table
symptom_counts = pd.merge(symptom_counts, total_occurrences, left_on='value', right_on='value')

# Calculate the percentage likelihood for each disease
symptom_counts['Percentage'] = (symptom_counts['Frequency'] / symptom_counts['Total']) * 100
symptom_counts['Percentage'] = symptom_counts['Percentage'].round(2)

# Display the resulting DataFrame
percentage_likelihood = symptom_counts[['value', 'Disease', 'Percentage']]
percentage_likelihood = percentage_likelihood.sort_values(by=['value', 'Percentage'], ascending=[True, False])
percentage_likelihood.reset_index(drop=True, inplace=True)
percentage_likelihood.columns = ['Symptom', 'Disease', 'Likelihood of getting the disease (%)']

percentage_likelihood

"""#### 4. Given the higher occurrence of the fatigue symptom, can we infer that fatigue may serve as a potential common indicator in a diverse range of diseases?"""

from tabulate import tabulate

# Find diseases where fatigue may or may not be a symptom
all_diseases = df1['Disease'].unique()

# Create DataFrames to store diseases with fatigue present, not present, or depends
df_present = pd.DataFrame(columns=['Disease'])
df_not_present = pd.DataFrame(columns=['Disease'])
df_depends = pd.DataFrame(columns=['Disease'])

# Iterate through diseases
for disease in all_diseases:
    # Check if there is at least one row for the disease where 'fatigue' is present in any symptom column
    fatigue_present = any(df1[df1['Disease'] == disease].apply(lambda row: 'fatigue' in ' '.join(row.dropna()), axis=1))

    # Check if there is at least one row for the disease where 'fatigue' is absent in all symptom columns
    fatigue_absent = any(df1[df1['Disease'] == disease].apply(lambda row: 'fatigue' not in ' '.join(row.dropna()), axis=1))

    # Categorize diseases based on fatigue presence or absence
    if fatigue_present and fatigue_absent:
        df_depends = pd.concat([df_depends, pd.DataFrame({'Disease': [disease]})], ignore_index=True)
    elif fatigue_present:
        df_present = pd.concat([df_present, pd.DataFrame({'Disease': [disease]})], ignore_index=True)
    elif fatigue_absent:
        df_not_present = pd.concat([df_not_present, pd.DataFrame({'Disease': [disease]})], ignore_index=True)

# Calculate percentages
total_diseases = len(all_diseases)
percentage_present = len(df_present) / total_diseases * 100
percentage_not_present = len(df_not_present) / total_diseases * 100
percentage_depends = len(df_depends) / total_diseases * 100

# Display the resulting table
table_present = tabulate(df_present, headers='keys', tablefmt='pretty', showindex=False)
table_not_present = tabulate(df_not_present, headers='keys', tablefmt='pretty', showindex=False)
table_depends = tabulate(df_depends, headers='keys', tablefmt='pretty', showindex=False)

print("\nDiseases with Fatigue Present:")
print(table_present)
print("\nDiseases with Fatigue Not Present:")
print(table_not_present)
print("\nDiseases where Fatigue Depends on the Situation:")
print(table_depends)
print("\nPercentage of Diseases with Fatigue Present: {:.2f}%".format(percentage_present))
print("Percentage of Diseases with Fatigue Not Present: {:.2f}%".format(percentage_not_present))
print("Percentage of Diseases where Fatigue Depends on the Situation: {:.2f}%".format(percentage_depends))
