"""Tests for the cleaning module"""
import unittest.mock
from unittest.mock import patch, Mock
import pandas as pd
import pytest
from pytest import MonkeyPatch
from life_expectancy.cleaning import main, load_data, clean_data, save_data
from . import OUTPUT_DIR, FIXTURES_DIR


def test_end_to_end(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    main("PT")
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )


@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Fixture to load the EU life expectancy sample data"""
    return pd.read_csv(
        OUTPUT_DIR / "eu_life_expectancy_raw_sample.tsv", delimiter="\t"
    )


@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the EU life expectancy expected data"""
    return pd.read_csv(
        FIXTURES_DIR / "pt_life_expectancy_expected_sample.csv"
    )


def test_load_data(monkeypatch: MonkeyPatch, eu_life_expectancy_raw: pd.DataFrame) -> None:
    """Test the `load_data` function by comparing the output to the expected output"""
    # Mock input data
    def _read_mock_data(*args, **kwargs) -> pd.DataFrame:  # pylint(unused-argument)
        return eu_life_expectancy_raw
    monkeypatch.setattr(
        "life_expectancy.cleaning.pd.read_csv", _read_mock_data)
    results = load_data()
    pd.testing.assert_frame_equal(results, eu_life_expectancy_raw)


def test_clean_data(eu_life_expectancy_raw: pd.DataFrame,
                    eu_life_expectancy_expected: pd.DataFrame) -> None:
    """Test the `clean_data` function by comparing the output to the expected output"""
    results = clean_data(eu_life_expectancy_raw, "PT")
    pd.testing.assert_frame_equal(
        results.reset_index(
            drop=True), eu_life_expectancy_expected.reset_index(drop=True),
        check_dtype=False)


def test_save_data(monkeypatch: MonkeyPatch,
                   eu_life_expectancy_raw: pd.DataFrame) -> None:
    """Test the `save_data` function by asserting that it is being called"""
    test_df = pd.DataFrame()
    with unittest.mock.patch.object(test_df, "to_csv",
                                    return_value=print('Successfully saved')) as to_csv_mock:
        save_data(eu_life_expectancy_raw)
        to_csv_mock.assert_called


@patch('life_expectancy.cleaning.parse_args_pt')
def test_parse_args_pt(MockMethod: Mock) -> None:
    """Patch the test of the `parse_args_pt` method"""
    main("PT")
    assert MockMethod.assert_called
