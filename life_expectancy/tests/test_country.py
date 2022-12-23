from life_expectancy.country import Country


def test_country():
    """Test the `Country` class by comparing the len of the list"""
    countries_list = Country.get_countries()
    assert len(countries_list) == 32
