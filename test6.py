def checkPalindrome():
 arrayS = []
 for q in range(1, 10):
    for p in range(0, 10):  
      for i in range(0, 10):
        for j in range(0, 10):
          for k in range(0, 10):
            for l in range(1, 10):
              n=100000*q+10000*p+1000*i+100*j+10*k+l
              if(q==l and p==k and i==j):
                arrayS.append(n)
 return arrayS  


def checkDigit():
  arrayN = []
  for i in range(1, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        for l in range(1, 10):
          for m in range(0, 10):
            for n in range(0, 10):
              m=(100*i+10*j+k)*(100*l+10*m+n)
              arrayN.append(m)
  arrayS=checkPalindrome()        
  #print arrayS
  #print arrayN
  arrayR = []
  for t in arrayN:
    for s in arrayS:   
      if(t==s):
        print 'The number is ', long(t)
        #arrayR.append(t) 
  print sorted(arrayR)        
  return 0


#print checkPalindrome(1000000)
#
checkDigit()
