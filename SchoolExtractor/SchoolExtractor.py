#/usr/bin/python
import CRFPP
from common.featureExt import featureExt
from pipline.Record import Record

class SchoolExtractor:

    def __init__(self):
        self._feaObj = featureExt()
        pass


    def init(self,confDict={}):
        self._feaObj.init()
        if 'modelFile' in confDict:
            self._modelFile = confDict['modelFile']
        return True

    def run(self, record={}):
        textLine = record.TEXT
        retList =self._feaObj.onLineExt(textLine).split('')
        tagger = CRFPP.Tagger("-m " + self._modelFile)
        tagger.clear()
        for line in retList:
            #print line
            tagger.add(line.strip().encode('utf-8'))
        tagger.parse()
        size = tagger.size()
        xsize = tagger.xsize()
        wordList =[]
        school_candi = ''
        if not record.SCHOOL:
            record.SCHOOL =[]
        for i in range(0, size):
            char = tagger.x(i, 0).decode('utf-8')
            tag = tagger.y2(i)
            #print char + '\t' + tag
            if tag == 'B':
                school_candi += char
                char = '[' + char
            if tag == 'I':
                school_candi += char
            if tag == 'S':
                school_candi += char
                record.SCHOOL.append(school_candi)
                school_candi = ''
                char = '[' + char + ']'
            if tag == 'E':
                school_candi += char
                record.SCHOOL.append(school_candi)
                school_candi = ''
                char = char + ']'
            wordList.append(char)
        print ''.join(wordList)
        return True

if __name__ == '__main__':
    obj = SchoolExtractor()
    confDict ={'modelFile':'../data/models/model_school'}
    obj.init(confDict)
    for line in open('test'):
        obj.run(line)
    pass
