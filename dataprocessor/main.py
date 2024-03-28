# This python script inputs data from .csv or .xlsx files, infers and converts the data, and displays the output via a web application.
# It was developed by Christian Daish on the 26th of March 2024 for Rhombus AI.
# This is version 1.0.260324

# import packages and functions
from .process_file import process_files
from django.conf import settings
import os

#Function to perform pre-processing and pass the data to the processing modules
def read_project_file(file_path, file_type,threshold_var='0.5'):
    # Define chunk size for large datasets and threshold for 'categorical' data type
    threshold_var = float(threshold_var) if threshold_var else 0.5
    chunksize_var = 10000 if file_type == 'csv' else None  # Chunk size is applicable for CSV files

    # Process the file based on its type and path
    file_name, result = process_files(file_path, file_type, chunksize_var, threshold_var)
    return file_name, result
