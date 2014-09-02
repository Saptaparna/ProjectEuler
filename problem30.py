import math

def fifthPower():
  for i in range(0, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        for l in range(0, 10):
          for m in range(0, 10):
            for n in range(0, 10):
              for o in range(0, 10):
                if(i*1000000 + j*100000 + k*10000 + l*1000 + m*100 + n*10 + o == math.pow(i, 5) + math.pow(j, 5) + math.pow(k, 5) + math.pow(l, 5) + math.pow(m, 5) + math.pow(n, 5) + math.pow(o, 5)):
                   print i, j, k, l, m, n, o         

fifthPower()
