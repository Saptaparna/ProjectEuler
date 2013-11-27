def computeDiff():
  sumOfsquares = 0
  for i in range(1, 101):
    sumOfsquares += i**2
  print sumOfsquares
  Sum = 0   
  SquareOfSum = 0 
  for i in range(1, 101):
    Sum += i 
    SquareOfSum = Sum**2
  print SquareOfSum
  print 'Hence the difference is = ', SquareOfSum - sumOfsquares 
  return 0

computeDiff()
