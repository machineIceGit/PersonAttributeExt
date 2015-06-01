python ModelTrain/CrfModelTrain.py -i $2 -c ../conf/ModelTrain/$1Conf.yaml > train_data/$1_train.data


sudo ./../depence/CRF++-0.53/crf_learn -f 3 -c 4.0 template train_data/$1_train.data ../data/models/model_$1


