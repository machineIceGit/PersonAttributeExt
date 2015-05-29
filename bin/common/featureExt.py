#/usr/bin/python

import os
import sys
import jieba.posseg as pseg

class featureExt:

    def __init__(self):
        pass


    def init(self, confDict ={}):
        return True

    def run(self, textLine):
        words = pseg.cut(textLine)
        for w in words:
            print w.word, w.flag
        return True


if __name__ ==  '__main__':
    pass
