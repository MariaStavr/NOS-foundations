"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_data
#, parse_args
from . import OUTPUT_DIR

def test_clean_data(pt_life_expectancy_expected): # pylint: disable=C0116
    """Run the `clean_data` function and compare the output to the expected output"""
    path='C:\\Users\\stavr\\OneDrive\\Desktop\\NOS Foundations\\assignments\\life_expectancy'
    imported_file='eu_life_expectancy_raw.tsv'
    saved_file='saved'
    clean_data(path,imported_file, saved_file )
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )

# def test_parser(self): # pylint: disable=C0116
#     parser = parse_args(['--country', 'PT'])
#     self.assertTrue(parser.long)
