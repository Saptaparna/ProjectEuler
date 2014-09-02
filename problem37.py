def isPrime(n):
  for i in range(2, n/2+1):
    if(n%i==0):
      return False
  if(n==1):
    return False 
  return True

def truncatablePrimes():
  for i in range(0, 10):
     for j in range(0, 10):
       for k in range(0, 10):
         for l in range(0, 10):
           for m in range(0, 10):
             for n in range(0, 10):
                if(isPrime(100000*i+10000*j+1000*k+100*l+10*m+n)==True and isPrime(10000*j+1000*k+100*l+10*m+n)==True and isPrime(1000*k+100*l+10*m+n)==True and isPrime(100*l+10*m+n)==True and isPrime(10*m+n)==True and isPrime(n)==True and isPrime(10000*i+1000*j+100*k+10*l+m)==True and isPrime(1000*i+100*j+10*k+l)==True and isPrime(100*i+10*j+k)==True and isPrime(10*i+j)==True and isPrime(i)==True):
                  print i, j, k, l, m, n

if(isPrime(1)==True): print 'not working'
truncatablePrimes()
