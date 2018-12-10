#!/usr/bin/env python3

from hashlib import md5
import json, os

def readFile(file='./input-hashchain.json'):
  path = os.path.join(os.path.dirname(__file__), file)
  with open(path, 'r') as f:
    return json.loads(f.read())

def hash(string):
  m = md5()
  m.update(string.encode('utf-8'))
  return m.hexdigest()

def secret(input, prev_hash, solution):
  for el in input:
    char = el['ch']
    value = hash(prev_hash + char)
    if el['hash'] == value:
      solution.append(char)
      secret(input, value, solution)

  return ''.join(solution)

def main():
  return secret(readFile(), hash('julekalender'), [])

if __name__ == '__main__':
  print(main())
