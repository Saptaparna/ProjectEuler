def Collatz(n):
  array = []
  while n>1: 
    if(n%2==0):
      n = n/2
    if(n%2!=0):
      n = 3*n + 1
    array.append(n)
  print array

Collatz(13)
