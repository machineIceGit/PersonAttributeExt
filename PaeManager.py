#bin/usr/python
# vim: set fileencoding=utf-8 :

import os
import sys
import yaml
from pipline.Record import Record
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
                paramDict = classInfo['paramDict']
		moduleName = className + '.' + className
            	module = __import__(moduleName, globals(), locals(), [className])
           	obj = getattr(module, className)()
                if obj.init(paramDict):
                    print obj.__class__.__name__ + " init SUCCESS"
                self._extractors.append(obj)
        return True
    def run(self, record={}):
        for obj in self._extractors:
            if obj.run(record):
                print record
                print obj.__class__.__name__ + " run SUCCESS"

if __name__ == '__main__':

    obj = PaeManager()
    obj.init("../conf/paeConf.yaml")
    record =Record({'TEXT':'1998年，邓杰古一家迁往阜阳市区，邓琳凤的哥哥邓枭枭被体操教练郭少华选中练习体操，受哥哥影响，邓琳凤在安徽日本早稻田大学也开始体操训练，同年就读北京体校一年级。'})
    obj.run(record)
