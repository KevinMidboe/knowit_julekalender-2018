#!/usr/bin/env python3

import os, re

def getVectors(file='./input-rain.txt'):
  path = os.path.join(os.path.dirname(__file__), file)
  with open(path, 'r') as f:
    return f.read().split('\n')

def mostParallelVectors(input):
  parallel_vectors = {}

  for plot in input:
    try:
      v1, v2 = re.sub(r'\(|\)', '', plot).split(';')
    except ValueError as e:
        continue

    x1,y1 = v1.split(',')
    x2,y2 = v2.split(',')
    x1,y1,x2,y2 = [int(x1),int(y1),int(x2),int(y2)]

    slope = (y2 - y1) / (x2-x1)

    if slope in list(parallel_vectors.keys()):
      parallel_vectors[slope] += 1
    else:
      parallel_vectors[slope] = 1

  most = 0
  for vector in parallel_vectors.values():
    if vector > most:
      most = vector
  return most

def main():
  return mostParallelVectors(getVectors())

if __name__ == '__main__':
  print(main())
