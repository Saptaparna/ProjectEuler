for line in open('problem8.txt'):
   array = []
   product = 1
   p = 0
   for i in line.strip():
     array.append(i)
   for j in range(0, len(array)-4):
     product = int(array[j])*int(array[j+1])*int(array[j+2])*int(array[j+3])*int(array[j+4])
     #print product
     if product > p: p = product
   print p  
