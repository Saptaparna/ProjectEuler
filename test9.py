def isPrime(n):
  for i in range(2, n/2):
    if(n%i==0):
       return False
  return True

def storePrime():
  array = []
  for i in range(2, 110000):
    if (isPrime(i)==True):
      array.append(i)
  print array
  print len(array)
  if(len(array)>=10001):
    print array[10001]

storePrime()
