import os
import pandas as pd


def get_data(league = 'LIGA'):
    directory_in_str = f'raw_data/{league}'
    directory = os.fsencode(directory_in_str)
    list_df = [ pd.read_csv(directory_in_str+'/'+os.fsdecode(file)) for file in os.listdir(directory) if os.fsdecode(file).endswith('.csv')]
    return list_df
