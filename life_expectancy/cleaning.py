"""
Provides data cleansing
"""
from pathlib import Path
import pandas as pd

DIR_PATH = Path(__file__).parent
IMPORT_FILE_NAME = "eu_life_expectancy_raw.tsv"
SAVE_FILE_NAME = "pt_life_expectancy.csv"


def load_data_tsv() -> pd.DataFrame:
    '''
    Loads the data from csv.
    '''
    _df = pd.read_csv(DIR_PATH / "data" / IMPORT_FILE_NAME, delimiter="\t")

    return _df


def load_data_json() -> pd.DataFrame:
    '''
    Loads the data from json.
    '''
    _df = pd.read_json(DIR_PATH / "data" / IMPORT_FILE_NAME, typ='frame')

    return _df


def clean_data_tsv(_df: pd.DataFrame, region_name: str) -> pd.DataFrame:
    '''
    Manipulates the data for tsv file.
    '''
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


def clean_data_json(_df: pd.DataFrame, region_name: str) -> pd.DataFrame:
    '''
    Manipulates the data for json file.
    '''
    _df = _df.rename(columns={'country': 'region',
                              'life_expectancy': 'value'})
    _df = _df[_df['region'] == region_name]
    _df = _df.drop(columns=["flag", "flag_detail"])
    _df['year'] = _df['year'].astype(int)
    _df['value'] = _df['value'].astype(float)
    return _df


def save_data(data: pd.DataFrame) -> None:
    '''
    Saves the data to a new file.
    '''
    data.to_csv(DIR_PATH / "data" / SAVE_FILE_NAME, index=False)
