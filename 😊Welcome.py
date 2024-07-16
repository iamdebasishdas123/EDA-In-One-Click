import streamlit as st
import pandas as pd
import mimetypes
import openpyxl

# Setup Streamlit
st.set_page_config(page_title="EDA App", layout="wide")

# App title
st.title("Exploratory Data Analysis (EDA) App")

# Sidebar for file upload
st.subheader("Upload your dataset")

def intro_file_upload(df):
    st.session_state['dataframe'] = df
    st.write("Dataset uploaded successfully!")
    
    # Display first few rows
    st.markdown("## About This App")
    st.markdown("#### First page of dataset about Basic Information")
    st.markdown("#### Second page of dataset about Graph, Relation, Hypothesis test, Normality Test etc")
    
    # Display dataset summary
    st.markdown("### Dataset Summary")
    st.write(df.head())
    st.write(f"Number of rows: {df.shape[0]}")
    st.write(f"Number of columns: {df.shape[1]}")

if 'dataframe' not in st.session_state:
    st.session_state['dataframe'] = None

uploaded_file = st.file_uploader("Drag and drop file here", type=["csv", "xlsx", "txt"])

if uploaded_file is not None:
    mime_type, _ = mimetypes.guess_type(uploaded_file.name)
    #st.write(f"Detected MIME type: {mime_type}")  # Debugging line to show MIME type

    # Display progress bar
    progress_bar = st.progress(0)

    try:
        if mime_type == "text/csv":
            df = pd.read_csv(uploaded_file)
            intro_file_upload(df)
        elif mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(uploaded_file)
            intro_file_upload(df)
        elif mime_type == "text/plain":
            df = pd.read_csv(uploaded_file, sep="\t", encoding='utf-8')
            intro_file_upload(df)
        elif mime_type == "application/vnd.ms-excel":
            df = pd.read_csv(uploaded_file)
            intro_file_upload(df)
        else:
            st.write("Unsupported file format. Please upload a CSV, Excel, or text file.")

        # Update progress bar
        progress_bar.progress(100)
        
    except Exception as e:
        st.write(f"An error occurred: {e}")
        progress_bar.progress(0)

st.markdown("""
    <div class="footer">
    <p>Created by - 📊Debasish Das📉</p>
    </div>
""", unsafe_allow_html=True)