"""
Creates the adapter
"""
import pandas as pd
from life_expectancy.cleaning import load_data_json, load_data_tsv, clean_data_json, clean_data_tsv


class AdapterFileType:  # pylint: disable=too-few-public-methods
    """Adapter used to distinguish the treatment for json and tsv files"""

    def __init__(self, file, region) -> None:
        self.file = file
        self.region = region

    def load_and_clean(self) -> pd.DataFrame:
        """Loads and cleans the file based on its extension"""
        extension = self.file.split(".")[1]
        if extension == "json":
            _df = load_data_json()
            return clean_data_json(_df, self.region)
        if extension == "tsv":
            _df = load_data_tsv()
            return clean_data_tsv(_df, self.region)
        return pd.DataFrame()
