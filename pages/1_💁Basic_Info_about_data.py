import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

st.header("Basic Information About Dataset")

# Check if the dataframe is in session state
if 'dataframe' in st.session_state:
    df = st.session_state['dataframe']
    st.write("Here is the dataset from the main page:")
    st.dataframe(df.head(5))
    
    # Basic Information about dataset
    rows, cols = df.shape
    st.write(f"Number of rows: {rows}")
    st.write(f"Number of columns: {cols}")
    
    st.write("Data Types:")
    # Redirect df.info() output to a buffer
    buffer = io.StringIO()
    df.info(buf=buffer)
    info = buffer.getvalue()

    # Display the info in Streamlit
    st.text(info)
    
    
    st.write("Missing Values:")
    st.write(df.isnull().sum())
    
    st.write(f"Duplicate Row Values: {df.duplicated().sum()}")
    datatypes = df.dtypes.value_counts().reset_index()
    datatypes.columns = ['Data Type', 'Count']

    st.write("Datatypes Counts:")
    st.dataframe(datatypes)
    # Summary Statistics
    st.header("Summary Statistics")
    st.write(df.describe(include="O"))
    st.write(df.describe())
else:
    st.write("No dataset found. Please upload a dataset on the main page.")

    





