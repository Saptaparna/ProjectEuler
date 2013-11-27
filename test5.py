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
  #print array
  for i in array:
    if(n%i==0):
      n = n/i
      #print i
  return 0

#primeFactors(600851475143)
"""
array1 = []
array2 = []
def checkDigit(n):
  for q in range(1, 10):
    for p in range(0, 10):  
      for i in range(0, 10):
        for j in range(0, 10):
          for k in range(0, 10):
            for l in range(0, 10):
              n=100000*q+10000*p+1000*i+100*j+10*k+l
              if(q==l and p==k and i==j):
                array1.append(n)
                m=(100*q+10*j+k)*(100*q+10*k+l)
                array2.append(m) 
                for s in array1:
                  for t in array2:
                    if(s==t): 
                      print s
  return 0

def checkDigit(n):
  for i in range(1, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        n=(100*i+10*j+k)*(100*i+10*j+k) 
        print n
  return 0

"""

def checkPalindrome():
 arrayS = []
 for q in range(0, 10):
    for p in range(0, 10):  
      for i in range(0, 10):
        for j in range(0, 10):
          for k in range(0, 10):
            for l in range(0, 10):
              n=100000*q+10000*p+1000*i+100*j+10*k+l
              if(q==l and p==k and i==j):
                arrayS.append(n)
 return arrayS  


def checkDigit():
  arrayN = []
  for i in range(0, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        m=(100*i+10*j+k)*(100*i+10*j+k)
        arrayN.append(m)
  arrayS=checkPalindrome()	  
  print arrayS
  print arrayN
  for p in arrayN:
    for q in arrayS:   
      if(p==q):
        print 'The number is ', i
  return 0


#print checkPalindrome(1000000)
#
checkDigit()
