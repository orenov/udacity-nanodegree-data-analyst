#!/usr/bin/python

import numpy

def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []
    error = []
    ### your code goes here
    for i in range(len(predictions)):
        error.append(abs(predictions[i] - net_worths[i]))
    perc = numpy.percentile(error, 90)
    print "Percentile"
    print perc
    for i in range(len(error)):
        if error[i] < perc:
            cleaned_data.append((ages[i], net_worths[i], error[i]))

    return cleaned_data

