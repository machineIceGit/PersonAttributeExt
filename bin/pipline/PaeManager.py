#bin/usr/python

import os
import sys


### Input text line , decortor to record

class PaeManager:
    
    def __init__(self):
        pass

    def init(self):
        print "init success"

    def run(self, testLine):
        print "PaeManager is running"

if __name__ == '__main__':

    obj = PaeManager()
    obj.init()
    obj.run()
    for line in sys.stdin:
        PaeManager.run(line)
