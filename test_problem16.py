def computePower():
  sring = ''
  number = 2**1000
  #print number
  string = str(number)
  sum = 0 
  for i in range(0, len(string)):
    sum += int(string[i])  
  print sum

computePower()
