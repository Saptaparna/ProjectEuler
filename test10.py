def makeSquare():
  square = 0
  array = [] 
  for i in range(1, 500):
    square = i**2
    array.append(square)
  #print array
  return array

def PythagoreanTriplet():
  arrayi = []
  arrayj = []
  array1 = []
  array2 = []
  array3 = []
  sumOfSquares = 0
  sqrtOfSquare = 0
  for i in range(1, 500):
    for j in range(2, 501):
      sumOfSquares = i**2 + j**2 
      arrayi.append(i**2)
      arrayj.append(j**2) 
      array2.append(sumOfSquares)
  array1 = makeSquare()
  for p in array1:
    for q in array2:
      if(p==q):
        if(p**0.5<1000):
          #print 'Common element < 1000', p 
          print array3.append(p)
  return array3

def solveProblem():
  

PythagoreanTriplet()
#makeSquare()
