def isPrime(n):
  for i in range(2, n/2+1):
    if(n%i==0):
      return False
  return True


array = []
def primeFactors(n):
  for i in range(2, 10000):
    if(isPrime(i)):
      #print i
      array.append(i)
  print array
  for i in array:
    n_new = n
    if(n%i==0):
      n_new = n_new/i
      print i
  return 0

primeFactors(600851475143)
