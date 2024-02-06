import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sweetviz as sv

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
st.pyplot(fig)

# Display correlation heatmap
st.subheader('Correlation Heatmap')
corr = df.corr(method='pearson')
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", linewidth=.5)
st.pyplot()

# Display value counts of Churn
st.subheader('Churn Value Counts')
st.write(df['Churn'].value_counts())
