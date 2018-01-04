"""
Train with extracted features and make predictions on test data
"""

import sys

import xgboost as xgb
import numpy as np

train_fea = open(sys.argv[1])
train_feas = []
for line in train_fea:
    line = line.strip()
    fea = []
    words = line.split(' ')
    for i in range(0, len(words)):
        fea.append(float(words[i]))
    train_feas.append(fea)

train_fea.close()

train_label = open(sys.argv[2])
train_labels = []
for line in train_label:
    line = line.strip()
    train_labels.append(int(line))

train_label.close()

classifier = xgb.XGBRegressor(
    #learning_rate = 0.02,
    n_estimators=2000,
    max_depth=4,
    min_child_weight=2,
    #gamma=1,
    gamma=0.9,
    subsample=0.8,
    colsample_bytree=0.8,
    objective='binary:logistic',
    nthread=-1,
    scale_pos_weight=1
).fit(np.array(train_feas), np.array(train_labels))

test_fea = open(sys.argv[3])

test_feas = []
for line in test_fea:
    line = line.strip()
    fea = []
    words = line.split(' ')
    for i in range(0, len(words)):
        fea.append(float(words[i]))
    test_feas.append(fea)


#print classifier.coef_

test_fea.close()
predicted_labels = classifier.predict(test_feas)
for l in predicted_labels:
    sys.stdout.write(str(l) + "\n")
