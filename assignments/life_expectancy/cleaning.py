"""
Provides data cleansing
"""
import argparse
import sys
import os
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))
import_file_name='eu_life_expectancy_raw.tsv'
saved_file_name = 'pt_life_expectancy.csv'

def clean_data(path, file_name, saved_file_name): # pylint: disable=C0116
    
    _df = pd.read_csv(f'{path}\data\{file_name}', sep='\t', engine='python')     
    _df[['unit','sex','age','region']] = _df.iloc[:, 0].str.split(',', expand=True)
    _df = _df.drop(_df.columns[0], axis=1)
    data = pd.melt(_df, id_vars=_df.iloc[:,-4:], value_vars=_df.iloc[:,:-4], var_name='year')
    data['year'] = data['year'].astype(int)
    data['value'] = data['value'].astype(str)
    data['value'] = data['value'].str.replace(':', '')
    data['value'] = data['value'].str.replace('[a-zA-Z]', '', regex=True)
    data = data[data['value']!=' ']
    data = data[data['region']=="PT"]
    data['value'] = data['value'].astype(float)
    data.to_csv(f'{path}\data\{saved_file_name}', index=False)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=str, default="PT")
    return parser.parse_args(args)

if __name__ == "__main__": # pragma: no cover
    parser = parse_args(sys.argv[1:])
    clean_data(dir_path, import_file_name, saved_file_name)
