#!/usr/bin/env python3
import sys
import json
import csv


def main():
    # Read the file
    data = readJson()
    # Decode the json in dictonary
    obj = json.loads(data)
    # Create list from dictonarys keys of x letter words
    list = makeList(obj, 4)
    saveCsv(list)


    return 0

# reads the json file
def readJson():
    with open('words_dictionary.json', 'r') as json:
        data=json.read()

    return data

def makeList(data, length):
    list = []
    
    for key in data.keys():
        if len(key) == length:
            list.append(key)

    return list

def saveCsv(list):
    with open('wordlist.csv', 'w') as wordlist:
        wr = csv.writer(wordlist, quoting=csv.QUOTE_ALL)
        wr.writerow(list)


# Maincontrol
if __name__ == "__main__":
    sys.exit(main())