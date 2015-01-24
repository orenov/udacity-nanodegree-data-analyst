#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then
clean it up. In the first exercise we want you to audit the datatypes that can be found in some 
particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a set of the datatypes
that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def audit_file(filename, fields):
    fieldtypes = {}
    for i in FIELDS:
        fieldtypes[i] = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for field in FIELDS:
            for row in reader:
                if row[field] == "NULL" or row[field] == "":
                    fieldtypes[field].append(type(None))
                elif row[field][0] == '{':
                    fieldtypes[field].append(type([]))
                elif isint(row[field]):
                    fieldtypes[field].append(type(1))
                elif isfloat(row[field]):
                    fieldtypes[field].append(type(1.1))
                #else:
                 #   fieldtypes[field].append(type("sf"))
            f.seek(0)
    for i in fieldtypes:
        fieldtypes[i] = set(fieldtypes[i])

    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()


