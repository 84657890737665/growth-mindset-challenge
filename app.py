# Imports 

import streamlit as st 
import pandas as pd 
import os 
from io import BytesIO



# Set up Our Application 

    # Title
st.title('📀Neatiformix - Makes Data Neat and Transform✨!')

    # Sidebar with options
option = st.sidebar.selectbox('Choose an option', ['Load Data', 'Clean Data', 'Transform Data'])

    # Load Data
if option == 'Load Data':
        file = st.file_uploader('Upload your CSV file', type=['csv'])
        if file is not None:
            df = pd.read_csv(file)
            st.dataframe(df)
            st.write('Data loaded successfully!')

            # Clean Data
            if st.checkbox('Clean Data'):
                df = df.dropna()
                df = df.drop_duplicates()
                st.dataframe(df)
                st.write('Data cleaned successfully!')
                if st.checkbox('Save Cleaned Data'):
                     file_name = 'cleaned_data.csv'
                     df.to_csv(file_name, index=False)
                     st.download_button(f'Download Cleaned Data ({file_name})', BytesIO(df.to_csv().encode()), file_name)
                     st.success('Cleaned data saved successfully!')

                     # Transform Data
                     if st.checkbox('Transform Data'):
                         selected_columns = st.multiselect('Select columns to transform', df.columns)
                         for column in selected_columns:
                             if st.checkbox(f'Log transform {column}'):
                                 import numpy as np  # Imported here as it was throwing error without this line of code.
                         st.dataframe(df)
                         st.write('Data transformed successfully!')
                         if st.checkbox('Save Transformed Data'):
                             file_name = 'transformed_data.csv'
                             df.to_csv(file_name, index=False)
                             st.download_button(f'Download Transformed Data ({file_name})', BytesIO(df.to_csv().encode()), file_name)
                             st.success('Transformed data saved successfully!')
         
                    