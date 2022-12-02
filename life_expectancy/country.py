"""
Creates an enumerate of the countries.
"""

from enum import Enum


class Country(Enum):
    '''
    An enumerate of all the possible countries.
    '''
    CYPRUS, SWITZERLAND, BULGARIA, BELGIUM, AUSTRIA, HUNGARY = 'CY', 'CH', 'BG', 'BE', 'AT', 'HU'
    ICELAND, FRANCE, NETHERLANDS, SLOVAKIA, GERMANY, IRELAND = 'IS', "FR", 'NL', 'SK', 'DE', 'IE'
    CROATIA, FINLAND, SPAIN, ESTONIA, DENMARK, CZECH_REPUBLIC = 'HR', 'FI', 'ES', 'EE', 'DK', 'CZ'
    ITALY, LIECHTENSTEIN, LITHUANIA, LUXEMBOURG, LATVIA, MALTA = 'IT', 'LI', 'LT', 'LU', 'LV', 'MT'
    NORWAY, POLAND, PORTUGAL, ROMANIA, SWEDEN, SLOVENIA = 'NO', 'PL', 'PT', 'RO', 'SE', 'SI'
    MONTENEGRO, NORTH_MACEDONIA, SERBIA, ARMENIA, AZERBAIJAN = 'ME', 'MK', 'RS', 'AM', 'AZ'
    UKRAINE, MOLDOVA, TURKEY, SAN_MARINO, RUSSIA, BELARUS = 'UA', 'MD', 'TR', 'SM', 'RU', 'BY'
    GEORGIA = 'GE'

    @classmethod
    def get_countries(cls):
        '''
        Returns all the possible countries.
        '''
        return [member.name for member in cls]
