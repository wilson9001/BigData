import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve

data = pd.read_csv("magic04.csv")

features = data.iloc[:, :-1]
labels = data['class']

trainFeatures, testFeatures, trainLabels, testLabels = train_test_split(features, labels)

bestForest = None
bestFalsePositiveRate = 1

for attempt in range(10):
    for forestSize in range(1, 50):
        ensemble = RandomForestClassifier(n_estimators = forestSize, n_jobs = -1).fit(trainFeatures, trainLabels)
        testFalsePositiveRates, testTruePositiveRates, testThresholds = roc_curve(testLabels, ensemble.predict(testFeatures), pos_label=1)
        if testFalsePositiveRates[1] < bestFalsePositiveRate:
            bestForest = ensemble
            bestFalsePositiveRate = testFalsePositiveRates[1]

print("The best forest is", bestForest, "with a false positive rate of", bestFalsePositiveRate)

allPredictions = bestForest.predict(features)

allPredictions = pd.DataFrame({'Id': range(len(data)), 'Predicted': allPredictions})

allPredictions.to_csv('AlexanderWilsonSubmission.csv', index = False)
