#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

#########################################################
#Peter Manca
##The features here are the words in the emails
##The labels are the authors, Chris and Sara. 

##First we need to import the SVM model and the accuracy score function
from sklearn import svm
from sklearn.metrics import accuracy_score

#set up svc model and set the kernal to be linear for the first quiz and rbf for second, clf stands for classifier
#for quiz 33 we play with the C parameter and the value is a float
clf = svm.SVC(kernel='rbf', C=10000)

#Part 2: set up timer
t0 = time()

#cutting down the size of the database to train the model faster
#This will bring down the accuracy
#features_train = features_train[:len(features_train)/100]
#abels_train = labels_train[:len(labels_train)/100] 

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

#Quiz 36 is to print the result for the 10th, 26th and 50th email
print "Email 10 is: ", prd[10]
print "Email 26 is: ", prd[26]
print "Email 50 is: ", prd[50]


#Create empty array to hold Chris's 1s
#BTW i hate python syntax
chris = []
#for loop for each prediction(0 or 1) in prd. if a prediction == 1 then add to array
for x in prd:
	if x == 1:
		chris.append(x)

#print the total number of test events or predictions that were Chris'
print len(chris)


#print "Chris's Total Emails: ", chrisTotal

#Results with a linear kernel
#no. of Chris training emails: 7936
#no. of Sara training emails: 7884
#training time: 0.145 s
#prediction time: 1.252 s
#Accuracy: 0.884527872582

#Results with a rbf kernel
#no. of Chris training emails: 7936
#no. of Sara training emails: 7884
#training time: 0.136 s
#prediction time: 1.467 s
#Accuracy: 0.616040955631

#Results with rbf and C=10
#training time: 0.134 s
#prediction time: 1.437 s
#Accuracy: 0.616040955631

#Results with rbf and C=100
#training time: 0.174 s
#prediction time: 1.505 s
#Accuracy: 0.616040955631

#Results with C=1000
#training time: 0.153 s
#prediction time: 1.387 s
#Accuracy: 0.821387940842

#Results with C=10000
#training time: 0.128 s
#prediction time: 1.157 s
#Accuracy: 0.892491467577

#Results for email 10,26,50
#mail 10 is:  1
#Email 26 is:  0
#Email 50 is:  1

#Chris had 877 test events
