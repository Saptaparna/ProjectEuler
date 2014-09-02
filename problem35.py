def isPrime(n):
  for i in range(2, n/2+1):
    if(n%i==0):
      return False
  if(n==1):
    return False
  return True

def circularPrimes():
  array = []
  for i in range(0, 10):
    if(isPrime(i)==True):
      print i
  for i in range(0, 10):
    for j in range(0, 10):
      if(isPrime(10*i+j)==True and isPrime(10*j+i)==True):
        print i, j
  for i in range(0, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        if(isPrime(100*i+10*j+k)==True and isPrime(100*j+10*k+i)==True and isPrime(100*k+10*i+j)==True):
          print i, j, k  
  for i in range(0, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        for l in range(0, 10):
          if(isPrime(1000*i+100*j+10*k+l)==True and isPrime(1000*j+100*k+10*l+i)==True and isPrime(1000*k+100*l+10*i+j)==True and isPrime(1000*l+100*i+10*j+k)==True):
            print i, j, k, l
  for i in range(0, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        for l in range(0, 10):
          for m in range(0, 10):
            if(isPrime(10000*i+1000*j+100*k+10*l+m)==True and isPrime(10000*j+1000*k+100*l+10*m+i)==True and isPrime(10000*k+1000*l+100*m+10*i+j)==True and isPrime(10000*l+1000*m+100*i+10*j+k)==True and isPrime(10000*m+1000*i+100*j+10*k+l)==True):
              print i, j, k, l, m
  for i in range(0, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        for l in range(0, 10):
          for m in range(0, 10):
            for n in range(0, 10):
              if(isPrime(100000*i + 10000*j + 1000*k + 100*l + 10*m +n)==True and isPrime(100000*j + 10000*k + 1000*l + 100*m + 10*n +i)==True and isPrime(100000*k + 10000*l + 1000*m + 100*n + 10*i +j)==True and isPrime(100000*l + 10000*m + 1000*n + 100*i + 10*j +k)==True and isPrime(100000*m + 10000*n + 1000*i + 100*j + 10*k +l)==True and isPrime(100000*n + 10000*i + 1000*j + 100*k + 10*l +m)==True):
                print i, j, k, l, m, n 



circularPrimes()
