#!/usr/bin/env python3.6

def main():
   n = 0
   while True:
      if (str(n)[-1] == '6'):
         numList = list(str(n))
         numList.insert(0, numList[-1])
         six_prefixed = int(''.join(map(str, numList[:-1])))
         if (six_prefixed/4 == n):
            print('SOLVED:', n)
            return n
      n += 1

if __name__ == '__main__':
   main()