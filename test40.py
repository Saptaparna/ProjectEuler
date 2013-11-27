def multiply():
  array = []
  for i in range(1, 1000000):
    print i
  return 0

#multiply()

def fileOp():
 string = ''
 for line in open('test40.txt'):
   string += line.strip()
 print string[0]
 print string[9]
 print string[99]
 print string[999]
 print string[9999]
 print string[99999]
 print string[999999]
 print int(string[0])*int(string[9])*int(string[99])*int(string[999])*int(string[9999])*int(string[99999])*int(string[999999])

fileOp()
