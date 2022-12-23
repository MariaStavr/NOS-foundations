"""
Runs the main script
"""
import argparse
from life_expectancy.data_processing import DataProcessor, SelectorDataProcessor
from life_expectancy.cleaning import save_data, IMPORT_FILE_NAME
from life_expectancy.country import Country


def parse_args():
    '''
    Adding command line option for region.
    '''
    parser_aux = argparse.ArgumentParser()
    parser_aux.add_argument('--region', type=str,
                            default=Country.PT.name)
    args = parser_aux.parse_args()
    return args.region

#


def main(region_name) -> None:
    '''
    Loads, cleans and saves the data.
    '''
    processor = DataProcessor()
    _df = SelectorDataProcessor(processor)
    cleaned_df = _df.get_processor(IMPORT_FILE_NAME, region_name)
    save_data(cleaned_df)


if __name__ == "__main__":  # pragma: no cover
    region = parse_args()
    main(region)
