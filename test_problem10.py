def isPrime(n):
  for i in range(2, n/2+1):
    if(n%i==0):
      return False
  return True

def sumPrime():
  array = []
  sumOfPrimes=0
  for i in range(2, 200000):
    if(isPrime(i)==True):
      sumOfPrimes += i
      #print i
  print sumOfPrimes
  return 0

sumPrime() 
