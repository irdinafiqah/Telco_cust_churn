import streamlit as st
import numpy as np
import pandas as pd
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
st.write(
