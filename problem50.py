def isPrime(n):
  for i in range(2, n/2+1):
    if(n%i==0):
      return False
  if(n==1):
    return False
  return True

def circularPrime(sum):
  arrayPrime = []
  arraySum = []
  add = 0
  for i in range(2, sum):
    if(isPrime(i)==True): 
      add += i
      arrayPrime.append(i)
      arraySum.append(add)
      print arrayPrime
      #print arraySum
  #for j in arraySum:
    #if(isPrime(arraySum[j])==True):
        

circularPrime(100)
