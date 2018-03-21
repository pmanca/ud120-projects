#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#########
#My Code

#get number of people
print len(enron_data)

#get number of features for each person
#need to get the number of falues for each person
#this gets the total number of values in the dict and divides it by the number of people
#this works because each person has the same exact number of features
print sum(len(v) for v in enron_data.itervalues()) / len(enron_data)


#get the number of People of interest(POI)
#data[person_name]["poi"]==1
x = 0
for p in enron_data:
	if enron_data[p]["poi"] == 1:
		x = x + 1


print x


#What is the value of stock for James Prentice
#1095040
print enron_data["PRENTICE JAMES"]["total_stock_value"]

#How many emails from Wesley Cowell to poi

print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']

#What\'s the value of stock options exercised by Jeffrey K Skilling?

print enron_data["SKILLING JEFFREY K"]['exercised_stock_options']

#WHo took home the most money

print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]

#how many peeps ahve a salary
x = 0
for p in enron_data:
	if enron_data[p]["salary"] != "NaN":
		x = x + 1


print x

#how many have an email address
x = 0
for p in enron_data:
	if enron_data[p]["email_address"] != "NaN":
		x = x + 1


print x

#percent of dudes who have NaN for total payments
x = 0
for p in enron_data:
	if enron_data[p]["total_payments"] == "NaN":
		x = x + 1


print x

#percent of POI who have NaN
x = 0
for p in enron_data:
	if enron_data[p]["total_payments"] == "NaN" and enron_data[p]["poi"] == 1:
		x = x + 1


print x

