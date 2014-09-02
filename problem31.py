
from collections import OrderedDict
import math

def distinctPowers():
   array = []
   for i in range(2, 101):
     for j in range(2, 101):
       array.append(int(math.pow(i, j)))
   list(OrderedDict.fromkeys(array))
   print len(list(OrderedDict.fromkeys(array)))


distinctPowers() 
