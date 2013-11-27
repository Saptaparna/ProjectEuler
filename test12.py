#string = ''
#for line in open('test12.txt'):
  #string += line.strip() 
#print string

string = '235678'

def computeProduct():
  product = 1
  for i in range(0, 5):
    product *= int(string[i])  
    break  
    print product

computeProduct()
