#! /bin/bash
tail -n 891 data/train.csv | python gen_feature.py 1 > train.fea.csv
tail -n 891 data/train.csv | awk -F"," '{ print $2 }' > train.label.csv
tail -n 418 data/test.csv | python gen_feature.py 0 > test.fea.csv
python train_n_predict.py train.fea.csv train.label.csv train.fea.csv > answer.predict.csv
paste answer.predict.csv train.label.csv > train.auc.csv; auc.sh train.auc.csv
rm train.auc.csv train.fea.csv train.label.csv test.fea.csv answer.predict.csv
