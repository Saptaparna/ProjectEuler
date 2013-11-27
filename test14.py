from math import factorial

print factorial(100)
string = str(factorial(100))
sum = 0
for i in range(0, len(string)):
  sum += int(string[i])
print sum
