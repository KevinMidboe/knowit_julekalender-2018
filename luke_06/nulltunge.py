#!/usr/bin/env python3

def main():
  total = 0
  for i in range(18163106):
    zeros = str(i).count('0')
    if zeros > len(str(i)) - zeros:
        total += i

  return total

if __name__ == '__main__':
  res = main()
  print(res)
