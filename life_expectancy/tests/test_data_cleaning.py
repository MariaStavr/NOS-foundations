"""Tests for the cleaning module"""
import unittest.mock
from unittest.mock import patch, Mock
import pandas as pd
from pytest import MonkeyPatch
from life_expectancy.cleaning import load_data_tsv, load_data_json, clean_data_tsv, clean_data_json, save_data
from life_expectancy.main_script import main
from life_expectancy.country import Country
from . import OUTPUT_DIR, FIXTURES_DIR


def test_end_to_end(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    main(Country.PT.name)
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )


def test_load_data_tsv(monkeypatch: MonkeyPatch, eu_life_expectancy_raw: pd.DataFrame) -> None:
    """Test the `load_data_tsv` function by comparing the output to the expected output"""
    # Mock input data
    def _read_mock_data(*args, **kwargs) -> pd.DataFrame:  # pylint(unused-argument)
        return eu_life_expectancy_raw
    monkeypatch.setattr(
        "life_expectancy.cleaning.pd.read_csv", _read_mock_data)
    results = load_data_tsv()
    pd.testing.assert_frame_equal(results, eu_life_expectancy_raw)


def test_load_data_json(monkeypatch: MonkeyPatch, eurostat_life_expect_json: pd.DataFrame) -> None:
    """Test the `load_data_json` function by comparing the output to the expected output"""
    # Mock input data
    def _read_mock_data(*args, **kwargs) -> pd.DataFrame:  # pylint(unused-argument)
        return eurostat_life_expect_json
    monkeypatch.setattr(
        "life_expectancy.cleaning.pd.read_json", _read_mock_data)
    results = load_data_json()
    pd.testing.assert_frame_equal(results, eurostat_life_expect_json)


def test_clean_data_tsv(eu_life_expectancy_raw: pd.DataFrame,
                        eu_life_expectancy_expected: pd.DataFrame) -> None:
    """Test the `clean_data_tsv` function by comparing the output to the expected output"""
    results = clean_data_tsv(eu_life_expectancy_raw, Country.PT.name)
    pd.testing.assert_frame_equal(
        results.reset_index(
            drop=True), eu_life_expectancy_expected.reset_index(drop=True),
        check_dtype=False)


def test_clean_data_json(eurostat_life_expect_json: pd.DataFrame,
                         eurostat_life_expect_expected_json: pd.DataFrame) -> None:
    """Test the `clean_data_json` function by comparing the output to the expected output"""
    results = clean_data_json(
        eurostat_life_expect_json, Country.PT.name)
    pd.testing.assert_frame_equal(
        results.reset_index(
            drop=True), eurostat_life_expect_expected_json.reset_index(drop=True),
        check_dtype=False, check_names=False)


def test_save_data(eu_life_expectancy_raw: pd.DataFrame) -> None:
    """Test the `save_data` function by asserting that it is being called"""
    test_df = pd.DataFrame()
    with unittest.mock.patch.object(test_df, "to_csv",
                                    return_value=print('Successfully saved')) as to_csv_mock:
        save_data(eu_life_expectancy_raw)
        to_csv_mock.assert_called


@patch('life_expectancy.main_script.parse_args')
def test_parse_args_pt(MockMethod: Mock) -> None:
    """Patch the test of the `parse_args_pt` method"""
    main(Country.PT.name)
    assert MockMethod.assert_called
