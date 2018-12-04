#!/usr/bin/env python3
import os
from PIL import Image
import numpy as np
import itertools

input_image = os.path.join(os.path.dirname(__file__), 'images/input-pokemon_jakt.png') 
output_image = os.path.join(os.path.dirname(__file__), 'images/output-pokemon_jakt.png') 

def main():
  LSB = 4
  image = Image.open(input_image)
  pixels = np.array(image)
  width, height, channels = pixels.shape

  for i,j,k in [(i,j,k) for i in range(width) for j in range(height) for k in range(channels)]:
    value = int(f'{pixels[i][j][k]:b}'[-LSB:], 2)
    pixels[i,j,k] = (255 // 2**LSB) * value

  image = Image.fromarray(pixels)
  image.save(output_image)
  return output_image

if __name__ == '__main__':
  main()



'''
_____
tests

 * compare the hash values of images
 *  compare all bits in every channel
    calls = [hashCompare]
'''

'''
___
previous attempts

for i, j, in itertools.product(width, height, channels):
  encoded_value = int(f'{pixels[i][j][k]:b}'[-LSB:], 2)
  rbg_lsb_ratio = 255 // 2**LSB
  pixels[i][j][k] = rbg_lsb_ratio * encoded_value


for i in range(width):
  for j in range(height):
    for k in range(channels):
      encoded_value = int(f'{pixels[i][j][k]:b}'[-LSB:], 2)
      rbg_lsb_ratio = 255 // 2**LSB
      pixels[i][j][k] = rbg_lsb_ratio * encoded_value

'''