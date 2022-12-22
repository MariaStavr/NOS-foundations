"""
Chooses the correct file treatment based on file extension
"""
from typing import Callable
import pandas as pd
from life_expectancy.cleaning import load_data_json, load_data_tsv, clean_data_json, clean_data_tsv


class DataProcessor():
    """Manipulator class for each file type"""
    data_processor: Callable[[str], pd.DataFrame]

    def json_processor(self, region: str) -> pd.DataFrame:
        """json processor method"""
        _df = load_data_json()
        return clean_data_json(_df, region)

    def tsv_processor(self, region: str) -> pd.DataFrame:
        """tsv processor method"""
        _df = load_data_tsv()
        return clean_data_tsv(_df, region)


class SelectorDataProcessor():  # pylint: disable=too-few-public-methods
    """Selector data processor class for each file type"""

    def __init__(self, data_processor: DataProcessor):
        self.data_processor = data_processor

    def get_processor(self, file, region):
        """Distinguish the treatment depending on the file extension"""
        extension = str(file.split(".")[1])

        strategy_map = {
            "json": self.data_processor.json_processor,
            "tsv": self.data_processor.tsv_processor,
        }

        return strategy_map[extension](region)
