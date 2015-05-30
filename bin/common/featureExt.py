#/usr/bin/python
# vim: set fileencoding=utf-8 :

import os
import sys
import jieba.posseg as pseg
reload(sys)
sys.setdefaultencoding('utf-8')

class featureExt:

    def __init__(self):
        self._feaExtList =[]
        self._suffixFile =""
        self._prefixFile =""
        pass

    def setFeatureList(self, feaList):
        self._feaExtList = feaList

    def setSuffixFile(self, suffixFile):
        self._suffixFile = suffixFile

    def setPrefixFile(self, prefixFile):    
        self._prefixFile = prefixFile

    def init(self, confDict ={}):
        return True

    def onLineExt(self, textLine):
        words = pseg.cut(textLine.strip())
        retArray = []
        for w in words:
            retArray.append(w.word + '\t' + w.flag + '\t' + 'O')
        return ''.join(retArray)

    def run(self, textLine):    
        array = pseg.cut(textLine)
        tag ='O'
        inner = 0
        words =[]

        for w in array:
            words.append(w)
            line =""

        for i in range(0, len(words)):

            if words[i].word == u'【':
                inner =1
                continue
            if words[i].word == u'】':
                tag = 'O'
                inner = 0
                continue
            if inner == 1:
                if i+1 < len(words) and words[i-1].word ==  u'【' and words[i+1].word == u'】':
                    tag = 'S'
                elif words[i-1].word == u'【':
                    tag = 'B'
                elif i+1 < len(words) and words[i+1].word == u'】':
                    tag = 'E'
                else:
                    tag = 'I'
            #index =0
            #uTag = ''
            #print words[i].word + '\t' + tag
            #for uChar in words[i].word:
            #    flag = tag
            #    if index == 0:
            #        if len(words[i].word) == 1:
            #            uTag = 'S'
            #        else:
            #            uTag = 'B'
            #        if tag == 'E':
            #            flag = 'I'
            #        if tag == 'S':
            #            flag = 'B'
            #    elif index == len(words[i].word)-1:
            #        uTag = 'E'
            #        if tag == 'B':
            #            flag = 'I'
            #        if tag == 'S':
            #            flag = 'E'
            #    else:
            #        uTag = 'I'
            #        if tag != 'O':
            #            flag = 'I'
                #print uChar + '\t' + tag + '\t' + flag + '\t' + str(index)
            #    index+=1
            line = line + words[i].word + '\t' + words[i].flag + '\t' + tag  + '\n'
        if inner == 0:
            print line

        return True


if __name__ ==  '__main__':
    pass
