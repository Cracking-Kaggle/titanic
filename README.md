# Titanic

https://www.kaggle.com/c/titanic

## Usage

`run.sh` is an executable file which does following things in order:

1. Extract features from train data:
```shell
  tail -n 891 data/train.csv | python gen_feature.py 1 > train.fea.csv
```
2. Extract labels from train data:
```shell
  tail -n 891 data/train.csv | awk -F"," '{ print $2 }' > train.label.csv
```
3. Extract features from test data:
```shell
  tail -n 418 data/test.csv | python gen_feature.py 0 > test.fea.csv
```
4. Train and predict:
```shell
  python train_n_predict.py train.fea.csv train.label.csv test.fea.csv > answer.label.csv
```
5. Concatenate answers:
```shell
  tail -n 418 data/test.csv | awk -F"," '{ print $1 }' > answer.id.csv; echo 'PassengerId,Survived' > answer.csv; paste -d "," answer.id.csv answer.label.csv >> answer.csv
```
6. Clean up:
```shell
  rm answer.label.csv answer.id.csv
```

`answer.csv` is the desired file for submission

`clean.sh` is another executable file which deletes all temp files (`train.fea.csv train.label.csv test.fea.csv`)
