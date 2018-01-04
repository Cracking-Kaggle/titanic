#! /bin/bash
tail -n 891 data/train.csv | python gen_feature.xgboost.py 1 > train.fea.csv
tail -n 891 data/train.csv | awk -F"," '{ print $2 }' > train.label.csv
paste train.label.csv train.fea.csv > train.xgboost.csv
tail -n 418 data/test.csv | python gen_feature.xgboost.py 0 > test.fea.csv
python train_n_predict.xgboost.py train.xgboost.csv test.fea.csv > answer.predcict.csv
tail -n 418 data/test.csv | awk -F"," '{ print $1 }' > answer.id.csv; echo 'PassengerId,Survived' > answer.csv; paste -d "," answer.id.csv answer.predcict.csv >> answer.csv
rm train.fea.csv train.label.csv test.fea.csv answer.predcict.csv answer.id.csv
