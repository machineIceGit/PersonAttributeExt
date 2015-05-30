from json import *

class Record:

    NAME = '_name'
    SCHOOL = '_school_attend'
    TITLE = '_title'
    BIRTH_DATE = '_birth_date'
    BIRTH_PLACE = '_birth_place'

    def __init__(self):
        self._dict ={}

    def __getattr__(self):
        pass

    def get(self, key):
        return self._dict[key]

    def set(self, key, value):
        self._dict[key] = value
    
    def __str__(self):
        print JSONEncoder().encode(self._dict)
