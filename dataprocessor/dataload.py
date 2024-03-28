#This python script inputs data from .csv or .xlsx files, converts them to DataFrames then returns them to process_file for processing.
# It was developed by Christian Daish on the 26th of March 2024 for Rhombus AI.
# This is version 1.0.260324

#import packages and functions
import pandas as pd

# import the dataset
def load_data(file_path,file_type,chunksize=None):
    """
        Load data from a CSV or Excel file into a Pandas DataFrame.

        Parameters:
            file_path (str): The path to the CSV or Excel file.
            file_type (str): Type of the file ('csv' or 'xlsx').
            chunksize (int): Number of rows per chunk for chunked reading.

        Returns:
            A tuple of (DataFrame or TextFileReader, str indicating data type).
        """
    # Determine the file type and load data accordingly
    # use chunks for large datasets
    # file_path.seek(0)

    if file_type == 'csv':
        if chunksize:
            return pd.read_csv(file_path,chunksize=chunksize),'csv_chunked'
        else:
            return pd.read_csv(file_path),'csv_full'
    elif file_type == 'xlsx':
        if chunksize:
            return pd.read_excel(file_path, engine='openpyxl'), 'xlsx_chunked'
        else:
            return pd.read_excel(file_path,engine='openpyxl'), 'xlsx_full'
    else:
        # Raise an error if the file format is unsupported
        raise ValueError("Unsupported file format. Please provide a CSV or Excel (.xlsx) file.")

