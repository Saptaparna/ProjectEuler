def computeExponentSum():
  array = []
  for i in range(0, 100):
    for j in range(1, 101):
      array.append(i**j)
  #print array
  #print len(array)
  return array

computeExponentSum() 
