#!/usr/bin/env python3.6

from pprint import pprint

def readFile():
    with open('./verda.txt', 'r') as f:
        read_data = f.read().splitlines()
    f.close()
    return read_data

def main():
    data = readFile()
    for line in data[1:]:
        listview = line.split('\t')
        city = listview[3]
        country = listview[10]
        cord = [listview[12], listview[13]]
        print('place: {}', city, 'in', country)
        print('cord:', cord)

if __name__=='__main__':
    main()
