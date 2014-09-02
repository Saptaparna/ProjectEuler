def pandigitalSum():
  array = []
  for i in range(0, 10):
    array.append(i)
  for j in range(0, len(array)-8):  
    print j
    if(array[j]!=array[j+1]):
      if(((10*array[j]+array[j+1])*(100*array[j+2] + 10*array[j+3] + array[j+4]))==(1000*array[j+5]+100*array[j+6]+10*array[j+7]+array[j+8])):
         print array[j], array[j+1], array[j+2], array[j+3], array[j+4], array[j+5], array[j+6], array[j+7], array[j+8]

pandigitalSum()
