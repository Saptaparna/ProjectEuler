def isPrime(n):
  for i in range(2, n/2+1):
    if(n%i==0):
      return False
  if(n==1):
    return False
  return True

def quadraticPrimes():
  for n in range(0, 1000):
    for a in range(1, 1000):
      for b in range(1, 1000):
        function1 = n*n + a*n + b
        function2 = n*n - a*n + b
        function3 = n*n + a*n - b 
        function4 = n*n - a*n - b
        if(isPrime(function1)==True):
           print 'function1', n, a, b
        if(isPrime(function2)==True):
           print 'function2', n, a, b
        if(isPrime(function3)==True):
           print 'function3', n, a, b
        if(isPrime(function4)==True):
           print 'function4', n, a, b

quadraticPrimes()
