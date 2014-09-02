def triangularNumbers():
  sum = 0
  for i in range(1, 1000000000):
    sum += i 
    array = []
    for j in range(1, 1000000000):
      if(sum%j==0):
        array.append(j)
    print array
    if(len(array)>500):
      print 'Here is the array you are looking for: ', array   
    

triangularNumbers()
