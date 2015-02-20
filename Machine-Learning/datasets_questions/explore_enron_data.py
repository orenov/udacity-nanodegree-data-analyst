#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import numpy as np

def featureFormat( dictionary, features, remove_NaN=True, remove_all_zeroes=True, remove_any_zeroes=False ):
    """ convert dictionary to numpy array of features
        remove_NaN=True will convert "NaN" string to 0.0
        remove_all_zeroes=True will omit any data points for which
            all the features you seek are 0.0
        remove_any_zeroes=True will omit any data points for which
            any of the features you seek are 0.0
    """


    return_list = []

    for key in sorted(dictionary.keys()):
        tmp_list = []
        append = False
        for feature in features:
            try:
                dictionary[key][feature]
            except KeyError:
                print "error: key ", feature, " not present"
                return
            value = dictionary[key][feature]
            if value=="NaN" and remove_NaN:
                value = 0
            tmp_list.append( float(value) )

        ### if all features are zero and you want to remove
        ### data points that are all zero, do that here
        if remove_all_zeroes:
            all_zeroes = True
            for item in tmp_list:
                if item != 0 and item != "NaN":
                    append = True

        ### if any features for a given data point are zero
        ### and you want to remove data points with any zeroes,
        ### handle that here
        if remove_any_zeroes:
            any_zeroes = False
            if 0 in tmp_list or "NaN" in tmp_list:
                append = False
        if append:
            return_list.append( np.array(tmp_list) )


    return np.array(return_list)


import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

f = open("../final_project/poi_names.txt", "r")

print enron_data["SKILLING JEFFREY K"]

arr = featureFormat(enron_data, ["total_payments", "deferral_payments"])


count = 0
count2 = 0
for i in enron_data:
    if enron_data[i]["total_payments"] == "NaN" and enron_data[i]["poi"]:
        count += 1
    if enron_data[i]["poi"]:
        count2 += 1

print count2
print count

print count/count2