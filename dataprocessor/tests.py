# add to tests.py
from .dataload import load_data
from .infer_and_convert_data import infer_and_convert_dtypes
import pandas as pd
from django.test import TestCase, Client

class DataProcessingTestCase(TestCase):
    def test_data_loading_csv(self):
        df, dtype = load_data('test-data/sample_data.csv', 'csv')
        self.assertIsInstance(df, pd.DataFrame)
        df, dtype = load_data('test-data/sample_data.xlsx', 'xlsx')
        self.assertIsInstance(df, pd.DataFrame)

    def test_data_type_inference(self):
        df = pd.DataFrame({
            'numeric': ['1', '2', '3'],
            'dates': ['2020-01-01', '2020-01-02', '2020-01-03'],
            'bool': ['True', 'False', 'True']
        })
        converted_df = infer_and_convert_dtypes(df, threshold=0.5)
        # Assert each column's dtype
        self.assertTrue(pd.api.types.is_numeric_dtype(converted_df['numeric']))
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(converted_df['dates']))
        self.assertTrue(pd.api.types.is_bool_dtype(converted_df['bool']))
