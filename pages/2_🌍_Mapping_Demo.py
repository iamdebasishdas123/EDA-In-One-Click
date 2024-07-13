import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import eda_helper_functions

 # Visualizations
st.header("Visualizations")
st.subheader("Analysis Column and Target column") 

def EDA(data,col, target):
        if data[col].dtype == "object" and len(data[col].unique()) < 20:
            st.plotly_chart(st.plotly_chart(eda_helper_functions.cat_summary(data, col)))
            st.plotly_chart(eda_helper_functions.cat_univar_plots(data, col))
            st.plotly_chart(eda_helper_functions.cat_bivar_plots(data, col, target))
            st.plotly_chart(eda_helper_functions.num_cat_bivar_plots(data, target, col))
            st.plotly_chart(eda_helper_functions.num_cat_hyp_testing(data, target, col))
        elif data[col].dtype == "object" and len(data[col].unique()) > 20:
            # Skip processing for large categorical columns
            st.plotly_chart(eda_helper_functions.cat_summary(data, col))
            st.write("This Column have %d unique values. So, I do not Analysis further", len(data[col].unique()))
        elif col == target:
            st.write("Both Column are same. So, I do Only Univariate Analysis")
            if data[col].dtype == "object" and len(data[col].unique()) < 20:
                    st.plotly_chart(eda_helper_functions.cat_summary(data, col))
                    st.plotly_chart(eda_helper_functions.cat_univar_plots(data, col))
            elif data[col].dtype == "object" and len(data[col].unique()) > 20:
                    st.plotly_chart(eda_helper_functions.cat_summary(data, col))
                    st.write("This Column have %d unique values. So, I do not Analysis further", len(data[col].unique()))
            else:
                st.plotly_chart(eda_helper_functions.num_summary(data, col))
                st.plotly_chart(eda_helper_functions.num_univar_plots(data, col))
            
        else:
            st.plotly_chart(eda_helper_functions.num_summary(data, col))
            st.plotly_chart(eda_helper_functions.num_univar_plots(data, col))
            st.plotly_chart(eda_helper_functions.num_bivar_plots(data, col, target))
            st.plotly_chart(eda_helper_functions.num_num_hyp_testing(data, col, target))
  

# Check if the dataframe is in session state
if 'dataframe' in st.session_state:
    df = st.session_state['dataframe']
    st.write("Here is the dataset from the main page:")
    st.write(df.head(5))

    
    st.header("Select Columns for EDA")
    
    column_names = df.columns.tolist()

    eda_column = st.sidebar.selectbox("Select a column for EDA", column_names)
    target_column = st.sidebar.selectbox("Select a target column for bivariate plots (optional)", [None] + column_names)
    plot_type = st.sidebar.selectbox("Select plot type (optional)", [None, "Distribution", "Box Plot", "Count Plot", "Pair Plot", "Correlation Heatmap"])
    
    if st.sidebar.button("Generate Plots"):
        if target_column:
            EDA(df,eda_column, target_column)
        else:
            EDA(df, eda_column)

        
else:
    st.write("Please upload a CSV file to start the EDA.")
    
                
