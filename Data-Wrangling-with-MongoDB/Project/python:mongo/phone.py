#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def convertPhone(phone):
    # First step i'm going to remove all non number characters
    phone = re.sub('\D', '', phone)

    return phone

def key_type(element, keys):
    if element.tag == "tag" and 'k' in element.attrib:
        if element.attrib['k'] in ['phone', 'contact:phone']:
            s = element.attrib['v'].split(',')
            for i in s:
                i = convertPhone(i) 
            print s
    return keys



def process_map(filename):
    data = {}
    for _, element in ET.iterparse(filename):
        data = key_type(element, data)

    return data



def test():
    keys = process_map('map')
    pprint.pprint(keys)

if __name__ == "__main__":
    test()