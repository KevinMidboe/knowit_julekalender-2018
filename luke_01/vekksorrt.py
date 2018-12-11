#!/usr/bin/env python3

def fileContents(path='./input-vekksort.txt'):
  import os
  path = os.path.join(os.path.dirname(__file__), path)
  with open(path, 'r') as f:
    return f.read().split('\n')[:-1]

def vekk(numbers):
  vekked = []
  lastLarger = lambda curr, prev: int(curr) >= int(prev)

  for i, num in enumerate(numbers):
    if (i == 0 or lastLarger(num, vekked[-1])):
      vekked.append(int(num))

  return sum(vekked)

def main():
  return vekk(fileContents())

if __name__ == '__main__':
  print(main())