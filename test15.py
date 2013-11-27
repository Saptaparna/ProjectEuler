def findFactors(n):
  for i in range(1, n/2+1):
    if(n%i==0):
      print i
  return 0

def amicableNumbes():
 array = [] 
 sumOfAmicable = 0
 for i in range(1, 284):
    if(isPrime(i)!=True):
      #print i
      array.append(i)
      sumOfAmicable += i
 print sumOfAmicable

findFactors(284)
#amicableNumbes()
