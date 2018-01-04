#! /bin/bash
tail -n 891 data/train.csv | python gen_feature.py 1 > train.fea.csv
tail -n 891 data/train.csv | awk -F"," '{ print $2 }' > train.label.csv
tail -n 418 data/test.csv | python gen_feature.py 0 > test.fea.csv
python train_n_predict.$1.py train.fea.csv train.label.csv test.fea.csv > answer.predict.csv
tail -n 418 data/test.csv | awk -F"," '{ print $1 }' > answer.id.csv; echo 'PassengerId,Survived' > answer.$1.csv; paste -d "," answer.id.csv answer.predict.csv >> answer.$1.csv
rm train.fea.csv train.label.csv test.fea.csv answer.predict.csv answer.id.csv
