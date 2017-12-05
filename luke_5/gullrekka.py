#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-12-04 16:40:56
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-12-05 11:13:52

def gold():
   gold_row = [1]
   number = 1
   while True:
      countdown = gold_row[number-1]
      while countdown > 0:
         gold_row.append(number)
         countdown -=1
         if len(gold_row) >= 1000000:
            return gold_row
      number +=1

def main():
   row = gold()

   print('Finished with million iterations')
   print(sum(row)+1)

if __name__ == '__main__':
   main()