"""
Chooses the correct file treatment based on file extension
"""
from abc import ABC, abstractmethod
import pandas as pd
from life_expectancy.cleaning import load_data_json, load_data_tsv, clean_data_json, clean_data_tsv


class AbstractFileType(ABC):
    """Abstract class for each file type"""
    @abstractmethod
    def json_file(self, region):
        """Abstract method for json file"""

    @abstractmethod
    def tsv_file(self, region):
        """Abstract method for tsv file"""


class FileManipulator(AbstractFileType):
    """Manipulator class for each file type"""

    def json_file(self, region):
        _df = load_data_json()
        return clean_data_json(_df, region)

    def tsv_file(self, region):
        _df = load_data_tsv()
        return clean_data_tsv(_df, region)


class SelectorFileManipulator():  # pylint: disable=too-few-public-methods
    """Selector file manipulator depending on the file extension"""

    def __init__(self, file_manipulator: AbstractFileType):
        self.file_manipulator = file_manipulator

    def select_treatment(self, file, region):
        """Distinguish the treatment depending on the file extension"""
        extension = file.split(".")[1]
        if extension == "json":
            return self.file_manipulator.json_file(region)
        if extension == "tsv":
            return self.file_manipulator.tsv_file(region)
        return pd.DataFrame()
