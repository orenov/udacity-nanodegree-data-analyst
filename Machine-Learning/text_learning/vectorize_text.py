#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification

    the list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    the actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project

    the data is stored in lists and packed away in pickle files at the end

"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list
temp_counter = 0
from nltk.corpus import *
sw = stopwords.words('english')

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        ##temp_counter += 1
        ##if temp_counter < 200:
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")
            content = parseOutText(email)


            #for i in ["sara", "shackleton", "chris", "germani"]:
            #    text.replace(i, "")
            stop_words = ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf"]

            for w in stop_words:
                content = content.replace(w, "")

            ### append the text to word_data
            word_data.append( content )

            if name == "sara":
                from_data.append(0)
            else:
                from_data.append(1)
            ### use parseOutText to extract the text from the opened email

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]

            ### append the text to word_data

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris


            email.close()

print "emails processed"
from_sara.close()
from_chris.close()
print word_data[152]
pickle.dump( word_data, open("word_data.pkl", "w") )
pickle.dump( from_data, open("email_authors.pkl", "w") )





### in Part 4, do TfIdf vectorization here

import sklearn
tfidf = sklearn.feature_extraction.text.TfidfVectorizer(stop_words='english')
tfidf.fit_transform(word_data)
print tfidf.get_feature_names()
print len(tfidf.get_feature_names())
print tfidf.get_feature_names()[34597]

