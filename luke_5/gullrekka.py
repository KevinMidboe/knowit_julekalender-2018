#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-12-04 16:40:56
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-12-05 10:36:22

total_loops = 0

def iterate(gold_row, num):
   global total_loops
   try:
      countdown = gold_row[num-1]
   except IndexError:
      countdown = num

   tmp = []
   while countdown >= 1:
      tmp.append(num)
      countdown -=1
      total_loops +=1
      if (total_loops >= 1000000):
         return tmp
   return tmp

def main():
   global total_loops
   gold_row = []
   i = 1
   while total_loops < 1000000:
      gold_row.extend(iterate(gold_row, i))
      i +=1

   print('Finished with million iterations')
   print(sum(gold_row))

if __name__ == '__main__':
   main()