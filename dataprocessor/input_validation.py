# This python script inputs a variety of datatypes to test the main application functionality
# It was developed by Christian Daish on the 26th of March 2024 for Rhombus AI.
# This is version 1.0.260324

import pandas as pd
import numpy as np
from .process_file import process_files

###Generate .CSV or .Xls #####
# Sample data frame with various data types
data = {
    'Numeric_Int': [1, 2, 3, 4, 5],
    'Numeric_Float': [1.1, 2.2, np.nan, 4.4, 5.5],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'String_Boolean': ['True', 'False', 'True', 'False', 'True'],
    'Complex_Number': ['1+2j', '2+3j', '3+4j', '4+5j', '5+6j'],
    'Category': ['A', 'B', 'A', 'B', 'C']
}
df = pd.DataFrame(data)
# sample_path = 'sample_data.csv'
# df.to_csv(sample_path, index=False)
sample_path = 'sample_data_test.xlsx'
df.to_excel(sample_path, index=False)

#Define chunk size for large datasets and threshold for 'categorical' data type
threshold_var = 0.5
chunksize_var = 10000

#Process dependent on filetype
if sample_path.endswith('.xlsx'):
    process_files(sample_path, threshold=threshold_var)  # For Excel
elif sample_path.endswith('.csv'):
    process_files(sample_path, chunksize=chunksize_var, threshold=threshold_var)


