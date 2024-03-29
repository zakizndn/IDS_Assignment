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

"""#### Primary Dataset"""

"""###### 1) df1.shape"""
st.write('Row =', df1.shape[0])
st.write('Column =', df1.shape[1])
"""The dataset has 4920 rows and 18 columns."""

"""###### 2) df1.dtypes"""
st.write(df1.dtypes)
"""This method returns a series with the data type of each column. All of the attributes are categorical data."""

"""###### 3) df1.isnull().sum()"""
st.write(df1.isnull().sum())
"""This method gives the total count of null for each column (attribute)."""

"""###### 4) df1"""
st.write(df1)

"""###### 5) df1.sample(n = 10)"""
st.write(df1.sample(n=10))
"""This method returns a random sample of 10 rows (n = 10) from the dataset."""

"""###### 6) df1.describe()"""
st.write(df1.describe())

st.markdown("---") 

"""#### Disease Description Dataset"""

"""###### 1) df2.shape"""
st.write('Row =', df2.shape[0])
st.write('Column =', df2.shape[1])
"""The dataset has 41 rows and 2 columns."""

"""###### 2) df2.types"""
st.write(df2.dtypes)
"""This method returns a series with the data type of each column. All of the attributes are categorical data."""

"""###### 3) df2"""
st.write(df2)

st.markdown("---") 

"""#### Disease Precaution Dataset"""

"""###### 1) df3.shape"""
st.write('Row =', df3.shape[0])
st.write('Column =', df3.shape[1])
"""The dataset has 41 rows and 5 columns."""

"""###### 2) df3.types"""
st.write(df3.dtypes)
"""This method returns a series with the data type of each column. All of the attributes are categorical data."""

"""###### 3) df3"""
st.write(df3)

"""###### 4) df3.describe()"""
st.write(df3.describe())

st.markdown("<hr style='border: 10px solid #ddd;'>", unsafe_allow_html=True)

"""## Further EDA"""

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
st.plotly_chart(fig)

# Display the total number of symptoms
st.write(f'Total number of occurrences: {total_symptoms}')

# Display all symptoms and their occurrence percentages
st.write('###### Occurrences of All Symptoms:')
all_symptoms = symptom_counts.copy()
all_symptoms['Percentage of Occurrence (%)'] = (all_symptoms['Frequency'] / total_symptoms) * 100
all_symptoms.columns = ['Symptom', 'Occurrence', 'Percentage of Occurrence (%)']
st.write(all_symptoms)

st.markdown("---") 

"""#### 2. What is the most common precaution across the dataset?"""

# Extract precaution columns from the DataFrame df3
precaution_columns = df3.iloc[:, 1:]

# Get the frequency of each precaution
precaution_counts = precaution_columns.stack().value_counts().reset_index()
precaution_counts.columns = ['Precautions', 'Frequency']

# Total number of precautions
total_precautions = len(precaution_columns.stack())

# Create an interactive bar chart with plotly for precautions
fig_precautions = px.bar(precaution_counts, x='Precautions', y='Frequency', title='Distribution of Precautions',
                         labels={'Frequency': 'Frequency', 'Precaution': 'Precautions'},
                         width=3000, height=700)

# Enable scroll bar for the x-axis
fig_precautions.update_xaxes(type='category', tickangle=45)

# Display the chart for precautions
st.plotly_chart(fig_precautions)

# Display the total number of precautions
st.write(f'Total number of occurrences: {total_precautions}')

# Display all precautions and their occurrence percentages
st.write('###### Occurrences of All Precautions:')
all_precautions = precaution_counts.copy()
all_precautions['Percentage of Occurrence (%)'] = (all_precautions['Frequency'] / total_precautions) * 100
all_precautions.columns = ['Precaution', 'Occurrence', 'Percentage of Occurrence (%)']
st.write(all_precautions)

st.markdown("---") 

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

"""
###### Finding

If the first reported symptom is "abdominal pain", the dataset suggests varying likelihoods of different diseases 
associated with this symptom. Specifically, the likelihood of getting Hepatitis E is slightly higher than 
other diseases, such as Alcoholic hepatitis, Chronic cholestasis, Hepatitis B, Hepatitis D, Jaundice, 
Peptic ulcer disease, Typhoid, and Hepatitis A, all with a likelihood of approximately 11.05%.

It's important to note that this analysis focuses solely on cases where only the first reported symptom is 
considered and does not consider additional symptoms reported later in the diagnostic process. 

For more comprehensive insights, further analysis can be conducted for each subsequent reported symptom, 
providing a nuanced understanding of disease likelihoods in multi-symptomatic scenarios. 
"""

st.markdown("---") 

"""#### 4. Given the higher occurrence of the fatigue symptom, can we infer that fatigue may serve as a potential common indicator in a diverse range of diseases?"""

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

# Replace missing values with blank strings
df_present['Disease'] = df_present['Disease'].replace({pd.NA: ''})
df_not_present['Disease'] = df_not_present['Disease'].replace({pd.NA: ''})
df_depends['Disease'] = df_depends['Disease'].replace({pd.NA: ''})

# Calculate percentages
total_diseases = len(all_diseases)
percentage_present = len(df_present) / total_diseases * 100
percentage_not_present = len(df_not_present) / total_diseases * 100
percentage_depends = len(df_depends) / total_diseases * 100

# Create a summary DataFrame
summary_df = pd.DataFrame({
    'Diseases with Fatigue Present': df_present['Disease'],
    'Diseases with Fatigue Not Present': df_not_present['Disease'],
    'Diseases where Fatigue Depends on the Situation': df_depends['Disease']
})

# Display the summary table using Streamlit
st.write(summary_df)
st.write(f'Diseases with Fatigue Present: {percentage_present:.2f}%')
st.write(f'Diseases with Fatigue Not Present: {percentage_not_present:.2f}%')
st.write(f'Diseases where Fatigue Depends on the Situation: {percentage_depends:.2f}%')

"""
###### Finding
While fatigue is a prevalent symptom in the dataset, its occurrence does not universally characterize all 
diseases. The analysis reveals that:

Diseases with Fatigue Present: 
- Only 2.44% of diseases in the dataset consistently exhibit fatigue as a reported symptom.

Diseases with Fatigue Not Present: 
- A significant portion, 58.54%, shows no association with fatigue. 
- These diseases are identified as having no reported instances of fatigue.

Diseases where Fatigue Depends on the Situation: 
- Approximately 39.02% of diseases fall into a category where the presence or absence of fatigue depends on the specific situation. 
- In these cases, the reported symptomatology may or may not include fatigue for the same diseases.

This nuanced breakdown emphasizes that while fatigue is commonly reported, it is not a universal indicator 
across all diseases. The 39.02% of cases where fatigue depends on the situation highlights the complexity of 
symptomatology and the variability in reported symptoms for certain diseases. Understanding these variations is 
crucial for accurate diagnosis and effective medical interventions.
"""
