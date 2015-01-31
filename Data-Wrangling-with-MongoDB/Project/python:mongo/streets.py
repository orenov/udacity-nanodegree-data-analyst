#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "example.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["вулиця", "бульвар", "проспект", "узвіз", "площа", "провулок", "шосе", "набережна", "тупик", 
            "дорога", "проїзд", "шлях"]

mapping = { "вул.": "вулиця",
            "пр.": "проспект",
            "пл." : "площа",
            'пров.' : 'провулок'
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name.strip())
    m = street_name.split(' ')
    if len(m) > 1:
        street_type = m[-1]
        if street_type.encode('utf-8').lower() not in expected:
            print "{}  -  {}".format(street_type.lower().encode('utf-8'), street_name.encode('utf-8'))

def is_street_name(elem):
    #return (elem.attrib['k'] == "name:en")
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types


def update_name(name, mapping):
    m = street_type_re.search(name)
    if m:
        s = m.group()
        updated_name = street_type_re.sub(mapping[s], name) 
        return updated_name
    return name

if __name__ == '__main__':
    audit('map')