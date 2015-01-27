import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
    d = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in d:
            d[elem.tag] += 1
        else:
            d[elem.tag] = 1
    return d


def run():

    tags = count_tags('map')
    pprint.pprint(tags)

if __name__ == "__main__":
    run()