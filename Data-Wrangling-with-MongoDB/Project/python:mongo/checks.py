#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag" and 'v' in element.attrib:
        s = element.attrib['v']
        if problemchars.match(s):
            if element.attrib['k'] in keys:
                keys[element.attrib['k']] += 1
            else:
                keys[element.attrib['k']] = 1
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