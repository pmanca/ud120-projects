#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

#First I had to install the matplotlib 
#pip install matplotlib

#Import Random Forest(Ensemble algorithm) algorithm and accuracy
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#create classifier with no parameters
clf = RandomForestClassifier()

#fit the classifier and train it with test data
clf.fit(features_train,labels_train)

#Test the model now to get an accurate prediction
prd = clf.predict(features_test)

#Get how accurate the prediction was.  we sucked in this function above
print "Accuracy:", accuracy_score(labels_test, prd)

#Accuract result was .92




try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
