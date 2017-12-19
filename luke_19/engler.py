#!/usr/bin/env python3.6
import os
from PIL import Image, ImageDraw

def readFile():
   with open(os.path.dirname(__file__) + '/path.txt', 'r') as f:
      return [line.split(", ") for line in f.read().splitlines()]

def plotRectangle(i, j, board, fill='red'):
   board.rectangle(((100+(10*j), 200+(10*i)), 100+(10*j+10), 200+(10*i+10)), fill=fill, outline="black")
   return board

def main():
   path = readFile()
   boardImg = Image.new('RGB', (400, 300), (255,255,255))
   board = ImageDraw.Draw(boardImg)
   x, y = [0,0]
   plotRectangle(x,y,board, 'green')

   for step, direction in path:
      if (direction == 'north'):
         for n in range(int(step)):
            x -= 1
            board = plotRectangle(x, y, board)
      elif (direction == 'east'):
         for n in range(int(step)):
            print(y)
            y += 1
            board = plotRectangle(x, y, board)
      elif (direction == 'south'):
         for n in range(int(step)):
            x += 1
            board = plotRectangle(x, y, board)
      elif (direction == 'west'):
         for n in range(int(step)):
            y -= 1
            board = plotRectangle(x, y, board)

   return 'batman'
   boardImg.show()

if __name__ == '__main__':
   main()