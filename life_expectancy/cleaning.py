"""
Provides data cleansing
"""
import argparse
import csv
from pathlib import Path

import pandas as pd

DIR_PATH = Path(__file__).parent
IMPORT_FILE_NAME = "eu_life_expectancy_raw.tsv"
SAVE_FILE_NAME = "pt_life_expectancy.csv"


def load_data() -> pd.DataFrame:  # pylint: disable=C0116
    _df = pd.read_csv(DIR_PATH / "data" / IMPORT_FILE_NAME, delimiter="\t")
    return _df


def clean_data(_df: pd.DataFrame, region_name: str) -> pd.DataFrame:  # pylint: disable=C0116
    _df[['unit', 'sex', 'age', 'region']
        ] = _df.iloc[:, 0].str.split(',', expand=True)
    _df = _df.drop(_df.columns[0], axis=1)
    data = pd.melt(_df, id_vars=_df.iloc[:, -4:],
                   value_vars=_df.iloc[:, :-4], var_name='year')
    data['year'] = data['year'].astype(int)
    data['value'] = data['value'].astype(str)
    data['value'] = data['value'].str.replace(':', '')
    data['value'] = data['value'].str.replace('[a-zA-Z]', '', regex=True)
    data = data[data['value'] != ' ']
    data = data[data['region'] == region_name]
    data['value'] = data['value'].astype(float)
    return data


def save_data(data) -> csv:  # pylint: disable=C0116
    data.to_csv(DIR_PATH / "data" / SAVE_FILE_NAME, index=False)


def parse_args():  # pylint: disable=C0116
    '''
    Adding command line option for region.
    '''
    parser_aux = argparse.ArgumentParser()
    parser_aux.add_argument('--region', type=str, default="PT")
    args = parser_aux.parse_args()
    return args.region


def main(region_name):
    '''
    Loads, cleans and saves the data.
    '''
    _df = load_data()
    cleaned_df = clean_data(_df, region_name)
    save_data(cleaned_df)


if __name__ == "__main__":  # pragma: no cover
    region = parse_args()
    main(region)
