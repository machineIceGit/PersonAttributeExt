#usr/bin/python
from common.CrfExtractor import CrfExtractor

class TitleExtractor:
    
    def __init__(self):
        self._crfExtObj = CrfExtractor()

    def init(self, confDict={}):
        if 'modelFile' in confDict:
            self._crfExtObj.init(confDict['modelFile'])
        return True

    def run(self, record={}):
        if not record.TITLE:
            record.TITLE =[]
        textLine = record.TEXT
        record.TITLE = self._crfExtObj.run(textLine)
        return True
    
if __name__ == '__main__':
    pass

