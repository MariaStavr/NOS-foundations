"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR, OUTPUT_DIR


@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    yield  # this is where the testing happens

    # Teardown : fill with any logic you want
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")


@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Fixture to load the EU life expectancy sample data"""
    return pd.read_csv(
        OUTPUT_DIR / "eu_life_expectancy_raw_sample.tsv", delimiter="\t"
    )


@pytest.fixture(scope="session")
def eurostat_life_expect_json() -> pd.DataFrame:
    """Fixture to load the EU life expectancy sample data for json file"""
    return pd.read_json(
        OUTPUT_DIR / "eurostat_life_expect_sample.json", typ='frame'
    )


@pytest.fixture(scope="session")
def eurostat_life_expect_expected_json() -> pd.DataFrame:
    """Fixture to load the EU life expectancy expected sample data for json file"""
    return pd.read_csv(
        FIXTURES_DIR / "eurostat_life_expect_expected_sample.csv"
    )


@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the EU life expectancy expected sample data"""
    return pd.read_csv(
        FIXTURES_DIR / "pt_life_expectancy_expected_sample.csv"
    )
