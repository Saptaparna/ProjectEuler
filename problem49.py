def isPrime(n):
  for i in range(2, n/2+1):
    if(n%i==0):
      return False
  if(n==1):
    return False
  return True

def primePermutations():
  array = []
  for i in range(0, 10):
    for j in range(0, 10): 
      for k in range(0, 10):
        for l in range(0, 10):
           if(isPrime(1000*i+100*j+10*k+l)==True and i>0):
             #print i, j, k, l
	     array.append(int(1000*i+100*j+10*k+l))
  for s in range(0, len(array)-1):
    for p in range(0, len(array)-1):
      for q in range(0, len(array)-1):
        if(abs(array[s] - array[p])==3330 and abs(array[p] - array[q])==3330 and array[s]!=array[p] and array[p]!=array[q] and array[q]!=array[s]):	
          print array[s], array[p],  array[q]
    
primePermutations()
     
