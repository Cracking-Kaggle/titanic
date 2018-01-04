"""
XGBoost uses a different input format
"""

import sys
import xgboost as xgb

# read in data
dtrain = xgb.DMatrix(sys.argv[1])
dtest = xgb.DMatrix(sys.argv[2])
# specify parameters via map
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
num_round = 2
bst = xgb.train(param, dtrain, num_round)
# make prediction
for l in bst.predict(dtest):
    sys.stdout.write(str(l) + "\n")
