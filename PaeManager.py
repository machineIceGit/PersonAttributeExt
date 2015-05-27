#bin/usr/python

import os
import sys
import yaml

### Input text line , decortor to record

class PaeManager:
    
    def __init__(self):
	self._extractors =[]
	pass

    def init(self, yamlFile):
    	
	fp =open(yamlFile)
	confDict = yaml.load(fp)
	if 'attributeExts' in confDict:
	    for classInfo in confDict['attributeExts']:
		className = classInfo['ExactorName']
		moduleName = className + '.' + className
            	module = __import__(moduleName, globals(), locals(), [className])
           	obj = getattr(module, className)()
                if obj.init():
                    print obj.__class__.__name__ + " init SUCCESS"
                self._extractors.append(obj)
        return True
    def run(self, testLine):
        for obj in self._extractors:
            if obj.run(testLine):
                print obj.__class__.__name__ + " run SUCCESS"

if __name__ == '__main__':

    obj = PaeManager()
    obj.init("../conf/paeConf.yaml")
    obj.run({'a':'b'})
