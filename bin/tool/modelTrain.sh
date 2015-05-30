python ModelTrain/SchoolModelTrain.py -i input -c  ../conf/ModelTrain/schoolConf.yaml > train.data


sudo ./../depence/CRF++-0.53/crf_learn -f 3 -c 4.0 template train.data model_school


