#/usr/bin/python
#coding:utf-8
# vim: set fileencoding=utf-8 :
import os,sys,yaml
from common.featureExt import featureExt
from common.tagger import tagger
import argparse
reload(sys)
sys.setdefaultencoding('utf-8')
#----- ext feature
#----- tagger
#----- training

class SchoolModelTrain:

    def __init__(self, trainFile):
		self._feaExtObj = featureExt()
		self._trainFile = trainFile
	
    def init(self, confDict={}):
		if 'featureList' in confDict:
			feaList =confDict['featureList']
		if 'suffixFile' in confDict:
			self._feaExtObj.setSuffixFile(confDict['suffixFile'])
		if 'prefixFile' in confDict:
			self._feaExtObj.setPrefixFile(confDict['prefixFile'])

		self._feaExtObj.setFeatureList(feaList)

		return True

    def run(self, textLine):
		self._feaExtObj.run(textLine)
		return True

if __name__ == '__main__':
        
		argParse = argparse.ArgumentParser(usage='SchoolExtModelTrain', description='user input args')
		argParse.add_argument('-c','--confYaml', default='../conf/ModelTrain/schoolConf.yaml', help ='model conf yaml file')
		argParse.add_argument('-i' ,'--inputFile', help ='input train file')
		args = argParse.parse_args()
		confYamlFile =args.confYaml 
		fp = open(confYamlFile)
		confDict = yaml.load(fp)
		fp.close()

		Obj = SchoolModelTrain(args.inputFile)
		Obj.init(confDict)
		fp = open(args.inputFile)
		for line in fp:
			line = line.strip().decode('utf8')
			Obj.run(line)
