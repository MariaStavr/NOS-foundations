from life_expectancy.country import Country


def test_country():
    """Test the `Country` class by comparing the len and the first element of the list"""
    countries_list = Country.get_countries()
    assert len(countries_list) == 42
    assert countries_list[0] == 'CYPRUS'
    assert countries_list[-1] == 'GEORGIA'
