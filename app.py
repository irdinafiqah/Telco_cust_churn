import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sweetviz as sv
import tempfile

# Load the dataset
@st.cache
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/irdinafiqah/Telco_cust_churn/main/WA_Fn-UseC_-Telco-Customer-Churn.csv')
    return df

df = load_data()

# Title of the web app
st.title('Telco Customer Churn Analysis')

# Display sample of data
if st.checkbox('Show Sample Data'):
    st.write(df.sample(n=5))

# Display dataset shape
st.write('Dataset Shape:', df.shape)

# Check for missing values
st.write('Missing Values:', df.isnull().sum())

# Analyze the dataset
advert_report = sv.analyze(df)

# Display the Sweetviz report
st.write(advert_report)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')

# Plot MonthlyCharges vs TotalCharges
st.subheader('Monthly Charges vs Total Charges')
fig, ax = plt.subplots()
sns.regplot(data=df, x='MonthlyCharges', y='TotalCharges', ax=ax)
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
plt.savefig(temp_file.name)
st.image(temp_file.name)
temp_file.close()
plt.close()

# Display correlation heatmap
st.subheader('Correlation Heatmap')
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", linewidth=.5)
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
plt.savefig(temp_file.name)
st.image(temp_file.name)
temp_file.close()
plt.close()

# Display value counts of Churn
st.subheader('Churn Value Counts')
st.write(df['Churn'].value_counts())
