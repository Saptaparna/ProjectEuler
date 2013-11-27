def Souvik():
  array = []
  sumOfPrime = 0
  for i in range(2, 2000000):
    isPrime=True
    for j in array:
     if(j<int(i/2)+1): 
       if (i%j==0):
          isPrime = False
          break
     else: break
    if isPrime:
      array.append(i)
      sumOfPrime += i
  print sumOfPrime

Souvik()
