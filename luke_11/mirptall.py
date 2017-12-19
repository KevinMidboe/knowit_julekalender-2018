#!/usr/bin/env python3.6

def palindrome(num):
   return int(str(num)[::-1])

def isPrime(num):
   state = True
   for n in range(2, num):
      if num % n == 0:
         state = False
   return state

def main():
   primes = []
   mirptall = 0
   for n in range(1000):
      if isPrime(n) and n != palindrome(n):
         primes.append(n)

         if (palindrome(n) in primes):
            mirptall += 2

   return mirptall

if __name__ == '__main__':
   main()