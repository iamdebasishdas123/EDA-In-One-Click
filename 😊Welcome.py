import streamlit as st
import pandas as pd

# Setup Streamlit
st.set_page_config(page_title="EDA App", layout="wide")

# App title
st.title("Exploratory Data Analysis (EDA) App")

# Sidebar for file upload
st.subheader("Upload your dataset")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['dataframe'] = df
    st.write("Dataset uploaded successfully!")
    
    # Display first few rows
    st.markdown("## About This App" )
    st.markdown("### First page of dataset about Basic Information")
    st.markdown("### Second page of dataset about Graph,Relation ,Hypothesis test, Normality Test etc")
    st.markdown("""
        <div class="footer">
        <p>Created by - 📊Debasish Das📉</p>
        """,unsafe_allow_html=True)
    
   
    
