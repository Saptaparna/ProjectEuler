from __future__ import division
from math import factorial
from decimal import Decimal


def sumPrime():
  sumOfPrimes=0
  for i in range(2, 20000):
    if (long(factorial(i-1)+1))%==i:
      #print (factorial(i-1)+1)
      sumOfPrimes += i
      print i
  print sumOfPrimes
  return 0

sumPrime() 
