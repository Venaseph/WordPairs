#!/usr/bin/env python3

import json
import sys

# Global Variables
match = None
replace = None
folder = None 


def main():
    # Read the file
    data = readJson()
    # Decode the json in dictonary
    obj = json.loads(data)
    list = makeList(obj)
    
    return 0

# reads the json file
def readJson():
    with open('words_dictionary.json', 'r') as json:
        data=json.read()

    return data

def makeList(data):
    list = []
    
    for key in data.keys():
        if len(key) == 4:
            print(key)
            list.append(key)

    return list


# Maincontrol
if __name__ == "__main__":
    sys.exit(main())