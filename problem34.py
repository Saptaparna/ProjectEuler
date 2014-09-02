from math import *

def digitFactorials():
  for i in range(1, 10):
    for j in range(0, 10):
      if((10*i+j)==(factorial(i)+factorial(j))):
        print i, j
  for i in range(1, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        if((100*i+10*j+k)==(factorial(i)+factorial(j)+factorial(k))):
          print i, j, k 
  for i in range(1, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        for l in range(0, 10):
          if((1000*i+100*j+10*k+l)==(factorial(i)+factorial(j)+factorial(k)+factorial(l))):
            print i, j, k, l
  for i in range(1, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        for l in range(0, 10):
          for m in range(0, 10): 
            if((10000*i+1000*j+100*k+10*l+m)==(factorial(i)+factorial(j)+factorial(k)+factorial(l)+factorial(m))):
              print i, j, k, l, m
  for i in range(1, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        for l in range(0, 10):
          for m in range(0, 10):
            for n in range(0, 10):
              if((100000*i+10000*j+1000*k+100*l+10*m+n)==(factorial(i)+factorial(j)+factorial(k)+factorial(l)+factorial(m)+factorial(n))):
                print i, j, k, l, m, n

digitFactorials()
