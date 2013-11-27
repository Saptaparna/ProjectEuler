array = []
sum = 0
for i in range(1, 1001):
  print i**i
  array.append(i**i)
for i in array:
  sum += i
print sum
