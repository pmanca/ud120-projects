#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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
#Peter Manca
##The features here are the words in the emails
##The labels are the authors, Chris and Sara. 

##First we need to import the Gaussian Naive Bayes model and the accuracy score function
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#set up Gaussian naive Bayes model
clf = GaussianNB()

#Part 2: set up timer
t0 = time()
#Part 2: First we need to train the model with features and labels
clf.fit(features_train, labels_train)
#Part 2: get the time it takes to train this line was given
print "training time:", round(time()-t0, 3), "s"

#part 2: set up timer
t1 = time()
#Test the model now to get an accurate prediction
prd = clf.predict(features_test)
#Part 2: Get the time it takes to predict something
print "prediction time:", round(time()-t1, 3), "s"

#Get how accurate the prediction was.  we sucked in this function above
print "Accuracy:", accuracy_score(labels_test, prd)




#Results
#Note: It is faster to predict a result then to train a model

'''
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 1.89 s
prediction time: 0.193 s
Accuracy: 0.973265073948
'''
#########################################################


