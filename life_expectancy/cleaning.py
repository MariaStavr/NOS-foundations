"""
Provides data cleansing
"""
import argparse
from pathlib import Path

import pandas as pd

DIR_PATH = Path(__file__).parent
IMPORT_FILE_NAME = "eu_life_expectancy_raw.tsv"
SAVE_FILE_NAME = "pt_life_expectancy.csv"


def clean_data(region_name: str):  # pylint: disable=C0116

    _df = pd.read_csv(DIR_PATH / "data" / IMPORT_FILE_NAME, delimiter="\t")
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
    data.to_csv(DIR_PATH / "data" / SAVE_FILE_NAME, index=False)


def parse_args():  # pylint: disable=C0116
    parser_aux = argparse.ArgumentParser()
    parser_aux.add_argument('--region', type=str, default="PT")
    args = parser_aux.parse_args()
    return args.region


if __name__ == "__main__":  # pragma: no cover
    region = parse_args()
    clean_data(region)
