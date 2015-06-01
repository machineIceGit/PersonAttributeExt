#bin/usr/python
# vim: set fileencoding=utf-8 :

import os
import sys
import yaml
from pipline.Record import Record
import argparse

class PaeManager:
    
    def __init__(self):
	self._extractors =[]
        self._filters = []
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
        if 'filterAttrs' in confDict:
	    for classInfo in confDict['filterAttrs']:
		className = classInfo['FilterName']
                paramDict = classInfo['paramDict']
		moduleName = className + '.' + className
            	module = __import__(moduleName, globals(), locals(), [className])
           	obj = getattr(module, className)()
                if obj.init(paramDict):
                    print obj.__class__.__name__ + " init SUCCESS"
                self._filters.append(obj)
        fp.close()
        return True

    def run(self, record={}):
        
        # Extractors

        print "Load this Module Sucess"

        for obj in self._extractors:
            if obj.run(record):
                print obj.__class__.__name__ + " run SUCCESS"
        print record
        
        # Filters

        for obj in self._filters:
            if obj.run(record):
                print obj.__class__.__name__ + " run SUCCESS"
        print record
        return record


if __name__ == '__main__':

    argParse = argparse.ArgumentParser(usage='PaeManager', description='user input args')
    argParse.add_argument('-i' ,'--inputFile', help ='input  file')
    argParse.add_argument('-c','--confYaml', default='../conf/paeConf.yaml', help ='model conf yaml file')
    argParse.add_argument('-t' ,'--targetName', help =' main person')

    args = argParse.parse_args()
    confYamlFile =args.confYaml 
    obj = PaeManager()
    obj.init(confYamlFile)

    iptFile = args.inputFile
    targetName = args.targetName
    
    fp = open('_tmp', 'w')

    for line in open(iptFile):
        line = line.strip().decode('utf-8')
        record = Record({'TEXT': line, 'TARGET_NAME': targetName})
        #record =Record({'TEXT':'邓琳凤在安徽日本早稻田大学也开始体操训练', 'TARGET_NAME':'邓枭枭'})
        #record =Record({'TEXT':'1998年，邓杰古一家迁往阜阳市区，邓琳凤的哥哥邓枭枭被体操教练郭少华选中练习体操，受哥哥影响，邓琳凤在安徽日本早稻田大学也开始体操训练，同年就读北京体校一年级。', 'TARGET_NAME':'邓枭枭'})
        #record =Record({'TEXT':'邓枭枭，女，是一名中国的演员。邓琳凤的哥哥邓枭枭被体操教练郭少华选中练习体操，受哥哥影响，邓琳凤在安徽日本早稻田大学也开始体操训练，同年就读北京体校一年级。', 'TARGET_NAME':'邓枭枭'})
        #record = Record({'TEXT':'张艺谋1945年毕业于广州外贸大学','TARGET_NAME':'张艺谋'})

        print >> fp , obj.run(record)
    
    fp.close()
