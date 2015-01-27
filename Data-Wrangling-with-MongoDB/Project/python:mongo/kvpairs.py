import xml.etree.ElementTree as ET
import pprint
from itertools import islice

def count_tags(filename):
    d = {}
    for event, elem in ET.iterparse(filename):
        if 'k' in elem.attrib:
            if elem.attrib['k'] in d:
                d[elem.attrib['k']] += 1
            else:
                d[elem.attrib['k']] = 1
    d = sorted(d.iteritems(), key=lambda (k,v): (v,k))
   # d = itertools.islice(d, 10) 
    return d

def run():

    tags = count_tags('map')
    pprint.pprint(tags)

if __name__ == "__main__":
    run()