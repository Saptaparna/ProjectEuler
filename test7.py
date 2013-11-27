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
    if(n%i==0):
      n = n/i
      print i
  return 0


array1 = []
array2 = []
for i in range(1,20):
  array2.append(i)

def findNumber(n):
  for i in range(1, 20):
   if(n%i==0):
     print i
     array1.append(i)
  if(array1==array2):
     print 'input integers found'
  return 0

for i in range(3000, 100000000):
  findNumber(i) 


def computeGCD(n, m):
  if(m>n and n!=0):
    p = m/n;
    if(p%)
    
   
