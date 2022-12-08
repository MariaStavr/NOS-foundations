"""
Creates an enumerate of the countries.
"""

from enum import Enum, auto


class Country(Enum):
    '''
    An enumerate of all the possible countries.
    '''

    DE = auto()
    IE = auto()
    HR = auto()
    FI = auto()
    ES = auto()
    EE = auto()
    DK = auto()
    CZ = auto()
    IT = auto()
    LI = auto()
    LT = auto()
    LU = auto()
    LV = auto()
    MT = auto()
    NO = auto()
    PL = auto()
    PT = auto()
    RO = auto()
    SE = auto()
    SI = auto()
    ME = auto()
    MK = auto()
    RS = auto()
    AM = auto()
    AZ = auto()
    UA = auto()
    MD = auto()
    TR = auto()
    SM = auto()
    RU = auto()
    BY = auto()
    GE = auto()

    @classmethod
    def get_countries(cls):
        '''
        Returns all the possible countries.
        '''
        return [member.name for member in cls]


print(Country.PT.name)
