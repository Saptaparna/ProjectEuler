def PythagoreanTriplet():
  sumOfSquares = 0
  for i in range(1, 500):
    for j in range(2, 501):
      sumOfSquares = i**2 + j**2
      if((sumOfSquares**0.5)%i==0):
        print sumOfSquares 
  return 0

PythagoreanTriplet() 
