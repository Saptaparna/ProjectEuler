from collections import Counter
from collections import defaultdict

def pythagorianTriplet():
  array = []
  for i in range(1, 1000):
    for j in range(1, 1000):
      for k in range(1, 1000):
         if(i*i == j*j + k*k and i+j+k<=1000):
            #print i, j, k, i+j+k
            array.append(int(i+j+k))
  #print max(k for k,v in Counter(array).items() if v>1)
  d = defaultdict(int)
  for i in array:
    d[i] += 1
  result = max(d.iteritems(), key=lambda x: x[1])
  print result  

pythagorianTriplet()
