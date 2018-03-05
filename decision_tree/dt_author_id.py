#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#Import Decistion tree algorithm and accuracy
from sklearn import tree
from sklearn.metrics import accuracy_score

#set up classifier (part 1) and give it a minimal saples split of 40
clf = tree.DecisionTreeClassifier(min_samples_split=40)

#train the model
clf.fit(features_train, labels_train)

#Test the model now to get an accurate prediction
prd = clf.predict(features_test)

#Get how accurate the prediction was.  we sucked in this function above
print "Accuracy:", accuracy_score(labels_test, prd)

#Part 2 use the given line of code to determine how many featues are in the dataset
#num = len(features_train[0])
print "The number of features are", len(features_train[0])



