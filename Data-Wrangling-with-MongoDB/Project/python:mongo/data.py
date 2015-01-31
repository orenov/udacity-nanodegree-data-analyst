#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]


def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
        node['type'] = element.tag
        for atr in element.attrib:
            if atr in CREATED:
                if 'created' in node:
                    node['created'][atr] = element.attrib[atr]
                else:
                    node['created'] = {atr : element.attrib[atr]}
            elif atr in ['lon', 'lat']:
                if 'pos' in node:
                    node['pos'].insert(0, float(element.attrib[atr]))
                else:
                    node['pos'] = [float(element.attrib[atr])]
            else:
                node[atr] = element.attrib[atr]
            for tag in element.iter('tag'):
                if problemchars.match(tag.attrib['v']):
                    pass
                elif 'addr:' in tag.attrib['k']:
                    s = tag.attrib['k'].replace('addr:','')
                    if ':' in s:
                        pass
                    else:
                        if 'address' in node:
                            node['address'][s] = tag.attrib['v']
                        else:
                            node['address'] = {s : tag.attrib['v']}
                else:
                    node[tag.attrib['k']] = tag.attrib['v']
            for nd in element.iter('nd'):
                if 'node_refs' in node:
                    node['node_refs'].append(nd.attrib['ref'])
                    node['node_refs'] = list(set(node['node_refs']))
                else:
                    node['node_refs'] = [nd.attrib['ref']]
                    
        return node
    else:
        return None


def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

def test():
     data = process_map('map', False)
    
if __name__ == "__main__":
    test()