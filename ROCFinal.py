import matplotlib.pyplot as plt
import numpy as np

YTruth = np.array([0,0,0,0,1,1,1,0,0,1,1])
YHat = np.array([0.21, 0.46, 0.52, 0.89, 0.45, 0.49, 0.86, 0.24, 0.22, 0.7, 0.53])

cutoffs = np.array([0, 0.25, 0.5, 0.75, 1])

# tpr = np.array([])
# fpr = np.array([])
points = []

for cutoff in cutoffs:
	confusionMatrix = np.array([[0,0],[0,0]])
	YHatTemp = np.array([1 if pred > cutoff else 0 for pred in YHat])
	print(YHatTemp)
	for index in range(len(YTruth)):
		if YTruth[index] == 1 and YHatTemp[index] == 1:
			confusionMatrix[0,0] += 1
		elif YTruth[index] == 0 and YHatTemp[index] == 1:
			confusionMatrix[0,1] += 1
		elif YTruth[index] == 1 and YHatTemp[index] == 0:
			confusionMatrix[1,0] += 1
		else:
			confusionMatrix[1,1] += 1
	
	# tpr = np.append(tpr, confusionMatrix[0,0] / (confusionMatrix[0,0] + confusionMatrix[1,0]))
	# fpr = np.append(fpr, confusionMatrix[1,0] / (confusionMatrix[0,1] + confusionMatrix[1,1]))
	tpr = confusionMatrix[0,0] / (confusionMatrix[0,0] + confusionMatrix[1,0])
	fpr = confusionMatrix[0,1] / (confusionMatrix[0,1] + confusionMatrix[1,1])
	points.append([fpr, tpr])

# plt.plot(fpr, tpr)
# for point in points:
# 	print(point)
# 	fpr, tpr = point
# 	plt.plot(fpr, tpr)
points = np.array(points)
print(points)

plt.plot(points[:,0], points[:,1])
plt.scatter(points[:,0], points[:,1])
plt.show()