import json

class Record:

    TEXT =None
    SCHOOL =None
    TITLE =None

    def __init__(self, tDict={}):
        self.__dict__.update(tDict)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            return False

    def __str__(self):  
        return json.dumps(self.__dict__, ensure_ascii = False)
