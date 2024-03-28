#This python script processes data that has been input via the process_file python script.
# It was developed by Christian Daish on the 26th of March 2024 for Rhombus AI.
# This is version 1.0.260324

#import packages and functions
import pandas as pd
import re

# infer and convert data types
def infer_and_convert_dtypes(df, threshold):
    """
     Infer and convert data types of a DataFrame to the most appropriate types.

     Parameters:
         df (DataFrame): The Pandas DataFrame whose data types are to be inferred and converted.

     Returns:
         DataFrame: A DataFrame with columns converted to inferred data types.
     """

    # List of potential date formats to try
    date_formats = ['%d-%m-%Y', '%d/%m/%Y', '%Y-%m-%d', '%d.%m.%Y', '%d-%b-%Y', '%b-%d-%Y']

    #Cycle through columns
    for col in df.columns:
        original_dtype = df[col].dtype # Store original dtype for comparison

        # Attempt to convert object columns potentially containing numeric or datetime data
        if original_dtype == 'object':
            # Numeric conversion attempt
            temp_col = pd.to_numeric(df[col], errors='coerce', downcast='integer')
            if not temp_col.isnull().all():
                df[col] = temp_col
            else:
                # Float conversion attempt
                temp_col = pd.to_numeric(df[col], errors='coerce', downcast='float')
                if not temp_col.isnull().all():
                    df[col] = temp_col
                else:
                    # Datetime conversion attempt
                    for date_format in date_formats:
                        temp_col = pd.to_datetime(df[col], format=date_format, errors='coerce')
                        if temp_col.notna().any():
                            df[col] = temp_col
                            break
                    else:
                        # Categorical conversion based on threshold
                        if df[col].nunique() / len(df) < threshold:
                            df[col] = df[col].astype('category')
                        else:
                            # Convert remaining object columns to explicit pandas string type
                            df[col] = df[col].astype('object')

        unique_vals = df[col].dropna().unique()
        # Boolean Conversion: Check for presence of boolean-like strings
        if set(unique_vals).issubset({'True', 'False', 'Yes', 'No', '1', '0'}):
            # Map to proper booleans
            df[col] = df[col].map(
                {'True': True, 'False': False, 'Yes': True, 'No': False, '1': True, '0': False}).astype('boolean')

        # Complex Conversion: Look for pattern indicative of complex numbers
        elif any(re.match(r'^[+\-]?\d+(\.\d+)?[+\-]\d+(\.\d+)?j$', str(val)) for val in unique_vals):
            df[col] = df[col].apply(lambda x: complex(x) if pd.notna(x) else x)

        # Timedelta Conversion: This could be complex depending on the format of the timedelta strings
        # As an example, assuming numeric values represent days:
        elif all(re.match(r'^\d+$', str(val)) for val in unique_vals) and ("duration" in col.lower() or "days" in col.lower()):
            df[col] = pd.to_timedelta(df[col].astype(float), unit='D', errors='coerce')

    return df


