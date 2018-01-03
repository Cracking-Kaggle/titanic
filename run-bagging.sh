#! /bin/bash
tail -n 891 data/train.csv | python gen_feature.py 1 > train.fea.csv
tail -n 891 data/train.csv | awk -F"," '{ print $2 }' > train.label.csv
tail -n 418 data/test.csv | python gen_feature.py 0 > test.fea.csv
python train_n_predict.lr.py train.fea.csv train.label.csv test.fea.csv > predict.lr.csv
python train_n_predict.svr.py train.fea.csv train.label.csv test.fea.csv > predict.svr.csv
paste predict.lr.csv predict.svr.csv | awk '{ average=($1+$2)/2; if (average>0.5) print "1"; else print "0"; }' > predict.csv
tail -n 418 data/test.csv | awk -F"," '{ print $1 }' > answer.id.csv; echo 'PassengerId,Survived' > answer.bagging.csv; paste -d "," answer.id.csv predict.csv >> answer.bagging.csv
rm predict.csv predict.lr.csv predict.svr.csv answer.id.csv
