"""
Extract features from records
"""
import sys

IS_TRAIN = int(sys.argv[1])
assert IS_TRAIN == 0 or IS_TRAIN == 1
HACK_COUNT = 0

for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    assert len(words) == 12 + IS_TRAIN
    passId = words[0]
    label = words[1]
    pclass = words[1 + IS_TRAIN]
    name = words[2 + IS_TRAIN] + "," + words[3 + IS_TRAIN]
    sex = words[4 + IS_TRAIN]
    age = words[5 + IS_TRAIN]
    sibsp = words[6 + IS_TRAIN]
    parch = words[7 + IS_TRAIN]
    ticket = words[8 + IS_TRAIN]
    fare = words[9 + IS_TRAIN]
    cabin = words[10 + IS_TRAIN]
    embarked = words[11 + IS_TRAIN]
    fea = []
    assert pclass in ["1", "2", "3"]
    if pclass == "1":
        fea.append(1)
        fea.append(0)
        fea.append(0)
    if pclass == "2":
        fea.append(0)
        fea.append(1)
        fea.append(0)
    if pclass == "3":
        fea.append(0)
        fea.append(0)
        fea.append(1)
    assert sex in ["male", "female"]
    if sex == "male":
        fea.append(1)
        fea.append(0)
    else:
        fea.append(0)
        fea.append(1)
    try:
        age = int(age)
    except ValueError:
        age = -5
    assert age == -5 or (age >= 0 and age <= 100)
    age_bucket = int(age / 5)
    assert age_bucket >= -1 and age_bucket <= 20
    for i in range(-1, age_bucket):
        fea.append(0)
    fea.append(1)
    for i in range(age_bucket + 1, 20 + 1):
        fea.append(0)
    fea.append((age + 0.0) / 100)
    sibsp = int(sibsp)
    assert sibsp >= 0 and sibsp <= 8
    fea.append((sibsp + 0.0) / 8)
    parch = int(parch)
    assert parch >= 0 and parch <= 10
    fea.append((parch + 0.0) / 10)
    if fare == "":
        HACK_COUNT += 1
        fare = "100"
    fare = float(fare)
    assert fare >= 0 and fare <= 520
    fea.append(fare / 520)
    assert embarked in ["", "C", "S", "Q"]
    if embarked == "":
        fea.append(1)
        fea.append(0)
        fea.append(0)
        fea.append(0)
    if embarked == "C":
        fea.append(0)
        fea.append(1)
        fea.append(0)
        fea.append(0)
    if embarked == "S":
        fea.append(0)
        fea.append(0)
        fea.append(1)
        fea.append(0)
    if embarked == "Q":
        fea.append(0)
        fea.append(0)
        fea.append(0)
        fea.append(1)
    # print len(fea)
    for i in range(0, len(fea) - 1):
        sys.stdout.write(str(fea[i]) + " ")
    sys.stdout.write(str(fea[len(fea) - 1]) + "\n")

sys.stderr.write("HACK_COUNT=" + str(HACK_COUNT) + "\n")
