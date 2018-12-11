#!/usr/bin/env python3
import os

def getFileContents(path='./input-crisscross.txt'):
  path = os.path.join(os.path.dirname(__file__), path)
  with open(path, 'r') as f:
    return f.read()

def IsNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def decideDirection(cords, action, distance=1):
  if action == 'H':
    cords['x'] += int(distance)
  elif action == 'V':
    cords['x'] -= int(distance)
  elif action == 'F':
    cords['y'] += int(distance)
  elif action == 'B':
    cords['y'] -= int(distance)
  else:
    raise ValueError("Unable to parse action: '{}'".format(action))

def main():
  cords = { 'x': 0, 'y': 0}
  char_buffer = ''

  note_containing_path = getFileContents()
  # note_containing_path = '2H2F2H3B'
  for char in note_containing_path:
    if IsNumber(char):
      char_buffer = str(char)
      continue

    if char_buffer:
      char_buffer += char
      distance, char = [char_buffer[0],char_buffer[1]]
      decideDirection(cords, char, distance)
    else:
      decideDirection(cords, char)

  return '[{},{}]'.format(cords['x'], cords['y'])


if __name__ == '__main__':
  print(main())