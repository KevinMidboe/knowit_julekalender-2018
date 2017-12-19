#!/usr/bin/env python3.6

def main():
   participants = list(range(1, 1501))
   while len(participants) > 1:
      for pers in participants:
         try:
            participants.pop(participants.index(pers) + 1)
         except IndexError:
            participants.pop(0)

      
   return participants.pop()

if __name__ == '__main__':
   main()